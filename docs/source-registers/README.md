# Current-source registers

Last full verification: 13 July 2026. A scoped source review on 29 October 2026 refreshed thirteen entries and quarantined ten overdue entries; a second scoped review on 31 October 2026 released five quarantines and re-checked one more record from primary text, leaving five quarantined (`UG-DPPR-2021`, `UG-COPYRIGHT-2026`, `KE-DP-GENERAL-2021`, `RW-DPP-2021` and `ITU-INTERNET-USAGE`). Neither review was a full-register or legal review. See the [October 2026 pass 1](../kaizen/2026-10-engine-kaizen/03-currentness.md) and [pass 2](../kaizen/2026-10-engine-kaizen-pass-2/03-currentness.md) currentness records. The freshness gate stays blocked (it exits 1) until each quarantined entry is re-verified or removed from use with its dependent claims retired. The register holds 179 records; the legal and market release gate rows that cite `UG-DPPR-2021` and `KE-DP-GENERAL-2021` rest on quarantined records and are `NOT_ASSESSED` until those are read.

`source-register.json` is the release-controlled register for changing legal, platform and market sources. Tier 1 means a statute, regulator, platform owner or intergovernmental data owner. It does not mean that an interpretation is legal advice or that a platform page will remain unchanged.

## Operating rules

1. Start with the record matching the market, channel and decision. Open the source; never cite this register as though it were the source itself.
2. Record the source ID, access date, relevant section/table, claim and any contradictory evidence in the client evidence log.
3. For market figures, retain the indicator definition, geography, period, population and denominator. Subscribers, accounts, devices, reach estimates and individual users are different measures.
4. For platform policy, verify again on the release date. A passing monthly freshness check does not replace campaign-level review.
5. For legal questions, identify the jurisdiction and processing/advertising act. Escalate material ambiguity, regulated sectors, minors, political/public communications, cross-border data, complaints, or disputed rights to qualified counsel or the responsible regulator.
6. If a source is unavailable, stale or contradictory, mark the check `not assessed`, explicitly quarantine the source record and withhold the affected claim, targeting, collection, publication or approval. A quarantined record remains a failed freshness check; quarantine is not a pass.

## Registers by use

- Legal and privacy: `UG-*`, `KE-*`, `RW-*`, and `TZ-*` records. See [legal and market release gate](../quality-gates/legal-market-release-gate.md).
- Platform and creator policy: `META-*`, `WHATSAPP-*`, `TIKTOK-*`, and `GOOGLE-*` records.
- Market context: `UCC-*`, `ITU-*`, and `UBOS-*` records. Prefer a current national source for national decisions and ITU for definition-aligned comparisons.

## Releasing a quarantine

A quarantined record stays `NOT_ASSESSED` until its primary text has been opened and read. To release it, remove `quarantined`, set `quarantine_released_on` and `verified_on` to the same date, set `support_status` to `partial` or `verified`, and fill `scope` (what was read), `release_basis` (how and when) and `uncertainty` (what was not checked). `scripts/check_source_freshness.py` refuses a release that lacks any of these. Changing a date without reading the source is not a release.

Run the freshness gate:

```sh
python3 -X utf8 scripts/check_source_freshness.py
python3 -X utf8 scripts/check_source_freshness.py --as-of 2026-12-01   # preview which records will be overdue on a future date
```

Adding a record requires a stable unique ID, current URL, publisher, tier, jurisdiction, verification date, review interval, next-review date, intended uses and a verification note. The checker rejects duplicate IDs, missing fields, invalid dates, inconsistent review dates and overdue records.
