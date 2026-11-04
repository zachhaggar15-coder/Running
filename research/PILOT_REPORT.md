# 30-race sourcing pilot: feasibility checkpoint

Research date: 4 November 2026. This is a source and content feasibility audit, not a set of publish-ready race pages. The row-level evidence and official links are in [pilot_30.tsv](pilot_30.tsv); rights screening is in the [source compliance register](../docs/SOURCE_COMPLIANCE_REGISTER.md).

## Sample and method

The 30 candidates span England (8), Scotland (8), Wales (7) and Northern Ireland (7); road, mixed, trail and ultra races; national series and small organisers; 5K to 100-mile distances. Inaccessible and poorly maintained official sites were retained in the sample. The target edition is 2027 except two still-upcoming 2026 Scottish/Welsh races. A prior-edition detail was never counted as current merely because an older FAQ remained linked from a 2027 page.

Each row counts **verified practical field categories**, not every atomic fact. Codes: D date; L start/location; X distance; C course description or format; E numerical elevation; T cut-off time; P public transport; K parking; F at least one facility such as water, toilets or baggage; R a rule or mandatory kit; A entry information. A code means that at least one useful value in that category was visible on an official source and attributable to the target edition. Historical codes are kept separate. Course-specific values were not transferred between distances. The TSV's note records limitations, and `review_flag` identifies conflicts or stale material.

The **provisional factual minimum** requires D, L, X, C and two more useful categories, with no material date or race-identity conflict. A **detailed candidate** also needs at least eight categories, including three from E, T, P, K, F and R. These are content screening thresholds, not legal clearance, final editorial verification, or a guarantee of search value. A future public profile should additionally show the checked date, edition, linked sources, original text, and clear unknowns; it must pass source-use review.

## Quantitative result

| Measure | Observed |
| --- | ---: |
| Races researched | 30 |
| Provisional factual minimum met | 15/30 (50%) |
| Detailed-profile candidates | 11/30 (37%) |
| England: minimum / detailed | 6/8 / 5/8 |
| Scotland: minimum / detailed | 4/8 / 3/8 |
| Wales: minimum / detailed | 4/7 / 3/7 |
| Northern Ireland: minimum / detailed | 1/7 / 0/7 |
| Current-edition field categories per race | mean 5.47; median 5.5 |
| Numerical elevation confirmed | 6/30 (20%) |
| Cut-off confirmed | 10/30 (33%) |
| Public transport confirmed | 6/30 (20%) |
| Parking confirmed | 6/30 (20%) |
| At least one facility confirmed | 15/30 (50%) |

These denominators include the seven candidates with no confirmed current-edition facts. A missing field means **unknown from reviewed official sources**, not that the event lacks the feature. Eleven records have enough field coverage to support genuinely useful logistical or course profiles in principle. Four more cross a minimum factual threshold but would still be fairly thin. The other fifteen should remain unpublished as current-edition profiles until more evidence is available.

## Value beyond a basic listing

The strongest detailed candidates combine decision-useful facts that a date/location/distance listing usually omits: South Downs Way 50 and Snowdonia Trail Ultra have ascent, staged or overall cut-offs, aid and rules; Richmond Park Half combines a lap format, cut-off, rail access, parking and facilities. The three [original profile drafts](profile_drafts.md) show how facts could be presented with explicit sources and unknowns. They are editorial sketches, not completed publication reviews. Many road-race pages have a date and distance but weak current-edition travel, parking or elevation detail; those offer little defensible differentiation yet.

## Verification and maintenance experiment

Thirteen records were fetched again later the same day and their visible text compared. Eleven returned the same content. Two changed only in unrelated navigation or related-event widgets. No observed race fact changed. This shows a repeat fetch can be performed for many pages, but **a same-day comparison does not establish monthly stability or update reliability**. Three Northern Ireland pages remained inaccessible or rendered only a loading shell. Several accessible pages still required judgment to separate years or distances. Examples:

- Highland Fling's official page displayed conflicting 2027 month references and older/other-event copy; the current date was held out of the table.
- Devil o' the Highlands had a 2027 date with inconsistent parking-month text; it was held pending organiser clarification.
- Manchester, Great North, Great South, Cardiff, Porthcawl, Rabbit Run and Omagh linked current pages to older timetable, FAQ, route or baggage details. Their historical categories were kept separate.
- Maverick and Race to the Stones have multiple course variants; elevation or cut-off must be attached to the correct distance.

