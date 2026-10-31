# Service outage and data-incident communications

Read when a client's own product or service has failed (an app, portal, payment flow or paid subscription is down or degraded) or customer personal data may have been exposed, and the brand must tell customers what is happening. Parent: [playbook-crisis-communications](../SKILL.md). This file covers what is said, to whom, on which channel and under which claim and disclosure rules. It does not diagnose the fault and it is not legal advice. The engine drafts; the client approver publishes (see the parent skill's approval rule).

## 1. Run two tracks from the first minute

| Track | Question it answers | Owner on the client side | Never concluded by the communications team |
|---|---|---|---|
| Service track | Is the service working, for whom, and when will it be? | Technical or incident lead | Cause, scope and recovery time before the lead confirms them |
| Data track | Could personal data have been accessed or acquired by someone not entitled to it? | Privacy lead, with counsel | Whether the event is or is not a personal-data breach |

An outage is not a breach, and it is not "not a breach" until the data track has been worked. Public text states only what each owner has confirmed. If the data track has not started, the statement says the service track is the only thing under way and does not say data is safe.

## 2. Uganda: the statutory anchor (read from primary text)

Data Protection and Privacy Act, Cap. 97 (Act 9 of 2019), read on the ULII PDF on 2026-10-31 (register `UG-DPPA-2019`, status `partial`; amendments after 2023 not checked):

- **s.23(1):** a controller, collector or processor that believes personal data has been accessed or acquired by an unauthorised person must immediately notify the Authority in the prescribed manner, stating the remedial action taken.
- **s.23(2) and (3):** the Authority decides whether the data subject must be told. If so, notice goes by registered mail, email, a prominent place on the responsible party's website, or the mass media.
- **s.23(4):** a notice to data subjects must give enough information for them to protect themselves.
- **s.23(5):** the Authority can direct the responsible party to publicise the compromise.
- **s.20:** the duty to secure personal data with reasonable technical and organisational measures sits in the same Part; do not describe security in the statement as "fully secure" or "unhackable".
- **s.33:** a data subject who suffers damage or distress may apply to a court for compensation. Public text that admits fault or promises compensation should therefore be reviewed by counsel.

The "prescribed manner", any time limit, and what counts as "believes" are in the Regulations (`UG-DPPR-2021`, quarantined: not read) and in PDPO guidance (not read). Kenya, Rwanda and Tanzania breach-notification duties are `NOT_ASSESSED` in this engine. State that in the deliverable; do not fill the gap from memory.

## 3. Sequence

| When | Service track | Data track | Public text |
|---|---|---|---|
| First 30 minutes | Incident lead confirms what is affected and who can confirm scope; names the update owner and next check time | Privacy lead is told if there is any sign of unauthorised access; counsel is alerted for a possible s.23 duty | None yet beyond a support-desk line: "We are aware of a problem and are checking" |
| Within 1 hour | Status page or pinned post live with the confirmed facts | Evidence preserved; decision recorded on whether a notice to the Authority is needed and who made it | Holding statement from section 5, approved by the client approver |
| Every update (agree the interval at intake; do not promise a time you cannot keep) | Update states what changed, what is still unknown, and the next update time | Only text the privacy lead and counsel have cleared | One voice, one message on every channel |
| Recovery | Service owner confirms recovery and what was checked | Open data questions stay open in the text | Resolution statement from section 5 |
| 48 to 72 hours after | Timeline, support-case reconciliation and corrective actions agreed | Notices, if any, issued through the channel the Authority or counsel set | Follow-up only with verified scope and actions |

Severity follows the parent skill's levels. Any sign of personal-data exposure, or a paying-customer outage that reaches media, is handled as Level 3.

## 4. Claim and tone rules

| Topic | Say | Do not say |
|---|---|---|
| Cause | Only a confirmed cause, in plain words | A guessed cause; blame on a supplier, a user or an attacker before it is established |
| Scope | The services and groups confirmed affected | "A small number of users" or "limited impact" without a count and a source |
| Recovery time | A time only when the lead gives one with a confidence level; otherwise the time of the next update | "Within the hour" or "shortly" as a promise |
| Data | "We are investigating whether any personal data was affected" while the data track is open | "No data was affected" before the investigation closes; "all clear" |
| Security | What was done: "we have taken steps to secure the service" | "Fully secure", "unhackable", or "this will never happen again" |
| Money | The refund, credit or service-level remedy in the customer's contract or the client's approved policy, quoted exactly | Any refund, credit, free month or compensation that is not in the contract or approved policy |
| Guarantees | Plain commitments to update and to answer | "Guarantee" or "warranty" for an informal promise: the UCC standard reserves them for formal written undertakings (section 6 cl.14 in the [clause screen](../../../content-writing/references/uganda-advertising-standards-check.md)) |
| Tone | Calm, specific, accountable, no jokes, no exclamation marks | Defensive wording, minimising, or marketing language in an incident post |
| Corrections | Correct an earlier statement visibly, keep the original timestamp and owner | Silent edits or deleted posts |

## 5. Complete example statements (fictional client)

The client below is invented ("Kite Ledger", an invoice-record service for small organisations). Replace every fact with the client's confirmed facts; do not publish an example.

**Holding statement (service track only):** "Some Kite Ledger customers cannot open their workspace at the moment. We are working to find the cause and will post an update by 14:30 East Africa Time. Support is available on the number on our website. We will not guess at a cause or a recovery time before we can confirm them."

**Holding statement (data track open):** "Some Kite Ledger customers cannot open their workspace. We are also checking whether any customer information was affected, and we will tell you what we find as soon as it is confirmed. Please do not send passwords or payment details to us in a message or comment; we will never ask for them in public. Next update by 14:30 East Africa Time."

**Resolution statement:** "Workspaces are opening again for customers who were affected. Our engineers confirmed this by signing in to a sample of affected workspaces at 16:10 East Africa Time. We are still reviewing what caused the interruption and will publish what we learn. Customers who paid for the period of the interruption can read how service credits work in their agreement, and our support team will answer questions about individual accounts."

Facts that must be confirmed before any such text is used: which component failed, who is affected, the time the problem began and ended, what recovery check was done, whether the privacy lead has opened the data track, and the exact remedy in the contract.

## 6. Channels

- Put the full text on the status page or the pinned owned-channel post first; other channels link to it, so there is one source.
- Pause scheduled promotional posts and paid ads that send traffic to the failing service (draft mode, not delete); resume only with client approval.
- WhatsApp: proactive customer notices need an opt-in and, outside the 24-hour customer-service window, an approved template (register `WHATSAPP-BUSINESS-POLICY`, `partial`; account set-up not assessed). Email and SMS follow the client's consent records.
- Support replies use the same wording as the public text, ask for the minimum details, and never invite credentials or payment data in public.

## 7. Evidence and `NOT_ASSESSED`

Record: incident timeline, each statement with its time, approver and the facts it relied on, the data-track decision and who made it, and any notice sent to the Authority. `NOT_ASSESSED` until read or confirmed: Uganda Regulations and PDPO breach guidance, other countries' breach duties, the client's contract terms, and whether UCC or consumer-protection rules apply to the client's service credits.
