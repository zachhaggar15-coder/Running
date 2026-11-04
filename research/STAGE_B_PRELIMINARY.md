# Preliminary Stage B concepts

Prepared 4 November 2026. These are design sketches only; no application, database service, paid plan, domain or public deployment was created.

## Brand directions

- **Race Fieldnotes**: editorial, source-led race profiles and practical notes.
- **Race Reference UK**: explicit UK search intent and a factual reference tone.
- **Startline Atlas**: discovery and geography emphasis.

These are working concepts, not cleared names. Trademark, domain and search checks would precede selection.

## Data model sketch

`organiser` owns `race`; `race` has `edition`; `edition` has one or more `course` rows. Every `fact` belongs to an edition or course, with value, unit, status (`confirmed`, `historical`, `unknown`, `disputed`), source URL, source title, checked time and reviewer note. `source` records terms review and permitted access method. `change_observation` stores a detected difference; `review_task` queues ambiguous changes. A public page should use only confirmed facts and should never infer an upcoming edition from an old one. No runner accounts or visitor personal data are needed.

## Page wireframes

**Discovery:** one clear search box; region, distance, terrain and date filters; result cards with event name, edition, course distance, location, date and last checked date. A card with sparse verified data should remain out of public results until it meets the threshold.

**Race profile:** title with edition and course; compact practical facts; “What to know before race day” for cut-off, course/elevation, travel/parking, facilities and rules; source/checked date beside consequential values; explicit “not confirmed for this edition” states; links to organiser registration and official race information. Original wording only.

**Curated region page:** a short original introduction and a filtered set of verified races with comparison fields that are actually populated. Do not create indexable combinations without enough useful content.

## Low-maintenance workflow hypothesis

1. Maintain a small list of permission-reviewed sources and allowed check methods.
2. Detect page or structured-feed changes; match them to edition and course; keep old facts separate.
3. Automatically accept only clearly scoped, low-risk changes where permitted and validated. Queue conflicting dates, route revisions, missing pages and rights questions.
4. Have ChatGPT Work research queued cases and prepare a proposed change with citations. The owner handles only consequential unresolved decisions.

This workflow remains a hypothesis. The pilot did not prove permitted automation, exception rates or a 1–2-hour monthly owner workload. It is a gate for later design, not authority to build a crawler.
