
## CLOSED ITEM — Token launch (reviewer ruling, ratified by operator, 22 Sep 2026)
Question: should Settle ever launch a token? Ruling: NO — deleted entirely, not drawered.
Mechanism: a tradable token makes every judgment a market event; the price becomes an
undeniable financial interest in findings. No firewall survives: judgments/network and
judgments/treasury separations fail on paper; excluding measured parties from holding is
unverifiable on a public chain, and an unverifiable claim contradicts the lab's model.
Non-transferable credentials add nothing the Ledger doesn't do; separate-entity tokens
are fiction once marketed as "the Settle token." Regulatory edge: publication timing
would read as trading windows. Cite this ruling; never re-debate.

## CLOSED ITEM — Correction shape: anchored artifacts vs unanchored drafts (reviewer ruling, 4 Oct 2026)
Rule: anchored artifacts (Ledger rows, frozen reports, published documents) carry corrections as
APPENDED errata with the original text untouched — the record shows both what was claimed and when
it was corrected. Unanchored drafts (PR-branch documents, review-surface text) get INLINE revision
with a dated Correction block in the body, so a reader of the current text sees that it was
corrected and when, and the git history shows what changed. Condition for inline revision: the
Correction block must be in the body itself, not only the commit message. First exercised 4 Oct
2026: the settlement-gating note (unanchored, branch review surface — inline, with a
"Correction (4 Oct 2026)" block) and the Ledger rows (anchored — appended errata, original body
preserved). Cite this ruling; do not re-derive per instance.

## POLICY CHANGE LOG — v1.1 (7 October 2026)

Per disclosure policy §11 ("changes are versioned, dated, and published in the Settle Ledger with a change log"). Hub commit 2abb5b8 (signed, anchor key), pushed and live-verified on settle-hub main, 7 Oct 2026.

- disclosure-policy v1.0 → v1.1: §5 contact-attempt cap (two documented delivery attempts ≥14 days apart, plus 30 days of silence; no third nudge, no channel-hopping; on delivery failure the attempt record is appended to the report and the §4 window runs from the last documented attempt); §10 every report header cites the accuracy record's state (anchors/ACCURACY.md). Assessments 001 and 002 remain governed by v1.0.
- independence-policy + about: the accuracy record is published, not internal — closes the 26 Sep reviewer-queue item (declared-vs-actual).
- independence-policy: reviewer selection is not shopped — pre-registered candidate order, declines final for the round, 90-day silence honored after a final nudge.
- independence-policy: dormancy-banner bullet corrected to the live mechanism (scheduled Pages rebuild, commit-age key, live since 2 Oct; MECHANISMS.md) — declared-vs-actual fix.
- external-reviewer-seat: no-reviewer-shopping term added.
