# Settle Ledger — Anchor 002

**Assessment:** 002 — x402-rs facilitator (pinned image ghcr.io/x402-rs/x402-facilitator@sha256:4ebe09d824bf6a5f342add8ae22eb44a2c56894ad22e7d3f5b83ba38023226b9), Base Sepolia (eip155:84532)
**Frozen:** 26 Sep 2026 (MYT)
**Method:** see METHOD.md — sums first, signature, commit, OpenTimestamps (pending -> upgraded after confirmation), hash chain to prior anchors

## Artifacts (see SHA256SUMS in this directory)

| File | sha256 | Note |
|---|---|---|
| 002-report.md | 9b6a456d…6e3b | Assessment report, freeze candidate; internal review complete 26 Sep |
| 002-scoring-sheet.md | e1f99423…8567 | Prediction scoring vs pre-registration, frozen 24 Sep |
| 002-pre-registration.md | 9de15c58…5b10 | Pre-registration, anchored 002-pre 17 Sep; published here unsealed |
| 002-disclosure-mechanism-corrected.md | f0c878c8…af6e | Corrected disclosure mechanism paragraph (supersedes bounced 24 Sep email's paragraph) |
| 002-audit.json | e027fad8…a08e | On-chain balance audit (private evidence repo; hash verified on-box 26 Sep) |

## Deliberately unpublished at anchor time

This is the first Settle anchor whose primary artifact (002-report.md) is intentionally NOT public at anchor time. The report has been disclosed to the subject maintainer by a channel still being established (recipient domain MX failure as of this anchor; attempt record in report section 6). Publication is held to the later of 8 Nov 2026 and 45 days from confirmed maintainer receipt, per the lab's disclosure policy including its unreachable-maintainer clause.

A reader who encounters the report's hash before publication should understand: the anchor proves the report existed, byte-for-byte, on 26 Sep 2026 — before the disclosure window closed. It is not withheld from the ledger; it is withheld from the world until the window closes. The pre-registration and scoring sheet ARE public from this anchor, so the prediction record is verifiable independently of the report's release.

## Chain

Anchored after 001/001a. Custody chain for bench evidence: cd7a2f3 -> c04679c -> cc8bdc0 -> 99f62f1.
