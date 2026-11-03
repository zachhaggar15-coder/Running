# Stage A — research and feasibility

Research snapshot: 3 November 2026. This is a decision checkpoint, not launch approval. The research is directional: it uses live public pages and a small official-source spot check, without paid keyword data, a representative data audit or legal review.

## Assessment

**There is a plausible but unproven search opportunity.** People search both for event calendars and for practical race-day facts. Broad distance/location calendars are already crowded. The stronger hypothesis is a reference that answers edition-specific questions such as *What is the cut-off? Is bag drop confirmed for this edition? Which station should I use?* with linked evidence, a last-checked date and an explicit unknown state. That value must be validated with a sourcing pilot; it cannot be manufactured by adding a large number of thin pages.

The competition is stronger than the original brief might imply. [Find A Race](https://findarace.com/half-marathons) has extensive distance, season and place landing pages and many 2027 listings. [Time Outdoors](https://www.timeoutdoors.com/events/half-marathons/scotland/march) already targets combinations such as Scottish half marathons in March. [Run Club Directory](https://runclubdirectory.co.uk/events) has location/radius, distance, date, terrain, status and price filters. [Race For You](https://raceforyou.co.uk/half-marathons/scotland) already shows confirmed upcoming editions, surface, month and location search and a compare link. [FindTrail](https://findtrail.co/race) offers substantial ultra data and [side-by-side comparison](https://findtrail.co/race/compare). [RaceIndex](https://raceindex.org/running-events/uk) positions itself around routes and elevation. A generic event directory, basic comparison table or elevation filter alone would be weak differentiation.

The potential gap is **high-trust practical information spanning road and trail**, with a transparent field-level evidence model, current-edition boundaries and useful comparison of known facts. That is an inference from the sampled competitor pages, not a claim that no competitor provides it. The [2026 Manchester Marathon bag-drop FAQ](https://www.manchestermarathon.co.uk/bag-drop-faqs/) illustrates why edition boundaries matter: a previous edition's arrangements cannot silently become a 2027 fact.

## Search opportunity map

| Intent | Observed competition | Initial judgement / page strategy |
| --- | --- | --- |
| “half marathons Scotland March 2027”; distance + place/month | Dedicated pages from [Time Outdoors](https://www.timeoutdoors.com/events/half-marathons/scotland/march), [Find A Race](https://findarace.com/half-marathons), and others | High competition. Build only a small number of curated, useful landing pages after coverage exists; do not mass-generate place × month pages. |
| “flat half marathons UK” / elevation comparisons | Specialist content and [RaceIndex](https://raceindex.org/running-events/uk) / [FindTrail](https://findtrail.co/race) course data | Competitive. Only publish a claim of flatness with an explicit measure or official course evidence, and explain coverage gaps. |
| Race name + year | Organiser pages and major directories tend to appear | Hard for a new site to displace official pages; a profile can still earn use if it adds independently useful, sourced logistics. |
| Race name + cut-off, bag drop, headphones, transport, water stations | Organiser FAQs/participant guides appear, often edition-specific | Best test area for a specialist reference. Aggregate facts carefully with source links and verification dates. Use unique prose, not copied FAQ text. |
| Trail/ultra by region + elevation/cut-off | [FindTrail](https://findtrail.co/race) is already sophisticated for ultras | Do not treat this as uncontested. Focus on cross-category comparison and source freshness if the pilot proves it. |

Illustrative live result checks included [Scottish half marathons in March 2027](https://www.timeoutdoors.com/events/half-marathons/scotland/march), an [official Alloa 2027 page](https://alloahalfmarathon.co.uk/), [flat UK half marathon editorial content](https://therunnersjournal.co.uk/flat-uk-half-marathons/), and an [edition-specific Manchester bag-drop FAQ](https://www.manchestermarathon.co.uk/bag-drop-faqs/). Search results vary by location and time. **No monthly search volumes, Google Trends index, competition scores or traffic estimates were obtained.** A keyword-data pass and repeatable SERP sample remain necessary. Google's [helpful-content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) and [scaled-content policy](https://developers.google.com/search/docs/essentials/spam-policies) reinforce the need for original practical value per indexed page.

## Data feasibility and proposed coverage

The official-source spot check found publicly visible 2027 dates across the four nations:

| Nation | Example official source | What the check establishes |
| --- | --- | --- |
| England | [Great North Run](https://www.greatrun.org/events/great-north-run/) says 12 September 2027; [Manchester Marathon](https://www.manchestermarathon.co.uk/news/how-to-get-a-place-in-the-2027-adidas-manchester-marathon/) says 18 April 2027. | Confirmed published dates, not complete profiles or reuse permissions. |
| Scotland | [Alloa Half Marathon](https://alloahalfmarathon.co.uk/) says 21 March 2027; [Scottish Half Marathon](https://www.scottishhalfmarathon.com/half) says 15 August 2027. | Confirmed published dates, not complete profiles or reuse permissions. |
| Wales | [Run 4 Wales](https://www.run4wales.org/thousands-take-to-the-streets-of-cardiff-for-2026-cardiff-half-marathon/) says Cardiff Half returns 3 October 2027; its [events page](https://www.run4wales.org/) lists several 2027 events. | Some date evidence exists. Individual course and logistics still need edition checks. |
| Northern Ireland | [Belfast City Marathon](https://belfastcitymarathon.com/events/2027-phoenix-energy-belfast-city-marathon) says 2 May 2027; [Omagh Half Marathon](https://omaghhalfmarathon.run/) displays a 2027 date. | Some date evidence exists. Individual course and logistics still need edition checks. |

This small search **does not establish 200–300 publishable profiles**. The most scarce data is likely current-edition course elevation, cut-offs, facilities and transport detail, not race names. A 20–30-event pilot should measure this rather than assume it. The pilot sample should include at least five events per nation; road, trail and ultra; 5K/10K/half/marathon and non-standard distances; club-run and large events; single- and multi-distance events; and both near-term and distant confirmed editions. Select candidates from official organiser sites, with any external calendars used only to discover leads pending their terms. No candidate should be public merely because it appears in a calendar.

For each pilot event, record: official URL; series, edition and course identity; exact verified facts and source pages; source terms/access limitations; time needed; update cadence; conflicts; and whether it meets a preliminary publication threshold. Suggested threshold: confirmed current edition/date or clearly undated series, official organiser link, venue/area, verified course distance and terrain, at least two additional practical current facts, original summary, field provenance and a checked date. A future edition with no confirmed date must not have a fabricated date or Event schema. Refine the threshold after the pilot. Report the achievable count before any bulk expansion.

## Rights and source approach

Use official organiser pages for individually reviewed facts and original writing, subject to source-specific terms; use an expressly licensed feed only after its licence is reviewed. No suitable UK-wide reuse licence has been verified. Do not ingest competitor directories. The [UK IPO's database-rights guidance](https://www.gov.uk/guidance/sui-generis-database-rights) and [1997 Regulations](https://www.legislation.gov.uk/uksi/1997/3032/part/III) mean a public calendar is not automatically a bulk-import source. Details and exclusions are in the [source register](SOURCE_COMPLIANCE_REGISTER.md). A recurring automated fetch needs a separate terms and access review, even if manually reading a page is straightforward.

## Recommended architecture if Stage A is approved

- Next.js + TypeScript for rendered indexable pages, with a relational Postgres model for `race_series`, `race_edition`, `course`, `fact`, `source`, and `change_review`. A fact carries edition/course scope, value/state, source URL, checked date and provenance. Unknown and confirmed-no are distinct states.
- Start the pilot in a controlled research table or database, not an automated scraper. Add import/update jobs only for sources whose reuse and access conditions are acceptable. Changes to date, venue, cancellation and rules enter review unless backed by strong current evidence. A private review queue can initially be an authenticated admin workflow or equivalent restricted database workflow.
- Server-rendered directory, profile and comparison pages. Search/filter URLs are functional for users; only curated landing pages enter the sitemap. Follow Google's [faceted-navigation guidance](https://developers.google.com/crawling/docs/faceted-navigation). Add [Event structured data](https://developers.google.com/search/docs/appearance/structured-data/event) only where current-edition facts meet its requirements; the required start date must be real. No indexing claims until Search Console confirms them.
- No accounts, advertising scripts or visitor-level tracking in the initial product. Search Console is sufficient for the first visibility measurement. Accurate privacy information must describe hosting/security processing. Review [ICO cookie guidance](https://ico.org.uk/for-the-public/online/cookies) before adding non-essential analytics.

### Indicative operating costs

At the time checked, [Vercel lists Hobby at $0/month for personal, non-commercial use and Pro at $20/month](https://vercel.com/pricing); [its terms restrict Hobby use](https://vercel.com/legal/terms). [Supabase lists Free at $0/month and Pro from $25/month](https://supabase.com/pricing); [Free projects can pause after low activity](https://supabase.com/docs/guides/platform/free-project-pausing). Thus a plausible infrastructure range is **$0 during a qualifying experiment to at least $45/month for Vercel Pro + Supabase Pro**, before VAT, domain registration, overages or any optional service. This is a scenario, not a quote or commitment. The eventual architecture may avoid a live database for public reads if static publishing proves simpler. No paid plan is authorised.

## Decision and next checkpoint

**Recommendation:** approve a narrow Stage B/pilot work package, not the full 200–300-profile build yet. The pilot should test whether source-backed practical profiles can be produced and kept current at reasonable effort, and whether the positioning remains distinctive against Race For You, RaceIndex and FindTrail. Then present pilot metrics, brand options, the final schema, page designs and a revised launch-size forecast for approval.

**Owner decision requested:** approve or amend that pilot and Stage B direction. This does not authorise public deployment, paid services, bulk import, a final brand or a reduced launch target. If the pilot cannot support 200–300 quality profiles, return with the verified achievable number and a specific scope decision.

