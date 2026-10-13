# Job Portal / Careers Finder — TinyFish Agent

A TinyFish-powered agent that finds live job and internship openings from company careers pages and job portals, matched to what the user is looking for.

## What it does
- Takes a job title / field + location from the user
- Searches company careers pages and job portals for live openings
- Returns a clean table: Job Title, Company, Location, Salary (if listed), Deadline, Application Link

## How to run
### Option 1: TinyFish Playground (no code)
1. Go to https://agent.tinyfish.ai/playground
2. Paste this task: Find open software engineering internships in New York right now. Check company careers pages (Google, Meta, Amazon) and job portals (LinkedIn, Indeed). For each opening, extract: Job Title, Company, Location, Salary (if listed), Application Deadline, and Application Link. Return results as a clean table sorted by deadline.
3. Watch the agent browse live and return results.

### Option 2: TinyFish API (code)
Run: python3 run.py --title "software engineering intern" --location "New York"
Requires TINYFISH_API_KEY env var.

## Tech
- TinyFish Agent API (natural-language browser automation)
- TinyFish Search API (ranked web search)

## Author
Poorya Dadashi — University of Maryland Global Campus (UMGC)
Built for the TinyFish Student Program / TinyBounties.
