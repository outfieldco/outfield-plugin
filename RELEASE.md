# Outfield 1.0.0 release checks

**Status: package prepared; not submitted, approved, or listed.**

## Listing draft

- Name / identifier: Outfield / `outfield`
- Version: `1.0.0`
- Publisher: Outfield business; submit using an Outfield-controlled Cursor account.
- Description: Connect Outfield CRM to search accounts, review activity, deals,
  goals and league play, and log activity using your existing permissions.
- Repository: https://github.com/outfieldco/outfield-plugin
- Homepage / documentation: https://run.outfieldapp.com/docs/mcp
- Support: https://www.outfieldapp.com/support · support@outfieldapp.com
- Privacy: https://www.outfieldapp.com/privacy
- Terms: https://www.outfieldapp.com/agreement
- Release notes: Initial Cursor package for the existing Outfield Streamable HTTP
  MCP server, authenticated through OAuth discovery, dynamic registration and PKCE.

Cursor's authenticated publisher form has not been inspected. Supply any
additional required publisher or listing facts from verified company information.
Do not infer country targeting, commerce declarations, or attestations from this
draft. OpenAI-specific review metadata is not a Cursor submission requirement.

## Release gates

- [ ] Run the Rails regression checklist on the compatibility PR.
- [ ] Human review, merge, and deployment of required callback support.
- [ ] Validate the exact public package checkout with `python3 scripts/validate_package.py`.
- [ ] Load the package in Cursor, verify manifest and MCP discovery, and finish OAuth.
- [ ] Record the actual callback URI and origin hostname for each tested host,
      without tokens, authorization codes, cookies, or customer data.
- [ ] Run all review scenarios against disposable sample data; record outcomes.
- [ ] Check token refresh and revocation, read-only writes, feature permissions,
      and organization/record isolation.
- [ ] Verify ChatGPT and Claude authorization after the server release.
- [ ] Prepare and verify an actual demo recording and private reviewer access if requested.
- [ ] Sign in to https://cursor.com/marketplace/publish using the Outfield publisher account.
- [ ] Complete publisher application and inspect its actual required fields.
- [ ] Submit the public repository only after the preceding verification passes;
      the authorized publisher completes any legal attestations.
- [ ] Record submission confirmation, submitted Git SHA/version, and review status.
- [ ] Address review feedback and record approval/listing URL.
- [ ] Install from the approved listing in Grok Bot, authenticate, discover tools,
      and repeat the representative read/write scenarios.
- [ ] Update README and release status with verified listing and installation evidence.

The current Grok custom connector callback is
`https://grok.com/connectors-oauth-exchange-code/`. Cursor documents
`https://www.cursor.com/agents/mcp/oauth/callback` and
`http://localhost:8787/callback`. Grok Bot's actual callback is **unobserved**.
Do not guess additional callbacks or widen origin rules based on a brand name.
If live testing shows an unrecognized callback/origin, record it and request a
narrow server change before proceeding. Server-side clients may send no Origin;
verify that behavior rather than adding unnecessary hosts.

## Verification record

| Check | Status | Evidence |
| --- | --- | --- |
| Production protected-resource metadata | Passed | Public GET on October 8, 2026 identifies `https://run.outfieldapp.com/mcp` and advertises `ai:read ai:write`. |
| Production authorization-server metadata | Passed | Public GET advertises registration, authorization, token and revocation endpoints, refresh tokens, and PKCE S256. |
| Public tool catalog | Passed | 36 tools returned; each includes boolean `readOnlyHint`, `openWorldHint`, and `destructiveHint` annotations. |
| Support contact | Passed | Published Outfield support page identifies `support@outfieldapp.com`. |
| Package validation | Passed | `python3 scripts/validate_package.py`: Outfield 1.0.0, one remote OAuth MCP connection, existing 300 x 300 PNG logo. Repeat on the submitted Git SHA. |
| Rails regression suite | Not run | User will run tests manually; capture commands, seed, results and failures. |
| Production callback deployment | Not verified | Human merge/deployment required. |
| Cursor local install and OAuth | Not run | Needs an available Cursor test session and deployed callbacks. |
| Grok Bot pre-release install | Not run | Use a supported pre-release connection if available; otherwise verify after listing. |
| Review scenarios / demo | Not run | REVIEW.md contains expected results and a recording script only. |
| Publisher application / submission | Not done | Outfield publisher sign-in and preceding gates required. |
| Marketplace approval / Grok Bot install | Not done | External review and actual installation required. |

For manual runs, append host/version, Git SHA, test date, case, outcome
(Passed/Failed/Blocked/Not run), redacted observations, and evidence location.
Never commit credentials, tokens, OAuth codes, or real customer data.

## Maintaining releases

The Outfield publisher account owns submission and follow-up. Keep support contact
information current. Changes require a version bump, package validation, relevant
host verification, release notes, and another marketplace review. Cursor reviews
updates before publishing; a Git push is not a marketplace update.

References: [submission](https://cursor.com/docs/reference/plugins),
[security and update review](https://cursor.com/help/security-and-privacy/marketplace-security),
[Grok Bot connection flow](https://cursor.com/help/grok-bot/connect-plugins).
