# Social Media Skills Engine

The Social Media Skills Engine (repository `social-media-skills`) is the Chwezi digital marketing and advertising engine: a library of 112 routed skills for consultancy work in Uganda and East Africa. It covers marketing foundations and positioning, channel selection, advertising strategy and budgeting, brand building and distinctive assets, media planning, programmatic buying and brand safety, marketing mix modelling, creative briefs, ad copy, paid search and paid social build specifications, content and copywriting in British, East African English, French and Kiswahili, campaign and community operations, measurement, attribution and reporting, AI-assisted marketing, agency business development and client training. Its produced outputs include client briefs and personas, social-media, digital-marketing and campaign strategies, media plans with reach and frequency calculations, advertising budgets and decision memos, creative briefs, ad copy sets, Google Ads and Meta/TikTok/LinkedIn campaign specifications, content calendars, publication-ready copy, audits, dashboards and monthly reports, ROI business cases, operating playbooks, organisational policies, proposals and training workbooks.

The engine works to named standards rather than house opinion. Personal-data and direct-marketing work is checked against the Uganda Data Protection and Privacy Act 2019 (read from primary text, with a recorded scope), with the Ugandan 2021 Regulations and the Kenyan, Rwandan and Tanzanian data-protection laws held in a dated source register (`docs/source-registers/source-register.json`, 179 records under a freshness gate). The Ugandan Regulations and the Kenyan and Rwandan records are quarantined as `NOT_ASSESSED` until their primary text is read (see [Quality and improvement](#quality-and-improvement)); advertising claims against the Uganda Communications Commission Advertising Standards 2019, through a clause screen that marks application to social posts `NOT_ASSESSED` because the standard names neither social media nor influencers, and the ICC Advertising and Marketing Communications Code; influencer disclosure against the FTC Endorsement Guides and ASA/CAP guidance; platform mechanics against the Meta, WhatsApp, TikTok, LinkedIn and Google policy pages in the same register; and web accessibility against WCAG 2.2. Method draws on named practitioner texts, among them Chaffey's RACE, Bodnar and Cohen's social ROI formula, Weinberg and Mares's Bullseye and Kotler's segmentation and positioning (full list under References). Every deliverable passes an anti-slop and human-review gate. The engine is for agency owners, account leads, strategists, media planners, copywriters, paid-media specialists, in-house marketing teams and founders who need reviewable, evidence-backed marketing decisions. It plans, specifies, writes, audits and reports; spending money, changing live ad accounts, publishing and contacting people always require explicit client authority.

## Installation

Prerequisites: Claude Code for the plugin route; Node.js 18 or later for the installer scripts; Python 3.11 or later (CI uses 3.12) with `PyYAML` for the validators and tests; Git for cloning.

### Claude Code plugin

The repository ships a Claude Code marketplace (`.claude-plugin/marketplace.json`, marketplace `chwezi-social`) containing one plugin, `social`:

```text
/plugin marketplace add https://github.com/peterbamuhigire/social-media-skills
/plugin install social@chwezi-social
```

### Installer scripts

`install.sh` and `install.ps1` both delegate to `scripts/install-engine.js`, which copies `skills/`, `hooks/` and `rules/` into a Claude root and records what it wrote in `.chwezi/install-state.json`, so uninstall removes only its own files. `--scope user` (the default) targets `~/.claude`; `--scope project` targets `.claude` in the current directory. `--dry-run` prints the plan without writing.

```sh
git clone https://github.com/peterbamuhigire/social-media-skills
cd social-media-skills
bash install.sh --scope project --dry-run   # macOS, Linux or Git Bash; drop --dry-run to install
.\install.ps1 --scope user                  # Windows PowerShell
node scripts/install-engine.js doctor --scope user
node scripts/install-engine.js uninstall --engine social-media-skills --scope user
```

### Codex

Codex reads the standard layout directly: clone the repository and point Codex at [`AGENTS.md`](AGENTS.md), which routes to `skills/<category>/<skill-name>/SKILL.md`. The Codex-only model-policy check is described in [`.codex/README.md`](.codex/README.md):

```text
python3 <engine-root>/.codex/ensure_model_policy.py --runtime codex --check
```

Claude skips that step. The check exits 1 and reports drift when no Codex configuration exists.

### Manual use

Clone the repository, read [`CLAUDE.md`](CLAUDE.md) (which imports [`AGENTS.md`](AGENTS.md)) as the router, then open the matching `SKILL.md` and its `references/`.

## Validation

Run these from the repository root before a release. `python3 -m pip install PyYAML` is the only dependency the Python checks need (`pyyaml` 6.0.3 was used on 31 October 2026); there is no requirements file. The test suite is `unittest`, which is what CI runs; `pytest` is optional and collects the same tests.

```sh
python3 -m pip install PyYAML
python3 -X utf8 scripts/validate_skill_engine.py --baseline quality-baseline.json
python3 -X utf8 scripts/check_package_integrity.py
python3 -X utf8 scripts/check_machine_paths.py
python3 -X utf8 scripts/check_skill_aliases.py
python3 -X utf8 scripts/routing_smoke_test.py --min-rank1 92 --lint-fixtures
python3 -X utf8 scripts/check_source_freshness.py
python3 -X utf8 scripts/source_ingestion_guardrail.py
python3 -X utf8 -m unittest discover -s tests -p "test_*.py"
python3 -X utf8 tests/agent-integration/test_social_media_agent_contract.py
node hooks/test-destructive-bash-gate.js
node hooks/test-plugin-hook-config.js
node scripts/generate-plugin-manifest.js --engine . --check
python3 -X utf8 skills/meta-utility/skill-writing/scripts/quick_validate.py skills/<category>/<skill-name>
```

| Command | What it checks | Result on 2026-10-31 |
|---|---|---|
| `validate_skill_engine.py --baseline quality-baseline.json` | Skill contract, 300-line budget, zero-debt baseline | Exit 0: 112 skills, 112 compliant, median 121 lines |
| `check_package_integrity.py` | The 5,000-entry ceiling on the checkout and the package tree | Exit 0: 0 findings |
| `check_machine_paths.py` | No host-specific paths in active content | Exit 0 |
| `check_skill_aliases.py` | Retired-skill routes and the 120-skill cap | Exit 0: 83 routes, 112 active |
| `routing_smoke_test.py --min-rank1 92 --lint-fixtures` | 400 routing fixtures, owned negatives, fixture lint (lexical proxy, not live routing) | Exit 0: 400 of 400 in the top three, precision at 1 381 of 400 (95.2%), 125 of 125 owned negatives |
| `check_source_freshness.py` | Source register: overdue, quarantined or malformed records | **Exit 1**: five quarantined records (see [Quality and improvement](#quality-and-improvement)) |
| `source_ingestion_guardrail.py` | No book extractions or reconstructive book content | Exit 0: 0 findings |
| `unittest discover` | The repository test suite | Exit 0: 116 tests (`pytest` 9.0.3 also reports 116 passed) |
| `tests/agent-integration/test_social_media_agent_contract.py` | The engine manifest against the router, skill glob and the coordination catalogue | Exit 0 (reports `NOT ASSESSED` for the catalogue when `chwezi-engine-agents` is not a sibling folder) |
| `hooks/test-destructive-bash-gate.js`, `hooks/test-plugin-hook-config.js` | The shipped command-gate hook | Exit 0: 61 of 61 and 7 of 7 |
| `generate-plugin-manifest.js --engine . --check` | `.claude-plugin/plugin.json` lists every active skill | Exit 0: current, 112 skills |
| `quick_validate.py <skill-dir>` | One skill's frontmatter and structure | Exit 0 for the two skill folders run (`playbook-crisis-communications`, `blog-writer`) |

Also available: `scripts/validate_media_plan_provenance.py <plan.json> [--as-of YYYY-MM-DD]` checks the evidence origin of a media plan's numeric inputs and the source state of the platform specifications it cites; `scripts/campaign_behaviour.py` and `scripts/kaizen_phase1_contracts.py` run synthetic fixtures; `scripts/measure_skill_scaffolding.py` reports repeated scaffolding.

Which checks need extra tools: none of the Python or Node checks above needs PowerShell, Pandoc, Mermaid, a browser, LibreOffice or a container. They ran on Linux (Fedora 44, Python 3.14.8, Node 22). Not exercised on Linux: `install.ps1` (needs PowerShell, which was not installed), and `install.sh` without `--dry-run` (it writes to a Claude root; use `--scope project` in a scratch folder). `install.sh` is not marked executable in the repository, so call it through `bash`. Producing `.docx`, `.pdf` or `.xlsx` deliverables is separate from validation and needs the tools named in `AGENTS.md` under Document and Spreadsheet Tooling.

## Capabilities

112 active `SKILL.md` files across 15 category folders under `skills/` (a further folder, `frameworks/`, holds only inactive aliases). The tables below were regenerated from the filesystem and `docs/skill-aliases.yml` on 29 Sep 2026; `tests/test_engine_quality.py` fails if they drift from either. The 2026-09-29 consolidation retired 83 skills: each stays on disk as an inactive `ALIAS.md`, and [docs/skill-aliases.yml](docs/skill-aliases.yml) routes it to the active skill that now holds its content (see [Retired skill routes](#retired-skill-routes)).

| Category | Skills |
|---|---:|
| `advertising` | 11 |
| `ai-marketing` | 6 |
| `business-development` | 6 |
| `content-writing` | 7 |
| `frameworks` | 0 (inactive aliases only) |
| `language` | 4 |
| `meta-analytics-ops` | 13 |
| `meta-utility` | 3 |
| `pipeline` | 13 |
| `platforms` | 8 |
| `playbooks` | 17 |
| `policies` | 1 |
| `sectors` | 2 |
| `seo-discovery` | 2 |
| `strategy` | 15 |
| `training` | 4 |
| **Total** | **112** |

| Category | Skill | What it does |
|---|---|---|
| `advertising` | `ad-copy-and-hook-lab` | Writes and tests ad headlines, hooks, offers, proof lines and guarantees across media. |
| `advertising` | `ad-testing-and-scaling` | Designs ad tests, reads results and decides what to scale, kill or refresh. |
| `advertising` | `ad-to-site-journey-handoff` | Hands campaign traffic to a landing page with message match, UTMs, events and consent. |
| `advertising` | `advertising-attribution-and-measurement` | Defines conversion events, attribution models, incrementality tests and break-even ROAS/CPA. |
| `advertising` | `advertising-strategy-and-budget` | Sets advertising objectives, measurement levels, triangulated budgets and governance terms. |
| `advertising` | `creative-brief-and-big-idea` | Writes the strategic creative brief, finds the insight and screens campaign ideas. |
| `advertising` | `direct-response-economics` | Builds pro-forma P&L, break-even and roll-out ladders for response campaigns. |
| `advertising` | `marketing-mix-modelling` | Specifies a marketing mix model (Meridian or Robyn), its data floor, experiment calibration and which evidence governs which budget decision. |
| `advertising` | `media-planning` | Builds and reviews media plans: reach, frequency, GRPs, CPM, flighting and post-buy. |
| `advertising` | `paid-search-advertising` | Plans, specifies and audits Google Ads Search, Performance Max and Demand Gen. |
| `advertising` | `programmatic-and-brand-safety` | Plans programmatic, CTV, DOOH and audio buying with viewability, invalid-traffic, supply-path and brand-suitability controls. |
| `ai-marketing` | `ai-generative-search-optimisation` | Plans brand visibility in AI and generative search answers. |
| `ai-marketing` | `ai-readiness-diagnostic` | Produces a scored AI readiness diagnostic for a marketing team. |
| `ai-marketing` | `ai-slop-audit` | Audits content for generic AI patterns and sets remediation. |
| `ai-marketing` | `ai-use-case-mapping` | Maps and prioritises AI use cases across the marketing workflow. |
| `ai-marketing` | `anti-ai-slop` | Applies the engine's anti-slop writing rules to any deliverable. |
| `ai-marketing` | `brand-voice-ai-training` | Encodes a brand voice into AI instructions, examples and checks. |
| `business-development` | `biz-dev-credentials` | Assembles an agency credentials pack from verifiable proof. |
| `business-development` | `biz-dev-lawful-prospecting-outreach` | Builds lawful B2B prospecting: lists, consent, sequences and speed-to-lead. |
| `business-development` | `biz-dev-positioning` | Defines agency niche, positioning and differentiation. |
| `business-development` | `biz-dev-pricing-menu` | Builds a priced services menu with scope and packages. |
| `business-development` | `biz-dev-proposal` | Drafts client proposals and statements of work. |
| `business-development` | `eac-call-for-applications-campaign` | Donor-compliant call-for-applications campaigns across the East African Community. |
| `content-writing` | `blog-writer` | Writes publication-ready blog posts to the engine's standards. |
| `content-writing` | `caption-writer` | Writes platform-fit social captions with calls to action. |
| `content-writing` | `content-ideas` | Produces a prioritised set of content ideas by pillar and format. |
| `content-writing` | `direct-response-funnel-copy` | Writes direct-response funnel copy: offers, pages and follow-up. |
| `content-writing` | `email-copywriter` | Writes marketing emails and sequences. |
| `content-writing` | `premium-commercial-writing` | Writes high-value commercial copy for premium offers and audiences. |
| `content-writing` | `prompt-engineering-library` | Maintains a reusable, tested marketing prompt library. |
| `language` | `east-african-english` | Sets East African English conventions for local audiences. |
| `language` | `french-native-copy` | Writes native French social copy for francophone markets. |
| `language` | `language-standards` | Sets the engine-wide British English and language rules. |
| `language` | `swahili-native-copy` | Writes native Kiswahili social copy. |
| `meta-analytics-ops` | `measurement-tracking-plan` | Writes the privacy-safe tracking plan: events, UTM convention, Consent Mode v2, Conversions API, enhanced conversions and BigQuery export. |
| `meta-analytics-ops` | `meta-algorithm-guide` | Builds a platform-ranking reference from current evidence. |
| `meta-analytics-ops` | `meta-budget-planner` | Allocates a confirmed budget across channels, production, tools and contingency. |
| `meta-analytics-ops` | `meta-competitor-analysis` | Compares named competitors to find positioning and content gaps. |
| `meta-analytics-ops` | `meta-content-audit` | Reviews content history to decide what to keep, stop, test or improve. |
| `meta-analytics-ops` | `meta-content-repurposing` | Turns a proven asset into channel-appropriate derivatives. |
| `meta-analytics-ops` | `meta-reporting` | Produces monthly written performance reports from verified data. |
| `meta-analytics-ops` | `meta-roi-framework` | Calculates campaign or channel return from attributable value and cost. |
| `meta-analytics-ops` | `meta-sales-marketing-alignment` | Defines shared lifecycle stages, ownership and handover rules. |
| `meta-analytics-ops` | `meta-social-listening` | Sets up listening queries, evidence logs, cadence and escalation. |
| `meta-analytics-ops` | `meta-social-metrics-framework` | Selects business, funnel and operational metrics with owners. |
| `meta-analytics-ops` | `meta-testing-framework` | Designs controlled marketing experiments with decision rules. |
| `meta-analytics-ops` | `meta-tools-stack-evaluation` | Evaluates the marketing technology stack for fit and total cost. |
| `meta-utility` | `kaizen-improvement-system` | Audits and improves the engine or any deliverable it produces. |
| `meta-utility` | `skill-safety-audit` | Reviews skills for unsafe instructions before adoption or release. |
| `meta-utility` | `skill-writing` | Creates or upgrades skills under the canonical skill-writing standard. |
| `pipeline` | `01-client-brief` | Turns discovery answers into the full brief and one-page client card. |
| `pipeline` | `02-platform-audit` | Audits active social profiles and named competitors. |
| `pipeline` | `03-audience-personas` | Develops research-grounded audience personas. |
| `pipeline` | `04-brand-voice-intake` | Defines verbal and visual brand direction. |
| `pipeline` | `05-social-media-strategy` | Produces the master social-media strategy. |
| `pipeline` | `06-digital-marketing-strategy` | Integrates social, email, search, web, influencer and paid into one plan. |
| `pipeline` | `07-email-marketing-strategy` | Designs a permission-based email programme and lifecycle. |
| `pipeline` | `08-influencer-marketing-strategy` | Plans creator programmes with fit, due diligence, rights and measures. |
| `pipeline` | `09-campaign-strategy` | Plans one focused launch, offer, awareness or event campaign. |
| `pipeline` | `10-content-pillars` | Defines three to five audience-linked content pillars. |
| `pipeline` | `11-content-calendar` | Schedules approved pillars and campaigns over 90 days. |
| `pipeline` | `12-website-content-plan` | Plans 90 days of website and blog content (not the build). |
| `pipeline` | `13-campaign-brief` | Turns an approved campaign strategy into an executable brief. |
| `platforms` | `platform-facebook` | Facebook channel plan: setup, content, community and measurement. |
| `platforms` | `platform-google-business-profile` | Google Business Profile plan: setup, posts, reviews and measurement. |
| `platforms` | `platform-instagram` | Instagram channel plan: setup, content, community and measurement. |
| `platforms` | `platform-linkedin` | LinkedIn channel plan for personal and professional presence. |
| `platforms` | `platform-tiktok` | TikTok channel plan: setup, content, community and measurement. |
| `platforms` | `platform-whatsapp` | WhatsApp channel plan: setup, broadcasts, community and measurement. |
| `platforms` | `platform-x-twitter` | X (Twitter) channel plan: setup, content and measurement. |
| `platforms` | `platform-youtube` | YouTube channel plan: setup, content, community and measurement. |
| `playbooks` | `playbook-agency-operations` | Agency operations playbook: roles, workflow, controls and measures. |
| `playbooks` | `playbook-chatbot-strategy` | Chatbot strategy playbook: scope, flows, handover and measures. |
| `playbooks` | `playbook-client-retainer-management` | Playbook for running and renewing client retainers. |
| `playbooks` | `playbook-community-management` | Community management playbook: moderation, response and escalation. |
| `playbooks` | `playbook-content-production` | Content production playbook from brief to approved asset. |
| `playbooks` | `playbook-crisis-communications` | Crisis communications playbook: triage, holding lines and escalation. |
| `playbooks` | `playbook-daily-operations-routine` | Daily social-media operations routine and checklists. |
| `playbooks` | `playbook-marketing-automation` | Marketing automation playbook: triggers, flows and controls. |
| `playbooks` | `playbook-networking` | Professional networking playbook for relationship-led growth. |
| `playbooks` | `playbook-paid-social-advertising` | Paid social on Meta, TikTok and LinkedIn: audiences, budgets, tracking and optimisation. |
| `playbooks` | `playbook-post-click-strategy` | Post-click playbook: landing experience, follow-up and conversion. |
| `playbooks` | `playbook-pr-publicity` | Publicity playbook: angles, pitching and coverage tracking. |
| `playbooks` | `playbook-reputation-management` | Reputation management playbook: monitoring, response and recovery. |
| `playbooks` | `playbook-sms-whatsapp-marketing` | SMS and WhatsApp marketing playbook with opt-in controls. |
| `playbooks` | `playbook-social-media-policy` | Playbook for drafting an organisational social media policy. |
| `playbooks` | `playbook-social-selling` | Social selling playbook for relationship-led sales. |
| `playbooks` | `playbook-viral-content-design` | Playbook for designing shareable content with evidence limits. |
| `policies` | `policy-ai-content-ethics` | Drafts or reviews an organisational AI content ethics policy. |
| `sectors` | `healthcare` | Healthcare marketing: patient-safe content, trust and misinformation response. |
| `sectors` | `hospitality-hotel-restaurant` | Hospitality marketing for hotels, lodges, restaurants, venues and catering. |
| `seo-discovery` | `demand-forecasting` | Demand forecasts, stockout timing and reorder decisions from operational data. |
| `seo-discovery` | `seo-geo-optimisation` | Page-level SEO and generative-search citation readiness. |
| `strategy` | `brand-strategy-and-distinctive-assets` | Brand building: category entry points, mental and physical availability, distinctive-asset audits, brand/activation balance and brand tracking; includes online-shop differentiation. |
| `strategy` | `ecommerce-export-marketing-advisory` | Export-market selection, cross-border trust and CAC-bounded campaigns. |
| `strategy` | `marketing-foundations-stp-positioning` | Segmentation, targeting, positioning, marketing mix and value proposition. |
| `strategy` | `peso-integrated-strategy` | Coordinates paid, earned, shared and owned channels. |
| `strategy` | `social-commerce-strategy` | Catalogue, WhatsApp ordering, Mobile Money and fulfilment content. |
| `strategy` | `strategy-b2b-customer-community` | Retention-first B2B account grading, contact plans and at-risk alerts. |
| `strategy` | `strategy-channel-architecture` | Platform roles, audience flows, hub-and-spoke routing and effort. |
| `strategy` | `strategy-creator-monetisation` | Creator revenue options, rate cards, partnerships and products. |
| `strategy` | `strategy-csr-purpose-communications` | CSR, community-impact and purpose communication. |
| `strategy` | `strategy-customer-value-journey` | Full-funnel content from awareness to advocacy. |
| `strategy` | `strategy-ewom-reviews` | Review generation, referrals and electronic word of mouth. |
| `strategy` | `strategy-experiential-marketing` | Live and hybrid experiences: launches, activations and pop-ups. |
| `strategy` | `strategy-personal-brand` | Individual positioning, authority, content and monetisation. |
| `strategy` | `strategy-video-content` | Cross-platform organic video formats, hooks, series and scripts. |
| `strategy` | `traction-channel-bullseye` | Chooses acquisition channels to test and fund from nineteen traction channels. |
| `training` | `training-ai-foundations` | Beginner AI literacy training for marketing teams. |
| `training` | `training-client-team` | Two-hour social-media handover workshop and workbook. |
| `training` | `training-smartphone-video-production` | Hands-on smartphone video shooting, sound, light and editing. |
| `training` | `training-social-media-fundamentals` | Beginner social-media concepts, safety and measurement. |

### Retired skill routes

Never run an `ALIAS.md`. Use the active owner below; the retired skill's unique content lives in the owner's `references/`. 83 routes, checked by `scripts/check_skill_aliases.py`.

| Retired skill (inactive `ALIAS.md`) | Active owner |
|---|---|
| `ai-marketing/ai-agentic-marketing-workflows` | `playbooks/playbook-marketing-automation` |
| `ai-marketing/ai-avatar-personalised-video` | `strategy/strategy-video-content` |
| `ai-marketing/ai-content-humaniser` | `ai-marketing/anti-ai-slop` |
| `ai-marketing/ai-content-recycling-pipeline` | `meta-analytics-ops/meta-content-repurposing` |
| `ai-marketing/ai-cultural-bias-audit` | `policies/policy-ai-content-ethics` |
| `ai-marketing/ai-data-foundation-audit` | `ai-marketing/ai-readiness-diagnostic` |
| `ai-marketing/ai-data-foundation-plan` | `ai-marketing/ai-readiness-diagnostic` |
| `ai-marketing/ai-growth-systems-design` | `ai-marketing/ai-use-case-mapping` |
| `ai-marketing/ai-influencer-strategy` | `pipeline/08-influencer-marketing-strategy` |
| `ai-marketing/ai-marketing-canvas-assessment` | `ai-marketing/ai-readiness-diagnostic` |
| `ai-marketing/ai-predictive-analytics-social` | `ai-marketing/ai-use-case-mapping` |
| `ai-marketing/ai-rag-brand-knowledge-base` | `ai-marketing/brand-voice-ai-training` |
| `ai-marketing/ai-strategy-co-thinker` | `ai-marketing/ai-use-case-mapping` |
| `ai-marketing/ai-synthetic-personas` | `pipeline/03-audience-personas` |
| `ai-marketing/ai-vendor-evaluation` | `meta-analytics-ops/meta-tools-stack-evaluation` |
| `ai-marketing/ai-whatsapp-chatbot-design` | `playbooks/playbook-chatbot-strategy` |
| `business-development/biz-dev-beyond-agency-offer` | `business-development/biz-dev-pricing-menu` |
| `business-development/biz-dev-case-study` | `business-development/biz-dev-credentials` |
| `business-development/biz-dev-practitioner-positioning` | `business-development/biz-dev-positioning` |
| `business-development/biz-dev-reactivation-campaign` | `pipeline/07-email-marketing-strategy` |
| `business-development/biz-dev-social-media-audit-offer` | `pipeline/02-platform-audit` |
| `business-development/biz-dev-video-outreach` | `business-development/biz-dev-lawful-prospecting-outreach` |
| `content-writing` (former category standards file) | `content-writing/premium-commercial-writing` |
| `content-writing/blog-idea-generator` | `content-writing/content-ideas` |
| `content-writing/content-whitepaper-ebook` | `content-writing/blog-writer` |
| `content-writing/copywriting-brochure` | `content-writing/premium-commercial-writing` |
| `content-writing/direct-mail-writer` | `content-writing/direct-response-funnel-copy` |
| `content-writing/hashtag-strategy` | `content-writing/caption-writer` |
| `content-writing/image-prompt-engineer` | `content-writing/prompt-engineering-library` |
| `content-writing/prompt-library-image-audio-video` | `content-writing/prompt-engineering-library` |
| `frameworks/framework-community-trust` | `playbooks/playbook-community-management` |
| `frameworks/framework-digital-transparency` | `strategy/strategy-csr-purpose-communications` |
| `meta-analytics-ops/meta-ai-tools-audit` | `meta-analytics-ops/meta-tools-stack-evaluation` |
| `meta-analytics-ops/meta-analytics-privacy` | `meta-analytics-ops/measurement-tracking-plan` |
| `meta-analytics-ops/meta-cohort-analysis` | `meta-analytics-ops/meta-roi-framework` |
| `meta-analytics-ops/meta-dashboard-design` | `meta-analytics-ops/meta-reporting` |
| `meta-analytics-ops/meta-evergreen-content-strategy` | `meta-analytics-ops/meta-content-repurposing` |
| `meta-analytics-ops/meta-lead-scoring` | `meta-analytics-ops/meta-sales-marketing-alignment` |
| `meta-analytics-ops/meta-posting-optimisation` | `meta-analytics-ops/meta-algorithm-guide` |
| `meta-analytics-ops/meta-revenue-planning` | `meta-analytics-ops/meta-budget-planner` |
| `meta-analytics-ops/meta-sentiment-analysis` | `meta-analytics-ops/meta-social-listening` |
| `meta-analytics-ops/meta-social-marketing-mix-review` | `meta-analytics-ops/meta-reporting` |
| `meta-analytics-ops/meta-social-media-roi-business-case` | `meta-analytics-ops/meta-roi-framework` |
| `meta-analytics-ops/meta-social-proof-system` | `strategy/strategy-ewom-reviews` |
| `meta-analytics-ops/meta-utm-tracking` | `meta-analytics-ops/measurement-tracking-plan` |
| `pipeline/00-client-intake` | `pipeline/01-client-brief` |
| `platforms/platform-instagram-growth` | `platforms/platform-instagram` |
| `platforms/platform-instagram-visual-system` | `platforms/platform-instagram` |
| `platforms/platform-linkedin-company-pages` | `platforms/platform-linkedin` |
| `platforms/platform-podcast-strategy` | `strategy/strategy-video-content` |
| `playbooks/playbook-ai-automation-workflow` | `playbooks/playbook-marketing-automation` |
| `playbooks/playbook-ai-content-workflow` | `playbooks/playbook-content-production` |
| `playbooks/playbook-audacious-content` | `playbooks/playbook-viral-content-design` |
| `playbooks/playbook-email-funnel` | `pipeline/07-email-marketing-strategy` |
| `playbooks/playbook-employee-advocacy` | `playbooks/playbook-social-selling` |
| `playbooks/playbook-geo-newsjacking` | `playbooks/playbook-pr-publicity` |
| `playbooks/playbook-instagram-dm-sales` | `strategy/social-commerce-strategy` |
| `playbooks/playbook-lead-magnet-system` | `pipeline/07-email-marketing-strategy` |
| `playbooks/playbook-location-based-marketing` | `platforms/platform-google-business-profile` |
| `playbooks/playbook-pr-media-integration` | `playbooks/playbook-pr-publicity` |
| `playbooks/playbook-profile-optimisation` | `pipeline/02-platform-audit` |
| `playbooks/playbook-question-engine` | `pipeline/12-website-content-plan` |
| `playbooks/playbook-sentiment-listening` | `meta-analytics-ops/meta-social-listening` |
| `playbooks/playbook-social-customer-service` | `playbooks/playbook-community-management` |
| `playbooks/playbook-social-media-brand-style-guide` | `pipeline/04-brand-voice-intake` |
| `playbooks/playbook-social-media-contests` | `pipeline/09-campaign-strategy` |
| `playbooks/playbook-social-media-governance` | `playbooks/playbook-social-media-policy` |
| `playbooks/playbook-ugc-strategy` | `pipeline/08-influencer-marketing-strategy` |
| `playbooks/playbook-webinars-live-events` | `strategy/strategy-experiential-marketing` |
| `playbooks/playbook-whatsapp-business` | `platforms/platform-whatsapp` |
| `playbooks/playbook-white-label-partnerships` | `playbooks/playbook-agency-operations` |
| `playbooks/playbook-word-of-mouth-strategy` | `strategy/strategy-ewom-reviews` |
| `policies/policy-ai-ip-and-copyright` | `policies/policy-ai-content-ethics` |
| `strategy/ecommerce-brand-differentiation` | `strategy/brand-strategy-and-distinctive-assets` |
| `strategy/ecommerce-conversion-optimisation` | `playbooks/playbook-post-click-strategy` |
| `strategy/owned-media-strategy` | `strategy/peso-integrated-strategy` |
| `strategy/premium-social-selling` | `playbooks/playbook-social-selling` |
| `strategy/strategy-micro-communities` | `playbooks/playbook-community-management` |
| `strategy/strategy-multigenerational-digital` | `pipeline/03-audience-personas` |
| `strategy/strategy-organic-paid-hybrid` | `advertising/ad-testing-and-scaling` |
| `strategy/strategy-pdca-workflow-design` | `playbooks/playbook-daily-operations-routine` |
| `training/training-ai-prompt-writing` | `training/training-ai-foundations` |
| `training/training-diy-content` | `training/training-client-team` |

## Approval boundaries

- Research, planning, drafting, auditing and reporting run without special permission.
- Ad spend, live ad-account or platform changes, publishing, messaging and outreach to real people, and personal-data processing need explicit client authority; without it the engine returns a draft marked for approval.
- Changing legal, platform or market claims must cite a current record in `docs/source-registers/source-register.json`; a stale or unavailable source makes the check `not assessed`.
- Visual execution routes to the design engine (`chwezi-design-engine`, held in a folder named `design-system-skills` on some machines); website builds route to `website-skills`.

## Quality and improvement

The evidence for the October 2026 Kaizen cycles is in [`docs/kaizen/2026-10-engine-kaizen/`](docs/kaizen/2026-10-engine-kaizen/) (pass 1, 29 October 2026) and [`docs/kaizen/2026-10-engine-kaizen-pass-2/`](docs/kaizen/2026-10-engine-kaizen-pass-2/) (pass 2, 31 October 2026). Each folder holds the same records: scope and evidence, baseline scorecard, backlog, currentness, experiment log, validation record, final report and next-cycle handoff, with its `logs/` and `tasks/`. The [documentation index](docs/README.md) lists the earlier dated records. Every Kaizen cycle starts from the currentness gate of the Digital Research engine (`digital-research-skills`; some machines still hold it in a folder named `chwezi-research-engine`).

**Latest published score** (pass 2 [final report](docs/kaizen/2026-10-engine-kaizen-pass-2/05-final-report.md)): raw 60.0 and published, capped at `min(raw, 65)`, 60.0. The cap did not bind, and the 95/100 target was not reached. Pass 1 closed at 58.5 and the pass 2 baseline was 58.2. The scores are self-assessed from named measures; no independent re-grade and no behavioural (Tier 3) model run took place. The changes behind these scores are listed under [What the October 2026 kaizen improved](#what-the-october-2026-kaizen-improved).

**Open findings that matter to a user**

- **The source-freshness gate exits 1.** Five quarantined records are overdue since 2026-10-11 and stay `NOT_ASSESSED` until their primary text is read: `UG-DPPR-2021` (Uganda Data Protection and Privacy Regulations 2021), `UG-COPYRIGHT-2026` (Uganda Copyright and Neighbouring Rights (Amendment) Act 2026), `KE-DP-GENERAL-2021` (Kenya Data Protection (General) Regulations 2021), `RW-DPP-2021` (Rwanda Law No. 058/2021) and `ITU-INTERNET-USAGE` (no skill uses it). Do not release a claim that depends on any of them, including the Ugandan and Kenyan direct-marketing rows of the [legal and market release gate](docs/quality-gates/legal-market-release-gate.md). The CI workflow runs this check, so that job fails while the gate exits 1. Details: [03-currentness.md](docs/kaizen/2026-10-engine-kaizen-pass-2/03-currentness.md).
- **Registered legal statuses are narrow.** `UG-DPPA-2019`, `UG-UCC-ADS-2019`, `TZ-PDPA` and `TZ-PDPR-2023` are `partial`: they record what was read, not that a campaign or post complies. Amendments to the Ugandan Act after December 2023 and any UCC revision were not searched.
- **Platform specification values are unread.** The platform-specification gate in `validate_media_plan_provenance.py` proves the state of a register record, not the value a platform page shows. Open the live page at each build date.
- **Routing is lexical and thinly covered.** At the pass 2 close, 9 of 112 skills had three positive and two owned-negative fixtures; the target is 56.
- **Not yet done:** a four-week launch calendar variant, a tie-break for overlapping media-class thresholds, LinkedIn page-field limits from a LinkedIn Help Centre source, and a broader claim audit. They are listed in [06-next-cycle.md](docs/kaizen/2026-10-engine-kaizen-pass-2/06-next-cycle.md).

**Date-triggered gates.** `check_source_freshness.py` fails from the day after a record's `next_review`. It already fails today because of the five quarantines above. If no record is re-verified, these further records become overdue (counts are records overdue and not quarantined, measured with `--as-of`):

| Run with `--as-of` | Overdue, not quarantined (cumulative) | Newly overdue since the row above |
|---|---:|---|
| 2026-11-08 | 1 | `BING-AI-PERFORMANCE-2026` |
| 2026-11-13 | 2 | `UG-PDPO-ORG` |
| 2026-11-29 | 20 | 18 records due 2026-11-18 to 2026-11-28, 14 of them on 2026-11-28 (including the three Computer Misuse records) |
| 2026-12-01 | 22 | `META-AD-STANDARDS` and `UG-FACEBOOK-ACCESS-2026` (due 2026-11-30) |
| 2026-12-30 | 90 | 68 records due 2026-12-07 to 2026-12-29, 44 of them on 2026-12-29 |
| 2027-01-30 | 95 | `UG-DPPA-2019`, `UG-UCC-ADS-2019`, `TZ-PDPA` and `TZ-PDPR-2023` (due 2027-01-29), plus one due 2027-01-09 |
| 2027-03-30 | 149 | 54 records due 2027-03-23 to 2027-03-29, 44 of them on 2027-03-29 |
| 2027-09-30 | 174 | The last 25 records (due 2027-09-29); every record that is not quarantined is now overdue |

`validate_media_plan_provenance.py` fails the same way for any plan that cites a register record once that record is overdue; the pass 2 sample plan fails with `--as-of 2027-01-01` because `META-AD-STANDARDS` is overdue by then. The test suite pins its dates and is not date-triggered. The proposed next audit is 2026-11-30, or earlier once the five quarantined records are read.

### What the October 2026 kaizen improved

Two Kaizen cycles ran on this engine, on 29 October (pass 1) and 31 October 2026 (pass 2), followed by a documentation wave. Every commit below is on `main` and was checked with `git show --stat`. Neither cycle reverted a kept change. The sources are the pass 1 [final report](docs/kaizen/2026-10-engine-kaizen/05-final-report.md) and [experiment log](docs/kaizen/2026-10-engine-kaizen/03-experiment-log.md), and the pass 2 [final report](docs/kaizen/2026-10-engine-kaizen-pass-2/05-final-report.md), [backlog](docs/kaizen/2026-10-engine-kaizen-pass-2/02-improvement-backlog.md), [experiment log](docs/kaizen/2026-10-engine-kaizen-pass-2/03-experiment-log.md) and [validation record](docs/kaizen/2026-10-engine-kaizen-pass-2/04-validation-record.md). The items rest on commands and counts, not on the self-assessed scores. What did not change: the source-freshness gate exits 1 before and after both cycles, the 95/100 target was not reached, and no paid or behavioural model run took place.

**Measured before and after.** "Re-measured" means the command was run on 2026-10-31 on a `git archive` snapshot of the commit named (or against the register held at that commit). "Evidence" means the figure is copied from the file named, because a score cannot be re-measured.

| Measure | Pass 1 (29 Oct) | Pass 2 (31 Oct) | Basis |
|---|---|---|---|
| Raw score, self-assessed | 58.5 to 58.5 | 58.2 to 60.0 | Evidence: [pass 1 scorecard](docs/kaizen/2026-10-engine-kaizen/01-baseline-scorecard.md), [pass 2 final report](docs/kaizen/2026-10-engine-kaizen-pass-2/05-final-report.md). The pass 2 baseline was lower than the pass 1 close because three dimensions lost a point for defects that were newly measured |
| Published score, `min(raw, 65)` | 58.5 to 58.5 | 58.2 to 60.0 | Evidence, same files. The cap did not bind at any point |
| Source-freshness findings (gate exits 1 at every point) | 23 to 10 | 11 to 5 | Re-measured: current `check_source_freshness.py` against the registers at `3664c85^` and `3664c85` (`--as-of 2026-10-29`) and at `f5e1ab1` and `HEAD` (`--as-of 2026-10-31`) |
| Routing fixtures, all passing, top three 1.000 | 392 to 396 | 396 to 400 | Re-measured: `routing_smoke_test.py --lint-fixtures` on snapshots of `750982a`, `891bb43`, `f5e1ab1` and the current tree |
| Lexical precision at 1 | 373/392 to 377/396 | 377/396 to 381/400 | Same runs; 95.2% each time. A lexical proxy, not live routing |
| Owned negatives, all passing | 121 to 123 | 123 to 125 | Same runs |
| Skills with three positives and two owned negatives (of 112; target 56) | 4 to 7 | 7 to 9 | Re-measured with `docs/kaizen/consolidation-2026-09-29/evidence/S13/measure_routing.py` on the same snapshots |
| Tests run by `unittest discover`, all passing | 70 to 92 | 92 to 116 | Re-measured on the same snapshots |
| Host-specific path lines in active content and router blocks | not measured | 5 to 0 | Pass 2 baseline from [evidence](docs/kaizen/2026-10-engine-kaizen-pass-2/01-baseline-scorecard.md), confirmed by `grep` at `ecef6e1^` (4 lines in `AGENTS.md`, 1 in the skill-writing skill); now 0 by `grep` and `check_machine_paths.py`. The step to 3 was `ecef6e1`, the step to 0 was the documentation wave (`830f154`) |

**Correctness and safety fixes, most serious first**

1. **The source gate passed quarantined sources** (`a80bc2e`, pass 1). The first quarantine code (`3664c85`) reported a quarantined record only when it was also overdue, so a quarantined record with a future review date passed. Independent acceptance review found it. Every `quarantined: true` record now blocks. Checked with a regression test, and again for this section on a scratch copy of the register (ten quarantined records, review dates set to 2027-12-31, `--as-of 2026-10-29`): the checker from `a80bc2e^` exited 0 and the one from `a80bc2e` exited 1. The scratch register was not committed.
2. **The outreach checklist overstated a statute** (`d5c8a4c`, pass 2). It said that processing personal data without prior consent (s.7, Uganda Data Protection and Privacy Act 2019) "is an offence". The Act text, read on 2026-10-31 from the ULII PDF, states the consent rule at s.7 with no penalty; the offences are ss.35 to 37 and complaints go to the Authority under ss.31 to 33. The sentence is corrected and `tests/test_legal_claim_guard.py` (4 tests) guards it. The guard pattern matches the file at `d5c8a4c^` and does not match the current file. Only this one claim is guarded, and Act amendments after December 2023 were not read.
3. **A symlinked `.claude-plugin` directory could resolve manifest files outside the checkout** (`15e73a8`, pass 1). The package check now refuses it before reading. Checked by an escape-path regression test; `tests/test_package_integrity.py` runs 11 tests and all pass.
4. **A malformed quarantine flag was treated as absent** (`b42b6ea`, pass 1). A non-boolean `quarantined` value now fails closed. Checked by `test_malformed_quarantine_flag_fails_closed`.
5. **Nothing stopped a quarantine being cleared without evidence** (`5aed7e2`, pass 2). A release now needs a `scope`, a `release_basis`, a `partial` or `verified` status and a `verified_on` date equal to the release date. Three of the four new tests failed before the change and all 11 in `tests/test_source_freshness_negative.py` pass after it ([log](docs/kaizen/2026-10-engine-kaizen-pass-2/logs/test-released-quarantine.txt)); the 11 pass again now.
6. **The media-planning workflow numbered two steps "6."** (`a4ef219`, pass 1). Steps now run 1 to 10, with a regression test in `tests/test_media_plan_provenance.py`.

**Source currentness**

7. **23 overdue records blocked the gate without separating reviewed from unreviewed ones** (`3664c85`, with `40d6cd7`, pass 1). Of 23 overdue records, 13 were re-scoped after the official page was opened, each `partial` with a stated narrow scope. The other 10 were quarantined as `NOT_ASSESSED` instead of having their dates moved. Findings fell from 23 to 10 (re-measured above). A quarantine is a block, not clearance; `40d6cd7` aligned the audit-date test to that. Detail: [pass 1 currentness record](docs/kaizen/2026-10-engine-kaizen/03-currentness.md).
8. **Primary text read for the records pass 1 could not open** (`b6dc4e0`, pass 2). Findings fell from 11 to 5. Five quarantines were released after the text was read (`UG-DPPA-2019`, `UG-UCC-ADS-2019`, `TZ-PDPA`, `TZ-PDPR-2023`, `META-AD-STANDARDS`), one record was re-checked (`UG-FACEBOOK-ACCESS-2026`) and three dead or mismatched URLs were corrected. Every release is `partial` with a recorded scope, and the Meta record supports page structure only. The commit subject says "six sources"; the correct count is five released and one re-checked. Sites that blocked automated access (ULII HTML pages, ITU DataHub, Kenya Law) were not worked around; five records stay quarantined because their primary text has not been read. Detail: [pass 2 currentness record](docs/kaizen/2026-10-engine-kaizen-pass-2/03-currentness.md).

**Gaps filled in skills and references**

9. **The README cited the UCC Advertising Standards 2019 but no skill carried a check** (`a86f456`, pass 2). New reference `skills/content-writing/references/uganda-advertising-standards-check.md`, linked from the direct-marketing ethics filter, the influencer term-sheet reference and the legal and market release gate. It records that no clause names the internet, social media or influencers, so application to social posts is `NOT_ASSESSED`. From the evidence file: 16 of 16 quoted phrases were found in the extracted primary text and seven digital-media search terms were found 0 times ([log](docs/kaizen/2026-10-engine-kaizen-pass-2/logs/clause-screen-text-checks.txt)). That check was not re-run here, because the extracted text was kept outside the repository.
10. **The crisis playbook had no route for a service outage with a possible data question, and no skill held the Act's s.23 notification duty** (`14ab9be`, pass 2). New reference `skills/playbooks/playbook-crisis-communications/references/service-outage-and-data-incident-communications.md` (74 lines) with a decision row in the skill. It states s.23(1) to (5) from primary text and bars refund or compensation wording that the contract or client policy does not supply. `validate_skill_engine.py` still reports 112 of 112 compliant; the new text was shortened to meet the validator's description limit rather than the limit being raised.
11. **The social anti-slop overlay identifiers (ME1 to ME7, AS1 to AS7) sat only in a child reference**, where the shared identifier scan missed them (`ecc151a`, pass 1). They are now exposed at the entry skill and `tests/test_anti_slop_overlay.py` guards the crosswalk. This proves the checks can be found, not that a model applies them.

**New checks and tests**

12. **No size or identity check on the package** (`177e2a0`, pass 1). `scripts/check_package_integrity.py` enforces a hard 5,000-entry ceiling on the full checkout and the package tree, fails closed on an incomplete walk, and checks the plugin name, version and path set. It is wired into the CI workflow. The script is absent from a snapshot of `750982a`; it now exits 0 with 1,431 and 971 entries (the checkout count includes `.git`).
13. **Media-plan numbers could appear without an origin** (`5a2f371`, pass 1). `scripts/validate_media_plan_provenance.py` requires an origin (`observed`, `client_input` or `synthetic_assumption`) and a source for every numeric input, and the plan example now carries them. Six tests at that commit (seven after `a4ef219`) cover the refusal paths. Figures remain synthetic assumptions, not forecasts.
14. **Platform specifications had no source-state check** (`5b46d84`, pass 2). Optional `platform_specs` entries are refused as `verified` when their register record is quarantined, overdue, absent or not verified. Ten of the 11 new tests errored before the change; `tests/test_media_plan_provenance.py` now passes 18 of 18. Re-run for this section: the honest sample plan exits 0, the negative control exits 1 with two findings, and the same sample with `--as-of 2027-01-01` exits 1 because `META-AD-STANDARDS` is overdue by then. The gate proves the state of a register record, not the value on a platform page.
15. **No check for host-specific paths** (`ecef6e1`, pass 2). `scripts/check_machine_paths.py` and 5 tests (all pass) fail on a host path in active content. The live checkout failed before the fix and passed after; two engine-local paths were removed (see the table for the figures).

**Routing**

16. **Fixture coverage was thin and tied to few skills** (`f2fd463`, pass 1; `14ab9be` and `7940e14`, pass 2). Fixtures rose from 392 to 400, owned negatives from 121 to 125, and skills meeting the three-positive, two-negative rule from 4 to 9 of 112 (figures in the table). Precision at 1 stayed at 95.2%. In pass 2 the first owned negative for outreach failed because its prompt was ambiguous, so the prompt was replaced rather than the router tuned. All figures are lexical, and 9 of 112 is far from the target of 56.

**Documentation and portability**

17. **Commands and results were Windows-only or missing** (`2abddc7`, `797a0ed`, `948d043`, `57067dd`, `3075062`, `830f154`, `5bfa956`, `6813015`, `b50403e`, documentation wave). The README listed five checks and CONTRIBUTING three, as backslash PowerShell commands with no results. The README now lists thirteen commands with a table of what each checks and its measured result, written for Linux (`python3`, and `bash install.sh` because the file is not executable). `AGENTS.md` and `rules/common/core.md` now use the current name `digital-research-skills`; three router sentences in `AGENTS.md` no longer name workstation paths; [`docs/README.md`](docs/README.md) separates controlling documents from dated records; and [`CHANGELOG.md`](CHANGELOG.md) records the history with corrected counts. The commands were run on Fedora 44 (Python 3.14, Node 22) and the exit codes are in [Validation](#validation). Not run: `install.ps1` (no PowerShell here) and a non-dry-run `install.sh`. Follow-ups that need skill or script changes are in [07-docs-followups.md](docs/kaizen/2026-10-engine-kaizen-pass-2/07-docs-followups.md).

## Sources and references

Full lists of books, repositories, standards, source-register sources and websites are in [docs/references.md](docs/references.md). They are citations only: no book content is stored in this repository.
