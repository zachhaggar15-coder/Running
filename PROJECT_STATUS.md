# Project status

Updated: 6 November 2026 (Europe/London)

## Agreed product direction from the brief

Build an independent, privacy-conscious UK road, trail and ultra race reference that helps runners find, investigate and compare events. Confirmed, edition-specific facts must be linked to their sources. Missing information must stay unknown. No fictional records, copied descriptions, advertising or paid features. Target 200–300 meaningful current profiles only if sourcing and verification make that responsible.

## Decisions made

- The owner approved the Stage A recommendation on 4 November 2026, amended to a 30-race sourcing pilot and preliminary Stage B work. Substantial application development waits until pilot results are reviewed.
- Publishing project files to this GitHub repository is authorised by the user's request. Public website deployment is a later, separate decision.
- No brand, domain, hosting plan, data feed, licence or public launch has been approved.
- The 200–300-profile launch target remains unchanged. No paid services, bulk imports, public deployment or domain purchase are authorised.
- Normal-operation owner involvement of no more than 1–2 hours/month is a design target to test, not an assumption.
- Strategic direction revised on 4 November 2026: differentiate through race suitability and decision-making, not directory size. The working proposition is “Find the race that suits you.”
- The 200–300 profile ambition remains a long-term expansion target, but is no longer a prerequisite for testing a smaller first release. A first public release size must be agreed before deployment; the current working range is 20–40 quality profiles.
- Substantial application development is now authorised. Public deployment, domain purchase, paid services and material legal uncertainty still require approval.

## Completed

- Initial competitor, search-intent, data-source, rights, SEO and infrastructure review in [Stage A](docs/STAGE_A_FEASIBILITY.md).
- Updated [source compliance register](docs/SOURCE_COMPLIANCE_REGISTER.md) with pilot-specific restrictions and holds.
- [30-race sourcing audit](research/PILOT_REPORT.md) with [row-level evidence](research/pilot_30.tsv) across all four nations and a 13-record same-day recheck.
- [50-query SEO audit](research/SEO_REPORT.md) with [query-level results](research/search_queries_50.tsv), direct Google spot checks and Google Trends comparisons. Absolute UK search volumes were unavailable.
- Three [original preliminary profile drafts](research/profile_drafts.md) and [preliminary Stage B concepts](research/STAGE_B_PRELIMINARY.md). No substantial application development or public deployment.
- Created a dependency-free [Race Fieldnotes prototype](app/index.html) with a suitability finder, searchable directory and three-race comparison using the 15 provisional-minimum pilot records.

## Verification performed

- Checked live competitor and official organiser pages, UK IPO database-rights guidance, Google Search Central guidance, and current Vercel/Supabase pricing pages on 3 November 2026.
- Checked that this GitHub repository exists and was empty at the start of this checkpoint.
- Audited 30 official-source races on 4 November 2026: 15 meet a provisional factual minimum and 11 are detailed-profile candidates. Cut-offs were found for 10/30, numerical elevation for 6/30, public transport for 6/30, parking for 6/30 and facilities for 15/30.
- Rechecked 13 records the same day: no race fact changed; two pages had unrelated navigation/widget changes. This cannot establish longer-term maintenance reliability.
- Inspected 50 specific search-service results, two direct Google results and three GB Google Trends comparisons. No credible absolute search-volume data was accessible, and ranking/traffic forecasts are not justified.
- Per-event mean/median creation time and monthly human review minutes remain **unmeasured**, because initial sourcing was batched and no permitted recurring update pipeline exists. The feasibility report gives labelled planning scenarios only.

## Open issues and risks

1. Newer competitors already offer course data, comparisons and even verification cues. Differentiation must be tested, not assumed.
2. No blanket licence or permitted bulk-import source has been identified. Organiser pages support limited factual, individually reviewed research; automated reuse needs source-by-source assessment.
3. Achieving 200–300 useful profiles, especially with current logistical details, has not been demonstrated. Northern Ireland yielded only one minimum candidate and no detailed candidate from seven.
4. Search evidence remains qualitative; no traffic forecast is justified. Official organisers dominate event-name and many logistics/cut-off results, while specialist directories compete for discovery.
5. Production costs and Vercel Hobby eligibility depend on the final use and plan terms.
6. The 1–2-hour/month owner workload target is not established. Even an optimistic hypothetical 5% exception rate at 300 records implies about 2.5 hours/month including 30 minutes of oversight.

