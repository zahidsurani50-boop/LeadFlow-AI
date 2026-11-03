# LeadFlow AI — Sales Automation Portfolio Project

**Created by Zahid Surani** · Local-first sales pipeline demo

A working mini CRM that captures leads, prioritizes opportunities, drafts follow-up messages, requires human review, and tracks pipeline progress. Built as a portfolio project for sales, tech sales, and revenue operations applications.

## Getting started

Requirements: Python 3.9+.

1. Clone or download this repository.
2. Open Terminal in the project folder.
3. Copy `.env.example` to `.env`.
4. Leave `AI_MODE=demo` for free rule-based scoring.
5. Run `python3 app.py`.
6. Open **http://127.0.0.1:9000**.

The basic CRM and demo scoring use Python's standard library.

Google Places business discovery requires a Google Maps Platform API key, appropriate API access and billing configuration. Set `GOOGLE_PLACES_API_KEY` in `.env`. Google API usage may incur charges.

## Analysis modes

**Demo mode (default):** Deterministic scoring based on lead information, with template-based outreach suggestions. This is not machine-generated AI analysis.

**Optional OpenAI mode:** Set `AI_MODE=openai` and provide a valid `OPENAI_API_KEY` in `.env`. This requires separately billed API credits.

ChatGPT subscriptions do not include OpenAI API credits.

## Sales workflow

1. Discover businesses through Google Places or add a lead manually.
2. Save discovered prospects and qualify them into CRM leads.
3. Score leads using rule-based demo analysis or optional OpenAI integration.
4. Review and edit outreach drafts.
5. Approve drafts manually.
6. Update pipeline stages and export leads as CSV.

The application does not automatically send emails.

## Security and limitations

- API keys are stored locally in `.env`, which is excluded from Git.
- Local SQLite data and backups are excluded from Git.
- The prototype is intended for local demonstration, not public deployment.
- No authentication or multi-user access controls are implemented.
- Google Places data usage is subject to Google's applicable terms.
- Lead scoring has not been validated against actual sales outcomes.

## Features

- Lead capture with validation and local SQLite storage
- Lead scoring (0–100), Hot/Warm/Cold classification, next-action recommendation
- AI-assisted email drafting when a key is configured
- Human review, editing, approval, and copy-to-clipboard (no sending)
- Pipeline stages: New, Contacted, Meeting booked, Qualified, Closed won, Closed lost
- Dashboard metrics, search, filters, and CSV export
- Local-only Python HTTP server, responsive HTML/CSS/JavaScript interface

## Architecture

```
Browser dashboard (HTML, CSS, JS)
             ↓
Local Python HTTP API (app.py)
          ↙        ↘ optional
SQLite database    OpenAI API
```

Leads are stored in `data/leadflow.db` on your own computer. Stop the server and delete that file to reset. The server listens on `127.0.0.1`, not the public internet.

## Interview demo script (60 seconds)

> "I noticed that many sales teams lose time manually sorting leads and writing the same follow-up emails. I built a local CRM prototype to demonstrate a solution. Here's a fictional gym owner whose trial sign-ups are being missed. I enter their need, budget, and timeline, run an analysis, review the recommended priority, and generate a follow-up draft. I can edit and approve it, then update the pipeline and export the results. The free demo uses scoring rules, while the optional AI mode produces model-generated recommendations and drafts."

## Responsible use and limitations

- The sample leads are fictional, using `example.com` email addresses. Do not enter real customer information without permission and suitable data safeguards.
- In real AI mode, lead fields are sent to the configured AI provider. Review its data practices before use.
- Scores are heuristic prioritization suggestions, **not** conversion probabilities or measured performance improvements.
- **Approve** updates the local dashboard; it does **not** send an email.
- This is a portfolio prototype, **not production software**. It lacks authentication, multi-user access, production security controls, and CRM/email integrations. Do not expose it publicly.
- The API key is read from an environment variable, never stored in the app's database or web frontend.

## Next improvements

1. Connect a Google Form to the lead intake API.
2. Connect a CRM such as HubSpot.
3. Measure time-to-first-response and actual meeting conversion on consented, anonymized data.
4. Add reminders and permission-based email sending with an explicit approval gate.

## Files

- `app.py` — local backend and database
- `static/index.html` — dashboard
- `tests/test_app.py` — automated tests
- `PROJECT_CASE_STUDY.md` — employer-facing portfolio write-up
- `.gitignore` — excludes local database and credentials
