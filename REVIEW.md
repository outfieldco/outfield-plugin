# Review scenarios for Outfield 1.0.0

These are suggested examples prepared by Outfield, not a Cursor-mandated test
plan. Cursor's [public submission checklist](https://cursor.com/docs/reference/plugins)
does not specify a scenario count or require a demo video. Additional requirements
in the authenticated publisher form remain unverified.

## Simple reviewer walkthrough

Outfield supplies an existing demo login with sample data through the private
submission channel if reviewer access is requested. Reviewers do not need to
create an Outfield account, configure an organization, enable features, or seed data.

1. Connect the Outfield plugin in Cursor and sign in with the supplied demo login.
2. Ask for the details and recent activity of the sample account named in the
   private reviewer instructions. Results should match its prepared sample data.
3. Optionally ask for the demo user's deals or goals, or log a note on the sample
   account. The note should appear in Outfield; it creates a real disposable record.

The optional examples below give prompts and expected results if more coverage is
useful. There is no claim that Cursor requires reviewers to run all of them.

## Outfield prepares access and data

Reuse the existing demo account used for previous submissions if it supports
Cursor OAuth and has the needed AI, contact, activity, deal, and goal permissions.
Outfield verifies the login and data before supplying access. Give reviewers the
login URL, credentials, actual sample account name, and a few known results privately.
Keep access working during review without dependence on an employee's mailbox or
MFA device.

**Plugin Review Grocery** below is a proposed fixture name, not a verified existing
record. Replace it with an account already in the demo data before sharing prompts.
Outfield supplies recent activity, a deal and goal for the relevant periods, and
disposable records for writes. Reviewers do not prepare these fixtures.

Keep passwords, private login instructions, tokens, and OAuth codes outside this
repository. Organization-isolation and restricted-account fixtures are for
Outfield's own engineering checks, not reviewer setup.

All scenarios below are **Not run**. Record actual evidence in RELEASE.md; an
expected result is not a verified result.

## Optional supported examples

| Case | Natural-language prompt | Expected calls and observable result |
| --- | --- | --- |
| Account lookup | "Find Plugin Review Grocery and show its details." | `search_contacts`, then `get_contact_detail` using the selected returned ID. Name and detail fields agree with the sample account. Clarify if multiple matches exist. |
| Activity summary | "Summarize activity for Plugin Review Grocery this week." | `search_contacts`, then `get_contact_activity` with the selected ID and the user's local week's date range. Summary references returned activity; pagination and empty results are reported honestly. |
| Deals | "Show my deals for this month." | `get_user_deals` with current-month dates in the user's time zone and the authenticated user as default. Returned deal IDs, amounts, and statuses agree with sample records. |
| Goals | "How am I progressing toward my goals?" | `get_user_goals`, optionally `get_user_goal_detail` for detail. Report actual target, progress and period from results, without inventing missing goals. |
| Write | "Log a note on Plugin Review Grocery: [Plugin review] follow up next week." | `search_contacts`, then `create_note` using the selected contact ID and the exact note text. With permitted `ai:write`, one note is created and its returned ID is visible in Outfield. Repeating this scenario intentionally creates another record. |

## Optional unsupported examples

| Prompt | Expected behavior |
| --- | --- |
| "Delete Plugin Review Grocery permanently." | Explain that the connector has no deletion tool. No write tool is used and the account remains present. |
| "Send an actual email to Plugin Review Grocery now." | Explain that the connector logs email activity but does not send email. Do not call `create_email` as a substitute or claim a message was sent. |
| "Create a recurring weekly calendar event for Plugin Review Grocery." | Explain that recurring events are unsupported. Do not silently create a single event or claim recurrence was scheduled. |

## Outfield engineering checks

Outfield verifies these boundaries before release; this is not a reviewer task list.

- Read-only OAuth tokens cannot create notes or deals.
- A user cannot retrieve records from an inaccessible organization or create
  activity on an inaccessible contact. Organization membership and feature
  permissions remain authoritative.
- Missing required feature permissions yield the existing access error.
- Expired/revoked tokens require authentication; no success is fabricated.
- Ambiguous names prompt selection; record IDs come from actual search results.
- Lists respect limits and pagination; no unbounded contact export is attempted.

## Optional demonstration script — recording pending

Record this walkthrough if the publisher form or reviewers request a video, or
if Outfield chooses to provide one. It is not a confirmed Cursor requirement.

1. Show version 1.0.0 loaded in Cursor and finish OAuth without showing credentials.
2. Run the account lookup and activity summary prompts; pause on readable results.
3. Run the goals prompt and compare it with the sample account's known data.
4. Run the note prompt on disposable data; show the created note in Outfield.
5. Ask for account deletion; show the unsupported-operation explanation.

Record real host interactions after callback support is deployed. Replay the video
to check readability and absence of secrets, then host it at a reviewer-accessible
location if requested. No recording or recording URL exists yet. Screenshots or
this script are not evidence that these scenarios passed.
