# Google Calendar MCP Setup

**Direct Google Calendar integration** — list events, create/update/delete, respond to invitations, check availability across calendars.

---

## Prerequisites

- Node.js 18+
- Google account with Calendar

---

## Step 1: Google Cloud Setup

### 1.1 Create Project & Enable API

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project (or select existing)
3. Enable **Google Calendar API**:
   - APIs & Services → Library → search "Google Calendar API" → Enable

### 1.2 Create OAuth Credentials

1. **APIs & Services** → **Credentials** → **Create Credentials** → **OAuth client ID**
2. If prompted, configure OAuth consent screen:
   - User type: **External** (or Internal for workspace)
   - App name: e.g. "Dex Calendar"
   - Add your email as **Test user** (required for test mode)
3. Create OAuth client:
   - Application type: **Desktop app**
   - Name: e.g. "Dex Calendar MCP"
4. Download the JSON file → save as `gcp-oauth.keys.json`

### 1.3 Save Credentials

Put the file somewhere secure. Recommended:

```
/Users/snatarajan/projects/Dex/.credentials/google-calendar-oauth.json
```

Create the folder if needed:
```bash
mkdir -p /Users/snatarajan/projects/Dex/.credentials
```

Add `.credentials/` to `.gitignore` (credentials must never be committed).

---

## Step 2: Add to Cursor MCP Config

The Google Calendar MCP is already added to your `.mcp.json`. Update the credentials path:

```json
"google-calendar-mcp": {
  "type": "stdio",
  "command": "npx",
  "args": ["-y", "@cocal/google-calendar-mcp"],
  "env": {
    "GOOGLE_OAUTH_CREDENTIALS": "/Users/snatarajan/projects/Dex/.credentials/google-calendar-oauth.json"
  }
}
```

**If your credentials are elsewhere**, edit the `GOOGLE_OAUTH_CREDENTIALS` path in `.mcp.json`.

---

## Step 3: First Run & Authentication

1. **Restart Cursor** (or reload MCP servers)
2. Ask: "What's on my calendar today?"
3. A browser window will open for **Google OAuth**
4. Sign in and grant calendar access
5. Tokens are stored locally — you're done

---

## Step 4: Test

Try:
- "List my calendars"
- "What meetings do I have today?"
- "Create a 30-minute meeting tomorrow at 2pm called 'Test event'"

---

## Tools Available

| Tool | What it does |
|------|---------------|
| `list-calendars` | List all calendars |
| `list-events` | Get events for a date range |
| `create-event` | Create new events |
| `update-event` | Modify events |
| `delete-event` | Remove events |
| `respond-to-event` | Accept/decline invitations |
| `get-freebusy` | Check availability |

---

## Dex Calendar vs Google Calendar MCP

| | Dex Calendar (Apple) | Google Calendar MCP |
|---|----------------------|---------------------|
| **Source** | Calendar.app (macOS) | Google Calendar API |
| **Setup** | Add Google to Calendar.app | OAuth credentials |
| **Platform** | macOS only | Any OS |
| **Features** | Read/write, attendees | + Invitations, free/busy, multi-account |

**Both can coexist.** Dex uses `calendar-mcp` (Apple) for `/daily-plan`; `google-calendar-mcp` adds direct Google access. If you use Google Calendar on macOS, adding your Google account to Calendar.app may make the built-in Dex calendar work without OAuth.

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| "Credentials file not found" | Check path in `.mcp.json`; use absolute path |
| "Test user" error | Add your email in OAuth consent screen → Test users |
| Tokens expire weekly | App is in test mode; publish to production to avoid (see [docs](https://github.com/nspady/google-calendar-mcp#re-authentication)) |
| Re-authenticate | `npx @cocal/google-calendar-mcp auth` (with GOOGLE_OAUTH_CREDENTIALS set) |

---

## Links

- [Google Calendar MCP GitHub](https://github.com/nspady/google-calendar-mcp)
- [Smithery listing](https://smithery.ai/server/google-calendar-mcp)

---

*Last updated: 2026-02-11*
