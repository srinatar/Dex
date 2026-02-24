# Jira & Confluence Setup: Push from Dex

**Model:** Dex is your source of truth. You update projects and tasks in Dex, then publish to Jira and Confluence for team visibility.

---

## Part 1: One-Time Setup

### 1.1 Create Atlassian API Tokens

1. Go to [https://id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
2. Click **Create API token**
3. Name it (e.g. "Dex MCP") and copy the token — **you won’t see it again**

> For Jira/Confluence **Server or Data Center**, use a Personal Access Token instead. See [Atlassian docs](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/).

### 1.2 Get Your URLs

- **Jira Cloud:** `https://YOUR-SITE.atlassian.net`
- **Confluence Cloud:** `https://YOUR-SITE.atlassian.net/wiki`

Replace `YOUR-SITE` with your company’s Atlassian site (e.g. `conviva` → `conviva.atlassian.net`).

### 1.3 Add MCP-Atlassian to Cursor

1. Open Cursor → **Settings** → **MCP**
2. Edit the MCP config (e.g. `~/.cursor/mcp.json` or project `.cursor/mcp.json` depending on setup)
3. Add the `mcp-atlassian` server:

```json
{
  "mcpServers": {
    "mcp-atlassian": {
      "command": "uvx",
      "args": ["mcp-atlassian"],
      "env": {
        "JIRA_URL": "https://YOUR-SITE.atlassian.net",
        "JIRA_USERNAME": "your.email@company.com",
        "JIRA_API_TOKEN": "YOUR_JIRA_TOKEN",
        "CONFLUENCE_URL": "https://YOUR-SITE.atlassian.net/wiki",
        "CONFLUENCE_USERNAME": "your.email@company.com",
        "CONFLUENCE_API_TOKEN": "YOUR_CONFLUENCE_TOKEN"
      }
    }
  }
}
```

> **Note:** Same token can be used for Jira and Confluence if your Atlassian account has access to both.
>
> **Python 3.14:** Use `["--python=3.12", "mcp-atlassian"]` if needed.

### 1.4 Install uv (if needed)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart Cursor after updating the MCP config.

---

## Part 2: Publishing Workflow (Dex → Atlassian)

### Push to Confluence

1. Update your project in Dex: `04-Projects/Your_Product/` (status, milestones, blockers).
2. Ask Dex:  
   **"Publish this project status to Confluence: [space key] [parent page title]"**
3. Dex uses MCP `confluence_create_page` or `confluence_update_page` to create or update a Confluence page.

**Example prompts:**
- "Create a Confluence page in our Product space with the current status of [Product X]"
- "Update the Product Health Confluence page with what’s in my Dex project for [Product X]"

**You’ll need:**
- Confluence **space key** (e.g. `PROD`, `TEAM`)
- **Parent page ID or title** (where the page will live)

### Push to Jira

1. Create or update tasks in Dex (`03-Tasks/Tasks.md` or project notes).
2. Ask Dex:  
   **"Create a Jira issue for: [task description]"**  
   or  
   **"Update Jira issue PROJ-123 with status Done"**
3. Dex uses `jira_create_issue` or `jira_update_issue` / `jira_transition_issue`.

**Example prompts:**
- "Create a Jira story in project PROJ: As a PM I need to validate the M&E use case with 3 customers"
- "Transition PROJ-456 to In Progress"
- "Create a Confluence page summarizing my 3 product statuses and link it from the Product space homepage"

---

## Part 3: Cheatsheet – Common Actions

| Goal | Say to Dex |
|------|------------|
| Publish project status | "Publish [Project name] status to Confluence in space [X] under page [Y]" |
| Create Jira story | "Create a Jira story in [PROJ]: [description]" |
| Create Jira bug | "Create a bug in [PROJ]: [description]" |
| Update Jira status | "Move PROJ-123 to Done" / "Transition PROJ-123 to In Progress" |
| Create Confluence page | "Create a Confluence page in [space]: [title] with content from [Dex project/note]" |
| Update Confluence page | "Update Confluence page [ID or title] with [new content summary]" |

---

## Part 4: Confluence Page and Jira Dashboard Tips

### Confluence status page

- Create a single page per product or a "Product Health" page.
- Run `/project-health` in Dex, then:  
  **"Publish this project health table to Confluence page [title] in space [X]"**
- Optionally set a weekly reminder to re-run and update.

### Jira dashboards

- Jira dashboards are built from **filters** and **gadgets**, not from Dex directly.
- Dex creates and updates **issues**. Your existing Jira filters and dashboards will automatically include those issues.
- To surface “Dex-sourced” work: use labels (e.g. `dex`) or a custom field, then add a filter to your dashboard.

---

## Troubleshooting

| Issue | Check |
|-------|--------|
| "MCP server not found" | Restart Cursor; ensure `uvx` is in PATH |
| "Authentication failed" | API token valid, correct email, correct site URL |
| "Page not found" / "Space not found" | Verify space key and parent page; check permissions |
| "Project PROJ does not exist" | Use the correct Jira project key (uppercase, e.g. `PROD`) |

---

## Links

- [MCP-Atlassian on Smithery](https://smithery.ai/server/mcp-atlassian)
- [MCP-Atlassian GitHub](https://github.com/sooperset/mcp-atlassian)
- [Full tools reference](https://personal-1d37018d.mintlify.app/docs/tools-reference)

---

*Last updated: 2026-02-11*
