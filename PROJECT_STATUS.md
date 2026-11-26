# Project status

Updated: 26 November 2026 (Europe/London)

## 26 November 2026: profile planning and complete race map

All 400 profiles now link to their own map pin and show a race-specific planning note: location confidence, edition timing, and up to four unanswered practical questions selected from the record's missing fields. The map offers search and nation/surface filters; every pin opens a race profile. Organizer directions supply 255 coordinates. The remaining 145 are clearly marked approximate town, venue-area, or route-area pins, so runners should confirm the actual start in final instructions. The homepage and race directory link to the map, and the sitemap includes it. The site generator now includes these improvements on each rebuild.

## 25 November 2026: 400-profile expansion

The working site now contains 400 unique source-linked profiles, including 200 additions from RunThrough, Wild Deer Events and Ultra Challenge pages. The organiser event pages were reviewed for dates, formats, routes and practical decisions. All 120 new RunThrough source pages returned HTTP 200 during the final audit; the remaining new source URLs also returned HTTP 200 when checked. Distinct editions of recurring races are listed separately, with their own date and organiser URL. Unknown details remain visible rather than inferred. The directory, catalogue, illustrations and sitemap have been rebuilt for the larger set. Older dated notes below describe earlier site states.

## Historical content checkpoint, 24 November 2026

- The local site now builds 200 distinct race profiles from 36 original records and 164 expansion records. All 200 have unique slugs and official organiser URLs; the generated directory and sitemap have been rebuilt.
- New expansion entries include practical, event-specific details such as start waves, course surface or laps, cut-offs, age rules, transport, parking and water provision when the organiser publishes them. Material contradictions in organiser pages are called out for a final-guide check.
- Two records for the same Hillsborough Castle event, two for the same Everton 10K, and a second Hampton Court half-marathon record were removed during duplicate review. The source URLs are now unique across the 200 records.
- The older dated checkpoints below describe the site at those earlier times; their 100-race counts are historical.

## Content quality update, 16 November 2026

- Refreshed 18 of the 20 thinner legacy profiles against current official organiser pages. Added edition dates where confirmed, course and start details, cut-offs, facilities, transport constraints and eligibility rules where available. Each refreshed page links to its supporting organiser detail page and shows the 16 November review date.
- The 80 newer profiles retain their previously researched practical sections. All 100 profiles are regenerated from the same structured data, with missing values labelled rather than inferred. The new review data is kept in `app/data/verified-updates.json` so it can be rechecked without editing generated HTML.
- Great North Run and Great South 5K were held from this refresh because the source compliance register marks Great Run website content as restricted for reuse. Their existing listings remain; this update does not claim a fresh verification of them.
- No source was scraped in bulk, no organiser was contacted, no Gmail access or paid service was used. The remaining gaps are mainly numerical elevation, cut-offs and precise travel details; those require source-specific review, not generic filler.

## Search visibility checkpoint, 15 November 2026

- Search Console for the verified `https://www.racedaycompare.company/` URL-prefix property shows the sitemap last read on 14 November with **Success** and 107 discovered pages. The separate domain property remains unverified.
- The Page indexing aggregate was last updated 9 November and showed one indexed URL and two marked “Crawled — currently not indexed.” Its examples were Thames Path 100 and South Downs Way 5km. A live inspection of Thames Path 100 on 15 November instead reports **Page is indexed**, demonstrating that the aggregate is lagging.
- The same inspection showed successful Googlebot smartphone fetch and allowed indexing. It also exposed a non-`www` user-declared canonical, inconsistent with the verified `www` property and sitemap.
- Implemented a static 100-race directory, homepage HTML links, profile-to-profile and profile-to-guide links, `www` canonical URLs, 20 original race-specific decision notes, and revised six decision guides. These changes are intended to improve discovery and usefulness; they do not guarantee impressions.
- The paid GSC Wizard connector is unavailable because its trial ended. Search Console was checked directly without subscribing, buying services or accessing Gmail.

## Current publication checkpoint

- A 100-race catalogue across England, Scotland, Wales and Northern Ireland is built locally. Each record has an individual static profile URL, an official-source link, a current-edition date or an explicit date status, and a unique original illustration or image.
- Sixty-four individually researched race records were added to the previous 36. Generated profile pages and the sitemap have been rebuilt for all 100.
- This is a catalogue expansion, not evidence that every profile is comprehensive: some organiser pages do not publish numerical elevation, cut-offs, travel or facilities. Unknowns remain explicit, and older records still need a focused refresh.
- The 1–2-hour monthly owner-workload target remains unproven at 100 races. No automated organiser scraping, paid service, contact with organisers or Gmail access was used.
- The owner explicitly authorised GitHub publication and connected the repository to Vercel. This checkpoint supersedes the older deployment-boundary notes below.

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
- On 6 November, began a source-by-source content revision for the requested 100-race catalogue. Six existing profiles now carry more specific course or logistical facts, and eleven have 2027 dates surfaced in the directory where official sources establish them. This is progress on the research, not completion of the 100-race request.
- The owner prohibited organiser contact, Gmail access and paid services. No organiser messages or purchases were made. Expansion must use individual public-source research and rights-safe imagery without bulk extraction from restricted calendars.
- Stage 2–5: search refinement, profile routes, formal data model, technical SEO, accessibility and browser testing remain in progress.
- Deployment: not deployed. The repository is ready for the owner to connect to Vercel; no hosting configuration or paid service was created by this work.\n