The second pass exposed the need for edition- and course-specific provenance, visual/content diffs, change queues and human exception review. It did **not** measure an automated monitoring system: source-specific permission has not been obtained and no recurring crawler was built.

## Time and owner-workload evidence

**Per-race creation time: unmeasured.** Research was done in batches, so a defensible mean or median elapsed time per event cannot be reconstructed. The three profile drafts were made after sourcing and do not measure the time to create fully verified profiles. Machine page-fetch latency is also not human or agent editorial time. Reporting a numeric average/median here would be invented. A sequential, timed production-quality sample is required before committing to a 200–300-profile build.

**Human intervention:** the TSV marks 25 of 30 rows with a review flag (including routine edition or course scope issues); this is a conservative proxy for potential intervention, not measured minutes. Of those, some would be handled by clear edition/course rules, while contradictions, inaccessible pages and permissions need human or organiser decisions. The 1–2-hour monthly owner target is not yet demonstrated.

Planning scenarios below are arithmetic, **not measured forecasts**. They assume one check per race per month, 8 minutes of human review per exception, and 30 minutes of fixed monthly oversight. They exclude source negotiation, fresh editions, dead links, large event changes and new profiles.

| Portfolio | 5% exception rate | 10% exception rate | Manual 3 min/race + oversight |
| --- | ---: | ---: | ---: |
| 200 races | 1 h 50 min | 3 h 10 min | 10 h 30 min |
| 300 races | 2 h 30 min | 4 h 30 min | 15 h 30 min |
| 1,000 races | 7 h 10 min | 13 h 50 min | 50 h 30 min |

Even the optimistic automated scenario exceeds two hours at 300 races. At 200, it barely fits, with no capacity for new editions. The pilot's 20 flagged cases are not a valid steady-state exception rate, but they argue against assuming 5% without a working, permitted process. To keep owner time near 1–2 hours, ChatGPT Work would need to perform approved source checks and exception triage, with only consequential unresolved cases sent to the owner. Source terms currently prevent treating that as an available capability.

At the observed **50% factual minimum yield**, finding 200–300 qualifying records could require screening roughly 400–600 candidates if this sample were representative. The 37% detailed yield would imply roughly 545–820 candidates for 200–300 detailed profiles. Those are simple yield extrapolations, not a validated market-wide sampling estimate. For labour planning only, 15/30/45 minutes of production work per accepted profile would imply 50–75 / 100–150 / 150–225 hours for 200–300 profiles, before candidate screening or maintenance. No one of these time assumptions has yet been validated, so a credible average/median and total effort remain open.

## Source and legal constraints

Official pages did not provide a blanket data licence. [Great Run's website terms](https://www.greatrun.org/website-terms-and-conditions/) are particularly restrictive about content and compilations; its two race rows must not be read as publication or automation approval. RunThrough participant terms are not a data reuse licence. No source-specific approval for bulk collection was established. Competitor directories were excluded from ingestion. No third-party prose, images, maps or GPX were copied into the profile drafts. No personal data, visitor account or tracking design was introduced.

## Feasibility decision

**Narrow the next stage to validation, while retaining the 200–300 target as an unapproved launch gate.** The data is promising for selected races, especially ultras, but the national coverage is uneven, practical fields are sparse, rights are conditional, and time/maintenance costs are not proven. Do not start substantial application development or publicly launch profiles from this audit. Before deciding to build toward 200–300, run a sequential timed sample of complete profiles, obtain source-specific automation/reuse clarity for priority organisers, and repeat maintenance checks across a real edition-change window. If those fail to support meaningful coverage and at most 1–2 hours of owner work per month, discuss a smaller launch or a different content strategy with the owner; do not silently lower the target.

The accompanying [SEO report](SEO_REPORT.md) finds possible demand for practical answers, but no evidence that comprehensive profiles alone will win Google impressions. The likely content strategy is selective, source-linked event pages and tightly curated discovery pages, then measurement in Search Console after an authorised launch.
