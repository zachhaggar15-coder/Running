# Initial source compliance register

Checked 4 November 2026. This is an operational screening record, not a legal opinion or a grant of reuse rights. Re-check the exact source terms before any importer or recurring fetch is implemented.

| Source class | Proposed use | Status | Condition / next check |
| --- | --- | --- | --- |
| Official organiser event pages and current-edition FAQs | Individually verify minimal factual values; link to source; write original commentary | **Conditional** | No blanket licence established. Inspect each site's terms and access controls before repeated automated retrieval. Do not reproduce prose, photos, maps, logos or GPX. Record URL, edition and access date for each fact. |
| Official organiser calendar pages | Find candidates and follow through to the edition page | **Conditional** | A calendar is not permission to copy a substantial collection. Assess terms and database rights before systematic extraction. |
| Direct organiser submissions | Future first-party factual source | **Not yet implemented** | Need submission terms, accuracy review and abuse/moderation process. Excluded from the first release in the brief. |
| Expressly licensed feed or API | Potential structured import | **Awaiting licence** | No suitable UK-wide feed or licence has been confirmed. Require written scope covering storage, display, update cadence, attribution and sublicensing restrictions. |
| Find A Race, Let's Do This, runABC, Time Outdoors, Race For You, RaceIndex, FindTrail and other directories | Competitive analysis only | **Excluded from ingestion** | Do not bulk copy or use these as a seed database without explicit permission. Public accessibility and robots.txt are insufficient permission. |
| UK athletics body fixture calendars | Candidate discovery only | **Awaiting terms** | Check publisher-specific licence and whether the calendar's contents or compilation may be reused. Verify each date against the organiser. |
| OpenStreetMap / OpenStreetMap-based geodata | Possible location display and search | **Awaiting design and licence review** | ODbL attribution/share-alike and service usage policies need review for the chosen implementation. Avoid importing geodata until then. |
| Google Search results and Google Trends | Qualitative market research | **Research only** | Do not scrape into a race database or treat observed results as a licensed data feed. |

## Pilot source-specific findings

| Source | Observed condition | Operational status |
| --- | --- | --- |
| [Great Run website terms](https://www.greatrun.org/website-terms-and-conditions/) | Terms expressly reserve rights in text, data compilations and other site content, and prohibit reproduction or derivative use without prior written consent. | **Restricted:** do not automate extraction or reuse site content. Any ongoing systematic use needs permission or qualified legal review. Individual race facts in the research table are screening evidence, not approval to publish content sourced from this site. |
| [RunThrough terms](https://www.runthrough.co.uk/terms-and-conditions) | The reviewed page is participant entry terms, not a reuse licence for website data. | **Conditional:** individual factual research only; no importer. Seek source-specific clarity before automated checks. |
| [Centurion 2027 event page](https://www.centurionrunning.com/races/south-downs-way-50-2027) | Rich edition-specific page; no reuse licence identified in this review. A separate live-tracking product has its own copyright notice. | **Conditional:** original factual summaries only; do not copy course description, live-tracking data, map or GPX. Automated monitoring needs review. |
| [Highland Fling](https://www.highlandflingrace.org/) and [Devil o' the Highlands](https://www.devilothehighlandsfootrace.co.uk/event-information) | Official pages contain apparent date/edition inconsistencies. | **Hold:** seek organiser clarification before a current-edition profile. Do not resolve contradictions by copying another directory's date. |
| [26.events Causeway Coast page](https://26.events/event/causewaycoastmarathon), [Antrim Coast site](https://antrimcoasthalfmarathon.com/), [Armagh organiser site](https://armaghinternationalroadraces.com/) | Research access returned only a loading shell or failed. | **Hold:** no bypass of access controls; use an openly accessible official page or direct permission if needed. |

All other named organiser sources in [the 30-race audit](../research/pilot_30.tsv) remain **conditional** for individual factual research and **unapproved** for recurring automated retrieval. This pilot did not establish a reusable UK-wide feed or licence. Candidate records are not cleared for public posting merely because the source page is official.

## Legal basis for caution

The [UK Intellectual Property Office](https://www.gov.uk/guidance/sui-generis-database-rights) says database rights can protect the contents of a database where there has been substantial investment in obtaining, verifying or presenting them. [Regulation 16](https://www.legislation.gov.uk/uksi/1997/3032/part/III) also covers repeated systematic extraction of insubstantial parts. The [IPO copyright overview](https://www.gov.uk/copyright) identifies web content and photographs as potentially protected works. These sources do not prohibit independently researching individual facts, but they make bulk directory copying a poor default strategy. Obtain qualified legal advice if a planned source or reuse method remains materially uncertain.
