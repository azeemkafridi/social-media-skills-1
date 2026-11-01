# Task 3 re-run: crisis sequence for a paid-service outage

Routed to `playbook-crisis-communications` and, new in this pass, its [service outage and data-incident reference](../../../../skills/playbooks/playbook-crisis-communications/references/service-outage-and-data-incident-communications.md). Pass 1 wrote this sequence from nothing; this version is built from the engine. Fictional incident: the invented Kite Ledger paid subscription cannot open customer workspaces from 08:00 East Africa Time. No cause, scope or recovery time is defined, and no real service, customer or personal data is involved.

## Severity and owners

Paying customers cannot reach their records and some say they fear a leak: Level 3 under the playbook (a possible personal-data question raises it). Roles: incident lead (technical), client approver, privacy lead, counsel, social media manager (executes approved text only).

## Sequence (from the reference, section 3)

| Time | Action | Who confirms |
|---|---|---|
| 08:30 | Support desk line: "We are aware of a problem and are checking." Scheduled promotional posts and ads that send traffic to the service are paused (draft mode) | Client approver |
| By 09:00 | Incident lead names the component, who can confirm scope, the update owner and the next check time. Privacy lead is told there are reports of fear of a leak; counsel is alerted to a possible s.23 notification duty | Incident lead; privacy lead |
| By 09:30 | Status page and pinned post go live with the holding statement below; other channels link to it | Client approver |
| Every update | What changed, what is unknown, the next update time | Incident lead; privacy lead for any data wording |
| Recovery | Resolution statement only after the incident lead confirms the recovery check | Incident lead |
| 48 to 72 hours | Timeline, support-case reconciliation, corrective actions, follow-up post only with verified scope | Client approver |

## Statements (complete text, fictional)

**Holding statement while the data question is open:** "Some Kite Ledger customers cannot open their workspace. We are also checking whether any customer information was affected, and we will tell you what we find as soon as it is confirmed. Please do not send passwords or payment details to us in a message or comment; we will never ask for them in public. Next update by 11:00 East Africa Time."

**Resolution statement:** "Workspaces are opening again for customers who were affected. Our engineers confirmed this by signing in to a sample of affected workspaces at 12:40 East Africa Time. We are still reviewing what caused the interruption and will publish what we learn. Customers who paid for the period of the interruption can read how service credits work in their agreement, and our support team will answer questions about individual accounts."

## Claim, tone and disclosure review

| Check | Result |
|---|---|
| Cause, scope, recovery time | None stated. The next update time is the only time promised |
| "No data affected" or "all clear" | Not used; the data track is open |
| Security wording | "Fully secure" and "never again" avoided (Act s.20 duty of reasonable measures) |
| Refund, credit, compensation | Only the contract's service-credit route is pointed to; no amount or promise. Act s.33 lets a data subject seek compensation in court, so any admission is counsel's call |
| "Guarantee" | Not used for an informal promise (UCC standard, section 6 cl.14) |
| Statutory step | Act s.23(1): a controller that believes personal data was accessed or acquired by an unauthorised person must immediately notify the Authority. The privacy lead and counsel decide whether that belief exists. The Regulations (`UG-DPPR-2021`, quarantined) and PDPO guidance were not read; other countries' duties are `NOT_ASSESSED` |
| Tone | Plain, calm, specific; no humour, no exclamation marks, no marketing language |
| Influencer or paid-promotion disclosure | Not triggered. If a creator or paid media amplifies the response, add the platform's paid label and "Ad" and run the legal and market release gate |

## NOT_ASSESSED

The client's contract terms and service-credit policy; the PDPO's prescribed manner and any time limit for notification; breach duties in Kenya, Rwanda and Tanzania; whether any UCC or consumer-protection rule applies to service credits; actual incident facts. This is a drill sequence, not a statement for public use.