## Approved pilot work plan

1. Research 30 representative official-source races across all four nations, terrains, distances and organiser sizes, without selecting only well-documented events.
2. Measure current-edition and historical fact coverage, practical fields, research time, human intervention, source limitations and whether each race meets minimum and detailed-profile standards.
3. Recheck a representative subset and measure source changes, edition ambiguity and manual maintenance effort.
4. Inspect 40–50 specific UK race queries and competing results. Use credible volume data if accessible; otherwise label it unavailable and report qualitative evidence and any usable Google Trends evidence.
5. Estimate creation effort for 200–300 profiles and monthly maintenance at 200, 300 and 1,000, with the 1–2 hour owner target explicitly assessed.
6. Preliminary brand concepts, relational model and wireframes are documented; none are selected or implemented.
7. **Superseded by the revised direction:** proceed with a controlled product build while targeted data and legal questions are resolved. The first slice is a private/local review build; no public deployment has occurred.

## Outstanding owner decisions

- **Completed autonomously:** source/SEO audit, same-day recheck, source compliance register, preliminary content and Stage B sketches. No owner action was needed for these.
- **Approval required before the next major commitment:** whether to proceed with substantial application development after reviewing these results; any relaxation of the 200–300 target; use of a materially uncertain source; paid plans, domain purchase or public deployment. The proposed narrow validation work stays within the pilot approval.
- **External-service action genuinely requiring the owner:** none currently identified. Source permissions may later require organiser contact or qualified legal advice; ChatGPT Work should prepare and consolidate any such requests first.

## Implementation progress

- Stage 1 foundation: prototype homepage, finder, directory, filters, source-linked cards and comparison table implemented in `app/`.
- Initial data: 15 pilot records meeting the provisional factual minimum are included; unknown elevation, cut-off and travel values remain labelled.
- Expansion slice: profile detail overlays now show verified fields, source links and unknowns; finder results include objective-specific context; directory cards expose profile inspection and comparison state.
- Catalogue expansion: 20 static profile routes are generated from a structured JSON record model, including five newly researched official-organiser candidates. New pages are marked for review until source and edition checks are complete.
- The interactive directory and finder now include all 20 catalogue candidates and link each card to its crawlable profile route.
- Added six curated decision guides covering flat half marathons, first half marathons, trail ultras with cut-offs, travel information, Welsh trail races and Northern Ireland coverage. These guides link to profiles and state their evidence limits.
- SEO foundation: profile pages include canonical URLs and Event JSON-LD; `app/sitemap.xml` and `app/robots.txt` are included.
- Operations: maintenance states and a review queue are documented in [MAINTENANCE_WORKFLOW.md](research/MAINTENANCE_WORKFLOW.md).
- User journey P1: added an anonymous session shortlist, save/remove actions, comparison removal controls and plain-language comparison conclusions.
- Search UX: added a visible hero search, rebound directory search listeners to the active renderer, and increased colour contrast across controls, cards and backgrounds.
- Directory UX: added an explicit Search button beside the directory query field and date filtering. Every catalogue race now displays either a confirmed date or an explicit date-to-confirm state; no date is inferred.
- Profile redesign: rebuilt all 20 profile pages from the live catalogue data with clean UTF-8 output, terrain-specific original imagery, practical fact grids, suitability explanations, verification checklists, source panels and responsive layouts.
- Race-specific imagery: replaced the three repeated terrain headers with 20 unique, compressed editorial illustrations tied to each race location or nearby town. Every profile now includes descriptive alternative text, an explicit illustration disclaimer, a location caption and an image URL in both the structured catalogue and Event JSON-LD.
- Stage 2–5: search refinement, profile routes, formal data model, technical SEO, accessibility and browser testing remain in progress.
- Deployment: not deployed. The repository is ready for the owner to connect to Vercel; no hosting configuration or paid service was created by this work.
