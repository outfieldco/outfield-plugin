# Outfield

![Outfield logo](assets/logo.png)

Connect your AI assistant to [Outfield](https://www.outfieldapp.com), the CRM for
field teams. Search accounts and people, review activity, deals, goals and league
play, and log new activity with the permissions of the signed-in Outfield user.

This is a Cursor plugin containing one hosted MCP connection. It uses Streamable
HTTP at `https://run.outfieldapp.com/mcp` and OAuth discovery with dynamic client
registration and PKCE S256. No API key, client secret, or pasted access token is
needed. The repository contains no server implementation or workflow skills.

## Release status

Version **1.0.0 is prepared for verification**. The Cursor publisher application,
marketplace review, and Grok Bot installation have not been completed. This
repository's existence does not mean the plugin is listed. See [release checks](RELEASE.md)
and [review scenarios](REVIEW.md) for outstanding work and verification records.

Cursor's web and desktop OAuth callbacks require the corresponding Outfield
server release. Complete the release checks before relying on those connections.

## Requirements

- An active Outfield account in an active organization with the **AI** feature enabled.
- An eligible user role; Viewer users cannot access the AI tools.
- Feature permissions for the tools you use, such as Deals, Goals, Tasks, or Calendar.
- A Cursor or Grok Bot plan and administrator policy allowing this plugin.

The connection does not grant additional organization, team, or record access.
Use `get_user_profile` to inspect the organizations available to your account.

## Install in Cursor

### Local package verification

1. Clone this repository **inside** `~/.cursor/plugins/local/outfield`:
   ```bash
   git clone https://github.com/outfieldco/outfield-plugin.git ~/.cursor/plugins/local/outfield
   ```
   If that directory already exists, use its existing checkout. A symlink to a
   directory outside `~/.cursor/plugins/local` does not load in current Cursor.
2. Restart Cursor or run **Developer: Reload Window**.
3. Open **Customize** and confirm the Outfield plugin and MCP server appear.
4. Authenticate Outfield, sign in using your Outfield account, and review consent.
5. Start a chat and ask: **"Ping Outfield and tell me who I'm connected as."**

Team administrators may need to permit local plugin imports. An installed
marketplace plugin with the same name takes precedence over a local copy.

### Manual MCP configuration

For connector testing without local plugin imports, merge this into your project's
`.cursor/mcp.json` or your personal `~/.cursor/mcp.json`. Preserve existing servers.

```json
{
  "mcpServers": {
    "outfield": {
      "url": "https://run.outfieldapp.com/mcp"
    }
  }
}
```

Authenticate from Customize. Do not add a bearer token or client secret to the file.

### Marketplace installation after approval

Once the listing is approved, find Outfield in Cursor's marketplace or Customize,
install it, and authenticate. An official listing link will be added after approval.

## Install in Grok Bot after approval

Open **Plugins**, search for Outfield, add it, and complete the Outfield OAuth
sign-in. Confirm it appears under Installed and try the ping prompt. A Cursor team
administrator may need to enable it. Availability and authentication must be
verified in Grok Bot after marketplace approval.

Grok's custom connector flow at `grok.com/connectors` is a separate installation
path; completing that flow does not verify a Grok Bot marketplace installation.

## What you can do

- Find accounts and contacts, then inspect details, activity history, and deals.
- Review user and organization activity, tasks, calendar events, goals, and performance.
- Inspect leagues, matchups, standings, leaderboards, and reward pool rankings.
- Browse inventory, product kits, deal options, and custom forms.
- Create deals and record check-ins, meetings, phone calls, emails, text messages,
  notes, tasks, and non-recurring calendar events when your permissions allow.

Examples:

- "Find Acme Grocery and summarize its latest activity."
- "Show my deals for this month."
- "How am I progressing toward my goals?"
- "Log a note on Acme Grocery: follow up next week."

Email and text-message tools **record CRM activity**; they do not send messages.
Calendar creation does not support recurring events. The connector does not
provide account deletion or route optimization tools. Write operations create
real records; use disposable sample data during verification.

The server's current [tool catalog](https://run.outfieldapp.com/docs/mcp/tools.json)
and [MCP documentation](https://run.outfieldapp.com/docs/mcp) describe all inputs,
limits, pagination, prerequisites, and results.

## Authorization and revocation

OAuth requests `ai:read` for reads and `ai:write` for writes. A read-only token can
use read tools but cannot create records. PKCE S256 is required for public clients;
tokens are bound to the Outfield MCP resource and can be refreshed.

Remove the connector in your assistant to stop using it. OAuth clients can revoke
tokens at `https://run.outfieldapp.com/oauth/revoke`; deactivating the Outfield user
invalidates their access. Removing a plugin is not proof that its OAuth tokens were
revoked. Contact Outfield support if you need help revoking access.

## Troubleshooting

| Symptom | What to check |
| --- | --- |
| Plugin missing in Customize | Clone location, reload, local import policy, and an existing marketplace copy. |
| `invalid_redirect_uri` | Server callback support has been deployed; capture the callback URL without tokens or codes. |
| `Forbidden: Origin validation failed` | Capture the requesting origin hostname for Outfield support; do not disable validation. |
| Waiting for authorization in Grok Bot | Use Reopen to finish the browser sign-in. |
| Disabled by team admin | Ask your Cursor team administrator to enable the plugin. |
| AI not enabled / role denied | Ask your Outfield administrator to check the AI feature and your role. |
| Write access not enabled | Reconnect and approve `ai:write`; also check the required feature permissions. |
| Tools missing after a server update | Refresh or reconnect, then start a new chat. |
| An ambiguous account or teammate | Choose the intended search result before using its ID. |

## Support, privacy, and terms

- [Support](https://www.outfieldapp.com/support) · support@outfieldapp.com
- [Privacy policy](https://www.outfieldapp.com/privacy)
- [User agreement](https://www.outfieldapp.com/agreement)
- [Source repository](https://github.com/outfieldco/outfield-plugin)

Connected assistants receive the Outfield data returned to fulfill your requests.
Their own data policies also apply. This package's MIT license covers the connector
configuration and documentation, not access to the hosted Outfield service.
Outfield's name and logo are trademarks; the license grants no trademark rights.

## Maintainers

Validate package files with `python3 scripts/validate_package.py`. Release versions
use semantic versioning. Commit messages must include `[skip ci]`; verification is
performed manually before submission. Follow [RELEASE.md](RELEASE.md) for every
release, including Cursor's separate review of plugin updates.

References: [Cursor plugin format](https://cursor.com/docs/reference/plugins),
[local plugin testing](https://cursor.com/docs/plugins),
[OAuth callbacks](https://cursor.com/docs/mcp),
[Grok Bot connections](https://cursor.com/help/grok-bot/connect-plugins).
