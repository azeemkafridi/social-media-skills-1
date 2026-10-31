# Currentness record, pass 2 (access date 2026-10-31)

This is a scoped content and source review under the Digital Research currentness gate, not a legal opinion or campaign clearance. A record is released from quarantine only where its primary text was opened and read; the register fields `scope`, `release_basis` and `uncertainty` hold the limits, and `check_source_freshness.py` now refuses a release without them (commit for SM2-01b). Fetched content was treated as data. Working copies of downloaded documents were kept outside the repository.

## Result

| Measure | 29 Oct final | 31 Oct baseline | 31 Oct after SM2-01 |
|---|---:|---:|---:|
| Findings from `check_source_freshness.py` | 10 | 11 | **5** |
| Quarantined and `NOT_ASSESSED` | 10 | 10 | **5** |
| Overdue and not quarantined | 0 | 1 | **0** |

Source: [`logs/baseline-freshness.txt`](logs/baseline-freshness.txt) and [`logs/freshness-after-sm2-01.txt`](logs/freshness-after-sm2-01.txt). The gate still exits 1 for the five records below; that is the intended state until their text is read.

## Records released or re-checked

| Register ID | Route to primary text | What was read | New state and next review |
|---|---|---|---|
| `UG-DPPA-2019` | ULII's own PDF host (`media.ulii.org`, Cap. 97 collection PDF, created 12 August 2026), because the ULII HTML pages return 403 to automated access. Not worked around. | Section list; ss.7, 8, 19, 23, 26, 35 to 37. s.7 states the consent rule and exceptions with no penalty; s.26(2) gives 14 days; s.23(1) requires immediate notice to the Authority; offences are ss.35 to 37. Section numbers unchanged in the Cap. 97 edition. | `partial`, context-bound. PDF says last checked for updates 31 December 2023; later amendment status `NOT_ASSESSED`. Next review 2027-01-29. |
| `UG-UCC-ADS-2019` | UCC-hosted PDF linked from the register page (page dated 31 October 2023). | Preamble; Part 3 interpretation; Part 6 cl.10 testimonials; Annex 4 cl.6, 7, 43, 44; Annex 5; Annex 7. No clause names the internet, social media or influencers. A UCC ruling reported by the Daily Monitor on 28 January 2026 relied on the 2019 standard. | `partial`, context-bound. No amendment linked from UCC; absence not proven. Next review 2027-01-29. |
| `TZ-PDPA` | `pdpc.go.tz` documents path (the registered `www.` host fails certificate validation; URL corrected). | Section list; s.14 (registration before collecting or processing), s.16 (five-year registration), s.35 (direct-marketing right). English version GN 395B, 13 June 2023. | `partial`, context-bound. Later amendments and commencement not read. Next review 2027-01-29. |
| `TZ-PDPR-2023` | `pdpc.go.tz` documents path (URL corrected). | Identity: GN 449C, 4 July 2023. Text searched: no direct-marketing or opt-out procedure appears. | `partial`, context-bound. Substantive rules not read in full. Next review 2027-01-29. |
| `META-AD-STANDARDS` | `transparency.meta.com/policies/ad-standards/` (the registered `facebook.com` URL redirects there; URL corrected). | Twelve top-level headings and the "subject to change at any time without notice" statement. No rule text read; no update date shown. | `partial`, time-sensitive. Supports policy structure only. Next review 2026-11-30. |
| `UG-FACEBOOK-ACCESS-2026` | Re-read of the 13 June 2026 Pulse Uganda article; official-confirmation search repeated. | Article states UCC had made no statement. No UCC or wire-service confirmation found. Reports of January 2026 election-period restrictions do not settle whether Facebook was included. | Remains `partial`, tier 3. Engine wording unchanged ("unstable; verify at the campaign date"). Next review 2026-11-30. |

## Records still quarantined (new access attempt recorded in each register entry)

