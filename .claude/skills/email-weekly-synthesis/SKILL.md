---
name: email-weekly-synthesis
description: Email the latest Weekly Synthesis to yourself (or a list) — prepares the email or sends via Gmail if connected.
---

## Purpose

After `/week-review` (or anytime), get the latest **Weekly Synthesis** into your inbox. Either the content is prepared for you to paste into Gmail, or — if you have a Gmail/send MCP connected — it’s sent automatically.

---

## When to Use

- Right after running `/week-review` — "Email me this synthesis."
- Anytime you want the latest weekly synthesis as an email (e.g. to forward to your manager or to read on your phone).

---

## Process

### 1. Find the latest Weekly Synthesis file

- List files in `00-Inbox/` matching `Weekly_Synthesis_*.md`.
- Sort by filename descending (e.g. `Weekly_Synthesis_2026-02-23.md` after `Weekly_Synthesis_2026-02-16.md`).
- The **latest** file is the one with the most recent date in the name. If none exist, tell the user: "No Weekly Synthesis file found. Run `/week-review` first to generate one."

### 2. Read the file and build subject

- Read the full content of the latest file.
- **Subject line:** Use the first heading, e.g. `Weekly Synthesis — Week of 2026-02-23` (strip any leading `#` and trim). If the first line is a markdown title, use that as the email subject.

### 3. Check for send-email capability (optional)

- If the user has a Gmail or Google Workspace MCP that exposes a **send email** (or similar) tool, call it with:
  - **To:** User's email (from `System/user-profile.yaml` if you have a field like `email`, or ask once: "What email should we send the weekly synthesis to?")
  - **Subject:** As above.
  - **Body:** Full synthesis content (plain text or HTML).
- If the tool exists and succeeds, say: "Sent! Check your inbox for **Subject**."
- If no send tool is available, continue to Step 4.

### 4. Prepare email-ready file (when send is not available)

- Write a file: `00-Inbox/Weekly_Synthesis_Email_YYYY-MM-DD.txt` (use the same date as in the synthesis filename).
- **Format:**
  - Line 1: `Subject: Weekly Synthesis — Week of YYYY-MM-DD`
  - Line 2: empty
  - Line 3 onward: full body of the synthesis (plain text; you can strip or keep markdown — plain text is easier for pasting into Gmail).
- Tell the user:
  - "I prepared the email in **`00-Inbox/Weekly_Synthesis_Email_YYYY-MM-DD.txt`**."
  - "Open it, copy everything. The first line is the subject; the rest is the body. Paste into a new Gmail message and send to yourself (or your list)."

### 5. Optional — open default mail client (macOS)

- If the user is on macOS and the body is short enough for a `mailto:` URL (under ~2000 characters), you can suggest: "I can open your default mail client with a draft. Say 'open draft' if you want that."
- If they say yes, run: `open "mailto:?subject=SUBJECT&body=BODY"` with URL-encoded subject and body. For long bodies, skip this and rely on the file.

---

## Summary

1. Find latest `00-Inbox/Weekly_Synthesis_*.md`.
2. Read content; set subject from first heading.
3. If send-email MCP available → send and confirm.
4. Else → write `00-Inbox/Weekly_Synthesis_Email_YYYY-MM-DD.txt` (Subject + body) and tell user to copy into Gmail.

---

## Notes

- **User email:** If you add a field like `email: sriram@conviva.ai` to `System/user-profile.yaml`, the skill can use it when a send tool is available. Until then, "send to yourself" means the user pastes and adds their address.
- **Gmail MCP:** To get one-click send, connect an MCP that can send email (e.g. a Gmail or Google Workspace server with send support). Then this skill can call it in Step 3.
