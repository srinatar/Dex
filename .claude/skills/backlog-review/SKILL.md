---
name: backlog-review
description: Review and prioritize backlog items from Field, Peers, and Support; promote to tasks or projects.
---

## Purpose

Triage everything in **Backlog Inbox** (`00-Inbox/Backlog_Inbox.md`): assign priority and project/pillar, then **promote** items to `03-Tasks/Tasks.md` or to a project in `04-Projects/`, or mark as deferred.

---

## When to Use

- Weekly (e.g. after `/week-review` or before `/week-plan`)
- When the inbox has grown and you want to clear it
- When you need to decide what to do with incoming asks

---

## Process

### 1. Load backlog and context

- Read `00-Inbox/Backlog_Inbox.md` and list all rows with **Status: pending**.
- Read `System/pillars.yaml` and `04-Projects/ALL_PROJECTS_ONE_VIEW.md` (or list `04-Projects/*.md`) so you know pillars and project names for routing.

### 2. Show pending items

- Present each pending item with:
  - Date, Source, Description, Requested by / Context
- If none: "No pending backlog items. Add some with `/backlog-capture`."

### 3. Triage each item (with user)

For each item (or in a batch), decide:

- **Priority:** P0 | P1 | P2 | Backlog (defer)
- **Project / Pillar:** Which project (e.g. API/MCP/SSD, DPI Launch, VDPI M&E) or pillar (Product-Market Fit, M&E Upsell)? Or "None / General".
- **Action:**
  - **Promote to task:** Create a task in `03-Tasks/Tasks.md` with the right project/pillar (use Work MCP `work_mcp_create_task` if available; else append to the right P0/P1/P2 section with project/pillar tag). Then set **Promoted to** to the task ID or "Tasks.md (P1)" and **Status** to triaged.
  - **Add to project only:** Append the ask to the relevant project’s **Tasks** or **Decisions** in `04-Projects/` (or in `ALL_PROJECTS_ONE_VIEW.md` and run `/sync-projects`). Set **Promoted to** to project name, **Status** to triaged.
  - **Defer:** Set **Promoted to** to "deferred", **Status** to triaged. Optionally move the row to a "Triaged (recent)" or "Deferred" section so the main inbox only shows pending.

### 4. Update Backlog_Inbox.md

- Mark each triaged item: **Status** = triaged, **Promoted to** = task ID, project name, or "deferred".
- Optionally add a "Last review: YYYY-MM-DD" at the bottom.

### 5. Summarize

- "Triaged [N] items: [X] promoted to tasks, [Y] added to projects, [Z] deferred. Backlog Inbox is clear (or [M] still pending)."

---

## Rules

- Don’t delete rows; mark them triaged and record where they went.
- When creating tasks, use the same project/pillar tags you use elsewhere (e.g. #product_market_fit, #mae_upsell, Project: API/MCP/SSD).
- If the user wants to do a quick pass (e.g. "just defer all" or "promote the top 3"), do that and leave the rest for next time.

---

## Integration

- **After review:** User can run `/week-plan` and pull promoted tasks into the week’s priorities.
- **Capture:** New items keep coming in via `/backlog-capture` so the inbox is the single funnel for Field, Peers, and Support.