| Register ID | Attempt on 2026-10-31 | Held out |
|---|---|---|
| `UG-DPPR-2021` | ULII HTML and source URLs return 403; no ULII media PDF for the Regulations found; secondary sources only. | Regulation text, registration and consent-record duties. |
| `UG-COPYRIGHT-2026` | ULII returns 403; no other official route found. | Current copyright conclusions. |
| `KE-DP-GENERAL-2021` | Registered ODPC PDF returns 404; ODPC home shows a maintenance notice; Kenya Law returned an empty challenge response. Register URL is dead; correct URL not found. | Regulation text; the engine's reg.14-18 direct-marketing claims. |
| `RW-DPP-2021` | `dpo.gov.rw` page opened: shows Chapter V (Articles 29 to 36, registration) and the Article 3 consent definition; no law number, gazette date or amendment notice; articles not read. | Article 29 registration claim; direct-marketing provisions. |
| `ITU-INTERNET-USAGE` | DataHub returns 403. The ITU Facts and Figures 2025 landing page was opened: global figures only (nearly three-quarters online, 2.2 billion offline); no East African value. | Country indicator values. |

No skill relies on `ITU-INTERNET-USAGE` (a search of `skills/` found no reference), so the open record blocks the gate without blocking a claim.

## Other items required by the prompt

| Item | Source and access | Result |
|---|---|---|
| FTC Endorsement Guides (`FTC-ENDORSEMENTS-REVIEWS-2026`, in window to 2027-03-23) | [FTC, "FTC's Endorsement Guides: What People Are Asking"](https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides), accessed 2026-10-31 | Page says the Guides were revised in 2023 and that an unexpected material connection should be clearly and conspicuously disclosed. It does not mention the Consumer Reviews and Testimonials Rule (16 CFR Part 465) or give an effective date. The eCFR pages for Parts 255 and 465 redirected to an unblock page and were not opened; the Part 465 effective date therefore rests on the earlier register entry. Register unchanged. |
| Google AI-search guide (`GOOGLE-AI-SEARCH-GUIDE-2026`, in window to 2026-12-07) | [Google Search Central guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), accessed 2026-10-31 | Last updated 2026-07-10 (matches the register); llms.txt and special AI markup are not needed for Google Search; chunking is not required; SEO fundamentals apply. Register unchanged. |
| UCC Advertising Standards | see table above | Text read; influencer or social-media application is an inference. New reference `uganda-advertising-standards-check.md` (SM2-03). |
| Data Protection and Privacy Regulations (Uganda) | see table above | Not reached; stays quarantined. |
| LinkedIn page-field limits (120-character tagline, 2,000-character overview) | Web search restricted to linkedin.com | No LinkedIn Help Centre page found; LinkedIn Learning tutorials support 120 and 2,000, third-party guides say 1,500 for the overview. Stays `NOT_ASSESSED`; not registered. |

## Model-currentness review (mandatory on every Kaizen)

Official sources checked on 2026-10-31: [OpenAI API changelog](https://developers.openai.com/api/docs/changelog) and [Anthropic models overview](https://platform.claude.com/docs/en/models/overview). OpenAI lists GPT-6.1 Terra (26 October 2026, already reviewed in pass 1) and GPT-6 Rosalind (30 October 2026, access limited to organisations approved through its trusted-access programme). Anthropic's roster is unchanged from pass 1: Claude Fable 5.1, Opus 5.5, Sonnet 5.5 and Haiku 5.5. No social skill pins a model. The authorised Luna/high pin is retained: a new release triggers evaluation, not replacement, and no comparison of quality, latency, cost or account availability was run (`NOT_ASSESSED`). No configuration or model policy was changed. The Anthropic row `ANTHROPIC-MODELS-2026` stays as reviewed in pass 1 (next review 2026-11-18).

## Claim-level support gained this pass (P1 audit item)

Claims now checked against primary text: Uganda Act ss.7, 8, 19, 23, 26, 35 to 37; UCC standard testimonial, recognition-of-advertising and split-screen clauses; Tanzanian Act ss.14, 16, 35. One engine claim was found overstated (Uganda s.7 "is an offence", fixed in SM2-02). The broader 179-record claim audit remains open.
