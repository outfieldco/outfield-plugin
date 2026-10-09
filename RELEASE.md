# Outfield 1.0.0 release checks

**Status: package prepared; not submitted, approved, or listed.**

This is Outfield's internal release checklist and evidence log. Cursor reviewers
are not expected to perform these engineering checks or prepare an Outfield test
environment. REVIEW.md contains a short suggested walkthrough using a demo account
and data supplied by Outfield.

## Confirmed Cursor requirements

Cursor's [public submission checklist](https://cursor.com/docs/reference/plugins)
requires a valid plugin manifest, public repository, usage/configuration README,
valid component files and relative paths, and local testing. A supplied logo must
be committed and correctly referenced. Submit the repository link at
https://cursor.com/marketplace/publish; the page currently requires sign-in to
apply as a publisher.

The public checklist does not specify five positive cases, three negative cases,
a demo video, or reviewer account creation. The authenticated form's additional
fields and requirements remain unverified. If access is requested, Outfield
supplies an existing demo login and prepared sample data privately, as with its
previous submissions.

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

## Outfield engineering verification

Owned by Outfield, not Cursor reviewers:

- [ ] Run the Rails regression checklist on the compatibility PR.
- [x] Human merge and deployment of required callback support; production registration verified October 9, 2026.
- [ ] Validate the exact public package checkout with `python3 scripts/validate_package.py`.
- [x] Load the package in Cursor and verify manifest and MCP server discovery.
- [ ] Finish OAuth after required callback support is deployed.
- [ ] Record the actual callback URI and origin hostname for each tested host,
      without tokens, authorization codes, cookies, or customer data.
- [ ] Verify representative read and write workflows using the existing demo account and disposable sample data; record outcomes. REVIEW.md provides optional examples.
- [ ] Check token refresh and revocation, read-only writes, feature permissions,
      and organization/record isolation.
- [ ] Verify ChatGPT and Claude authorization after the server release.

## Publisher submission and follow-up

Owned by the Outfield publisher:

- [ ] Verify an existing demo account works with Cursor and its sample data supports the suggested walkthrough. No reviewer account creation or data preparation is expected.
- [ ] Supply credentials and actual sample record names privately if reviewer access is requested.
- [ ] Provide a demo recording only if requested by the form/reviewers or chosen by Outfield.
- [ ] Sign in to https://cursor.com/marketplace/publish using the Outfield publisher account.
- [ ] Complete publisher application and inspect its actual required fields.
- [ ] Submit the locally tested public repository after Outfield's release verification;
      the authorized publisher completes any legal attestations.
- [ ] Record submission confirmation, submitted Git SHA/version, and review status.
- [ ] Address review feedback and record approval/listing URL.
- [ ] Install from the approved listing in Grok Bot, authenticate, discover tools,
      and repeat the representative read/write scenarios.
- [ ] Update README and release status with verified listing and installation evidence.

The current Grok custom connector callback is
`https://grok.com/connectors-oauth-exchange-code/`. Cursor documents
`https://www.cursor.com/agents/mcp/oauth/callback` and
`http://localhost:8787/callback`. Cursor also registers the native callback
`cursor://anysphere.cursor-mcp/oauth/callback`; production now accepts all three
together. Grok Bot's actual callback is **unobserved**.
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
| Production callback deployment | Passed | October 9, 2026: discovery endpoints returned 200; `POST /oauth/register` with all three Cursor callbacks returned 201 and preserved all three, public-client authentication, and `ai:read ai:write`. Adding a lookalike native callback returned 400 `invalid_redirect_uri`. No user authorization or CRM data access occurred. |
| Cursor local package discovery | Passed | Native Customize UI on October 8, 2026 displays Outfield 1.0.0, its logo, repository/homepage, and MCPs 1. Local checkout installed at `~/.cursor/plugins/local/outfield`. |
| Cursor OAuth | Pending user verification | Production registration blocker resolved October 9, 2026. Reconnect in Cursor and verify browser consent and authenticated tools; these have not been completed by the agent. |
| Grok Bot pre-release install | Not run | Use a supported pre-release connection if available; otherwise verify after listing. |
| Review scenarios / demo | Not run | REVIEW.md contains expected results and a recording script only. |
| Publisher application / submission | Not done | October 9, 2026: publish page displays “Sign in to apply” and requires sign-in for a plugin publisher application. Authenticated fields remain unverified. Outfield publisher sign-in and preceding gates required. |
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
