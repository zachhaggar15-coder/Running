# User journey improvement plan

Updated: 5 November 2026

The product promise is: **find the race that suits you, not just the race nearest you**. The journey should help a runner move from a vague intention to a confident shortlist, while showing the evidence and uncertainty behind every recommendation.

## 1. Target journey

### Stage 1: Arrive with a question

Typical entry points:

- “I want my first half marathon.”
- “I need a race I can attend without a car.”
- “I want a scenic trail race.”
- “Can I finish this race within its cut-off?”
- A race-specific Google result such as “parking” or “elevation”.

The landing page must immediately offer two routes: a guided suitability finder and direct browsing for runners who already know what they want.

### Stage 2: State the minimum context

The first interaction should ask only:

1. Distance
2. Road, trail or either
3. Main objective

The runner should get useful results without an account, location permission or a long questionnaire. Advanced preferences should appear only after the first result set.

### Stage 3: Understand the recommendation

Each result should answer three questions in the card itself:

- Why might this suit me?
- What could make it unsuitable?
- What remains unknown?

The explanation must use one of three labels: **verified**, **calculated**, or **unknown**. A missing cut-off, elevation or travel detail must never be silently treated as favourable.

### Stage 4: Narrow the shortlist

The runner should be able to refine results by:

- Region or nation
- Date or date range
- Expected finish time
- Maximum travel distance
- Flat-course preference
- Car-free preference
- Course type

Filters should appear progressively. If a filter would remove a race because the field is unknown, the interface should say so rather than pretending the race failed the test.

### Stage 5: Inspect a profile

The profile page should place practical decision fields before editorial text:

- Edition and date
- Distance and terrain
- Course and elevation
- Cut-off
- Start and finish
- Transport and parking
- Facilities
- Rules and entry

Every important value should show its source and checked date. A “What to check before entering” section should collect unresolved items into a short, useful list.

### Stage 6: Compare and decide

Comparison should support no more than three races. The table should include explanatory summaries such as:

- “Race A has a published cut-off; Race B does not.”
- “Race A has rail information, but timing feasibility is unconfirmed.”
- “Race B has published ascent; Race A’s elevation is unknown.”

The goal is a decision, not a universal ranking. The final action should be a clear link to the official organiser page.

### Stage 7: Return or share

The runner should be able to share a shortlist or a profile through a parameter-based URL without creating an account. Search details must not be indexed as public pages. No search history or personal training data should be stored.

## 2. Current friction and improvements

| Friction | Improvement | Priority |
| --- | --- | --- |
| Results currently feel like cards rather than a guided decision | Add a visible “why this suits you” and “watch out” block to every result | P0 |
| Optional preferences are not yet available | Add progressive controls for expected finish, date, travel and flatness | P0 |
| Profile overlays are useful but not durable SEO routes in the main journey | Make every card’s profile link primary and keep the overlay as a quick preview | P0 |
| Unknown fields can be overlooked | Use consistent unknown badges and a “missing information” summary | P0 |
| Comparison does not yet explain trade-offs | Add plain-language comparison conclusions beneath the table | P1 |
| Directory and guides are separate experiences | Add “Use this guide in the finder” and related-guide links on profiles | P1 |
| Sparse records may look equivalent to comprehensive records | Show a verification/detail level and explain what it means | P1 |
| Travel information may be overinterpreted | Separate “source mentions transport” from “race-day timing verified” | P1 |
| Users may not know what to do next | Add a single official-entry action and a “save/share shortlist” action | P1 |
| Stale or held records could weaken trust | Add visible last-checked dates and hide held records from indexable discovery pages | P1 |

## 3. Recommended implementation sequence

### Release A: decision clarity

- Improve result cards with verified/unknown labels.
- Add watch-outs and objective-specific explanations.
- Add expected finish time and preferred date range inputs.
- Make profile URLs the primary card action.
- Add profile breadcrumb and related-race links.

### Release B: shortlist workflow

- Add a persistent anonymous shortlist in URL parameters or session storage.
- Add remove buttons and comparison conclusions.
- Add a “why these three?” summary.
- Add an empty-state guide for every filter combination.

### Release C: confidence and trust

- Add field-level checked dates.
- Add record detail levels: essential, useful, comprehensive.
- Add “what to verify before entering” panels.
- Add a visible source-use and independence statement.

### Release D: measurement

Track only privacy-conscious events needed to evaluate the journey, subject to approval:

- Finder started
- Finder completed
- Filter changed
- Profile opened
- Official source clicked
- Comparison started
- Comparison completed
- Guide opened

Google Search Console remains the primary organic-performance measurement. Any additional analytics should be approved before implementation and should avoid storing search text or personal profiles.

## 4. Success measures

The journey should be evaluated with five representative tasks:

1. Find a flat half marathon for a PB.
2. Find a first half marathon with a clearly published cut-off.
3. Find a race where rail or shuttle information is available.
4. Compare two demanding trail races.
5. Answer a race-specific question and reach the official organiser source.

For each task, record:

- Whether the runner finds a suitable shortlist.
- Whether they understand why the races appeared.
- Whether they notice important unknowns.
- Whether they can reach the official source.
- Where they hesitate or abandon the journey.

The product should not be considered differentiated merely because it has filters. It should show that runners make a better-informed decision with less searching and less uncertainty.

## 5. Guardrails

- Never infer flatness from missing elevation.
- Never infer unlimited time from a missing cut-off.
- Never infer public-transport feasibility from a nearby station.
- Never rank a race as universally best.
- Never index thin filter combinations.
- Never store unnecessary personal search or training data.
- Keep source, edition and course boundaries visible.
