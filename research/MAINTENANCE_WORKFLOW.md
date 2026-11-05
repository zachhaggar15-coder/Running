# Maintenance and review workflow

This is the operating design for the first release. It is deliberately conservative: source-specific permissions remain a prerequisite for recurring automated retrieval.

## Record states

- `confirmed`: current edition facts checked against an official source and ready for display.
- `review`: a page changed, a new edition appeared, or an edition/course ambiguity needs review.
- `held`: contradiction, inaccessible source or material source-use uncertainty prevents publication.
- `historical`: retained for context but never used as a current-edition value.

## Review queue

Every fact stores a source URL, edition, course scope, checked date and reviewer note. A scheduled check may detect a changed page only where the source terms and access method permit it. It creates a review item containing the old value, new evidence and link; it does not silently overwrite a current fact.

The review queue is prioritised: date/race identity, course distance, cut-off, elevation, transport, parking, facilities, rules and entry. Conflicting dates, inaccessible pages and old FAQs are always human-review items. A reviewer can confirm, keep the prior value with a note, mark unknown, or hold the record.

## Publication checks

Before a profile is indexable, confirm: current edition, source link, original wording, no copied imagery or maps, no unresolved material contradiction, and explicit unknowns for missing practical fields. Completed editions move to historical status and are removed from “upcoming” discovery pages.

## Owner workload target

ChatGPT Work should prepare proposed changes and citations, then batch only consequential unresolved cases for the owner. The 1–2 hour/month target remains a design goal rather than a measured result. No bulk crawler should be enabled until each source's terms and permitted access are recorded.
