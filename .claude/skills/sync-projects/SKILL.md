---
name: sync-projects
description: Sync ALL_PROJECTS_ONE_VIEW.md to individual project files in 04-Projects/
---

Push changes from the single **All Projects — One View** document out to the individual project files so Dex skills (e.g. `/project-health`) see your updates.

## When to Use

- After you edit `04-Projects/ALL_PROJECTS_ONE_VIEW.md` and want those changes reflected in the rest of Dex
- After adding a new project section in the one-view (creates the new file)
- You do **not** need to run this if you only read the one-view

## Process

### 1. Read the one-view file

Read `04-Projects/ALL_PROJECTS_ONE_VIEW.md` in full.

### 2. Parse project blocks

- Split the content by the pattern **`## Project:`** (each project block starts with this).
- Ignore everything before the first `## Project:` (the header and instructions).
- For each block:
  - **First line** is `## Project: <Title>` — capture `<Title>`.
  - **Second line** must be `<!-- file: Filename.md -->` — capture `Filename.md` (no path, no space in the filename).
  - **Body** is everything from the line after the file comment until the next `## Project:` or end of file. Do not include the next `## Project:` line.

### 3. Build each individual file’s content

For each (Title, Filename, Body):

- **Title line:** `# <Title>` (single `#` for the project title).
- **Body:** In the body, replace every line that starts with `### ` with `## ` (so subsection headings become top-level section headings in the individual file). Leave `#### ` as-is or promote to `### ` if you prefer consistency with existing files (existing files use `##` for Q1 Focus, Tasks, etc., and `###` for task sub-heads like "Out of Box (OOB) Metrics").
- **Output:** The file content is: `# <Title>\n\n` + the modified body (no `## Project:` line, no `<!-- file: ... -->` line).

**Heading convention for individual files:**

- One `#` for the project title.
- `## ` for main sections (Q1 Focus, Success Definition, Calendar, Tasks, Next Actions, Key Stakeholders, Timeline & Milestones, Related Meetings, Decisions, References).
- `### ` for sub-sections under Tasks (e.g. "Out of Box (OOB) Metrics", "AI Alerts"). So in the body: turn `### ` → `## `, and `#### ` → `### `.

### 4. Write to disk

For each project block, write the built content to `04-Projects/<Filename>`. Use the exact filename from the `<!-- file: ... -->` line (e.g. `API_MCP_SSD_Export.md`).

### 5. Confirm

Tell the user how many projects were synced and list the filenames updated. If a block was missing `<!-- file: ... -->` or had an invalid format, skip that block and say which one was skipped.

## Rules

- Do not modify `ALL_PROJECTS_ONE_VIEW.md` during this skill — only read from it and write to the individual `04-Projects/*.md` files.
- If the one-view has a new `## Project: ...` with a new `<!-- file: New_Name.md -->`, create `04-Projects/New_Name.md`; no need to pre-create it.
- To remove a project from Dex: the user should delete that project’s section from the one-view and then run `/sync-projects`. The corresponding file in `04-Projects/` will no longer be updated; if the user wants it gone, they can delete the file manually.

## Summary

1. Read `04-Projects/ALL_PROJECTS_ONE_VIEW.md`.
2. Split by `## Project:`, parse Title + `<!-- file: X.md -->` + body per block.
3. For each block: build content with `# Title` and body (promote `###` → `##`, `####` → `###`).
4. Write to `04-Projects/<X.md>`.
5. Report how many files were updated and which ones.
