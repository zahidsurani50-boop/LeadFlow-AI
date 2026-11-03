# LeadFlow AI | Sales Automation Case Study

**Creator:** Zahid Surani  
**Status:** Self-directed working prototype; not deployed to clients  
**Focus:** Sales operations, automation, customer outreach, workflow design

## Problem
Small businesses often collect sales inquiries in disconnected spreadsheets, inboxes, and forms. Without consistent qualification and follow-up, urgent opportunities can be overlooked.

## Solution
I created a lightweight local CRM to capture incoming leads, suggest their priority, draft relevant follow-up messages, and track them through a sales pipeline. Human review is required before a message is approved; the system does not send emails.

## Workflow
1. Capture lead details and the customer's stated problem.
2. Prioritize the lead and recommend the next action.
3. Draft an email using the customer's context.
4. Edit, approve, and copy the message.
5. Update pipeline status and export a report.

## Technology
Python's built-in HTTP server, SQLite, JavaScript, HTML and CSS. No dependencies for the local demo. Optional OpenAI API integration adds real model-generated lead analysis and follow-up drafting. The free demo uses clearly labeled rule-based scoring, not AI.

## Potential value — not measured
Could reduce manual lead triage and first-draft writing time, standardize follow-ups, and help salespeople prioritize conversations. No customer results or productivity improvements have been measured yet.

## What I'd build next
Connect a lead form and CRM; add a follow-up reminder system; evaluate lead-scoring quality against real outcomes; and add stronger privacy, authentication, and approval safeguards before any real-world deployment.

## Interview pitch
"I wanted to go beyond saying I'm interested in AI and sales automation. I built a functioning prototype that demonstrates how incoming leads can be prioritized, followed up with, and tracked. It combines my sales experience with practical workflow design, and I can show every step live."
