# Review scenarios for Outfield 1.0.0

## Dedicated sample environment

Use a dedicated, active Outfield user in an organization with AI enabled, permitted
contacts, activity, deals, and goals. Give that user only the permissions needed
for these scenarios. Include a sample account named **Plugin Review Grocery**,
recent activity, a current-month deal, and a goal with known progress. Provide a
second organization and a restricted account for access-control checks.

Write tests use disposable sample records only. Keep passwords, login instructions
containing private tenant details, tokens, and OAuth codes outside this repository.
If reviewer access is requested, provide it through the publisher's private
submission channel. Reviewers must not depend on an employee's mailbox or MFA device.

All scenarios below are **Not run**. Record actual evidence in RELEASE.md; an
expected result is not a verified result.

## Five positive scenarios

| Case | Natural-language prompt | Expected calls and observable result |
| --- | --- | --- |
| Account lookup | "Find Plugin Review Grocery and show its details." | `search_contacts`, then `get_contact_detail` using the selected returned ID. Name and detail fields agree with the sample account. Clarify if multiple matches exist. |
| Activity summary | "Summarize activity for Plugin Review Grocery this week." | `search_contacts`, then `get_contact_activity` with the selected ID and the user's local week's date range. Summary references returned activity; pagination and empty results are reported honestly. |
| Deals | "Show my deals for this month." | `get_user_deals` with current-month dates in the user's time zone and the authenticated user as default. Returned deal IDs, amounts, and statuses agree with sample records. |
| Goals | "How am I progressing toward my goals?" | `get_user_goals`, optionally `get_user_goal_detail` for detail. Report actual target, progress and period from results, without inventing missing goals. |
| Write | "Log a note on Plugin Review Grocery: [Plugin review] follow up next week." | `search_contacts`, then `create_note` using the selected contact ID and the exact note text. With permitted `ai:write`, one note is created and its returned ID is visible in Outfield. Repeating this scenario intentionally creates another record. |

## Three unsupported scenarios

| Prompt | Expected behavior |
| --- | --- |
| "Delete Plugin Review Grocery permanently." | Explain that the connector has no deletion tool. No write tool is used and the account remains present. |
| "Send an actual email to Plugin Review Grocery now." | Explain that the connector logs email activity but does not send email. Do not call `create_email` as a substitute or claim a message was sent. |
| "Create a recurring weekly calendar event for Plugin Review Grocery." | Explain that recurring events are unsupported. Do not silently create a single event or claim recurrence was scheduled. |

## Additional boundaries

- Read-only OAuth tokens cannot create notes or deals.
- A user cannot retrieve records from an inaccessible organization or create
  activity on an inaccessible contact. Organization membership and feature
  permissions remain authoritative.
- Missing required feature permissions yield the existing access error.
- Expired/revoked tokens require authentication; no success is fabricated.
- Ambiguous names prompt selection; record IDs come from actual search results.
- Lists respect limits and pagination; no unbounded contact export is attempted.

## Demonstration script — recording pending

1. Show version 1.0.0 loaded in Cursor and finish OAuth without showing credentials.
2. Run the account lookup and activity summary prompts; pause on readable results.
3. Run the goals prompt and compare it with the sample account's known data.
4. Run the note prompt on disposable data; show the created note in Outfield.
5. Ask for account deletion; show the unsupported-operation explanation.

Record real host interactions after callback support is deployed. Replay the video
to check readability and absence of secrets, then host it at a reviewer-accessible
location if requested. No recording or recording URL exists yet. Screenshots or
this script are not evidence that these scenarios passed.
