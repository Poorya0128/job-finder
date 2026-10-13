#!/usr/bin/env python3
"""Job Portal / Careers Finder — TinyFish Agent."""
import argparse, json, os, sys, time, urllib.request
API_BASE = "https://agent.tinyfish.ai"
def _req(url, method="GET", payload=None):
    key = os.environ.get("TINYFISH_API_KEY")
    if not key:
        print("Error: set TINYFISH_API_KEY env var", file=sys.stderr); sys.exit(1)
    data = json.dumps(payload).encode() if payload else None
    req = urllib.request.Request(url, data=data, method=method, headers={"X-API-Key": key, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode())
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", default="software engineering intern")
    ap.add_argument("--location", default="New York")
    args = ap.parse_args()
    goal = f"Find open {args.title} positions in {args.location} right now. Check company careers pages and job portals (LinkedIn, Indeed). For each opening, extract: Job Title, Company, Location, Salary (if listed), Application Deadline, and Application Link. Return results as a clean table sorted by deadline."
    run = _req(f"{API_BASE}/v1/automation/run-async", "POST", {"url": "https://www.linkedin.com/jobs", "goal": goal, "browser_profile": "lite"})
    run_id = run["run_id"]
    print(f"Run started: {run_id}")
    while True:
        status = _req(f"{API_BASE}/v1/runs/{run_id}")
        if status["status"] in ("COMPLETED", "FAILED"):
            print(json.dumps(status.get("result"), indent=2, ensure_ascii=False)); break
        time.sleep(15)
if __name__ == "__main__":
    main()
