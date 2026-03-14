---
name: backlog-capture
description: Add one or more backlog items from Field, Peers, or Support to the Backlog Inbox.
---

## Purpose

Capture requests and asks from **Field**, **Peers**, or **Support** into `00-Inbox/Backlog_Inbox.md` so they can be reviewed and prioritized later with `/backlog-review`.

---

## When to Use

- User says: "Field asked for X", "Support escalation: Y", "Add to backlog: Z from [source]"
- User pastes a list of asks from Slack/email and wants them logged
- After a meeting: "Capture these as backlog items: …"

---

## Process

### 1. Get source and description(s)

- **Source** must be one of: **Field** | **Peer** | **Support** (default: Field if unclear).
- **Description:** one-line per item. If user gives a long paragraph, summarize to one clear line.
- **Requested by / Context:** optional (e.g. "Emilyn, NBC" or "Support ticket #1234").

If user didn’t specify, ask: "Who’s it from — Field, Peer, or Support? And one line for the ask?"

### 2. Append to Backlog Inbox

- Open `00-Inbox/Backlog_Inbox.md`.
- In the **Inbox (pending)** table, add one row per item:
  - **Date:** today (YYYY-MM-DD)
  - **Source:** Field | Peer | Support
  - **Description:** one-line ask
  - **Requested by / Context:** optional
  - **Status:** pending
  - **Promoted to:** —
- Keep the table format valid (pipe-separated, header row preserved).

### 3. Confirm

- Tell user: "Added [N] item(s) to Backlog Inbox (Field/Peer/Support). Run `/backlog-review` when you’re ready to prioritize."

---

## Examples

- "Add to backlog: Sales wants a one-pager on MCP use cases for enterprise. From Field."
- "Support escalation — customer needs SSD feed docs by Friday. Add as backlog."
- "Capture this: Engineering asked for clearer API error codes. Peer."

---

## Rules

- Do not assign priority or project here; that happens in `/backlog-review`.
- If the same ask is already in the inbox (duplicate), say so and offer to add a note (e.g. "Also asked by X") instead of a second row.
