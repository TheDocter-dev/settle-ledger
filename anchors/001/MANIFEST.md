# anchor-001 — Settle Freeze Anchor

**Date:** 19 Sep 2026 (freeze day, afternoon MYT; publication still 22 Sep)
**Repo:** settle-ledger (live since 15 Sep 2026) — `anchors/001/`, signed commit on protected `main` by the existing Ledger key (ed25519, 3C15C334…CD3C0642)
**Numbering:** anchor numbers follow assessment numbers, not commit order — anchors/002-pre-registration.md was committed first by design (pre-registration before execution); 001 is the freeze anchor for the first publication package.
**Commit:** 12bf15ff8f304a704a0213462d4d09db0802c82f
**OTS proof:** SHA256SUMS.ots + anchor-001-commit.txt.ots — stamped afternoon of 19 Sep (MYT); upgraded on Bitcoin confirmation; commit-hash proof binds the OTS attestation to the git tree, not just the sums file.

## What this anchor establishes

The artifacts listed in SHA256SUMS existed in exactly this form on or before the Bitcoin-confirmed timestamp of the accompanying OpenTimestamps proof. OpenTimestamps proves **prior existence only** — it proves nothing about the truth of any claim inside an artifact. Verification steps: each row below names where the bytes are published.

Published locations resolve from 22 Sep 2026; the anchor precedes publication by design (anchor-before-share).

## Anchored artifacts (sha256 + published location per row)

| # | Artifact | sha256 | Published at |
|---|---|---|---|
| 1 | Settle Demo Report — Faremeter v0.22.0, **v1.0 freeze version** (date inside the hashed text; DRAFT 0.3 hash superseded by design) | 251462925260bb4d45ae88762cd98518f36b8f29df96345ed5a06539e157e5fb | https://github.com/TheDocter-dev/settle-hub/blob/main/assessments/001-faremeter-v0.22.0.md |
| 2 | independence-policy.md v5 | 6940031bc164ae39cb7186a7d001c5f5706cc198f00bbce8e268f3a8bcffcf93 | https://github.com/TheDocter-dev/settle-hub/blob/main/independence-policy.md |
| 3 | about-page.md v2 | 492742e68cc2b1b5b55647e87ec404cfca3939ad2b3b3ff9bb17c0e1d01b8950 | https://github.com/TheDocter-dev/settle-hub/blob/main/about.md |
| 4 | external-reviewer-seat.md v2 | 259f98cefbc057b0b8c9c742c7332cb38df1792ff92f73b992818dde596abcc8 | https://github.com/TheDocter-dev/settle-hub/blob/main/external-reviewer-seat.md |
| 5 | Disclosure policy, standing v1.0 (governs 001 by its effective-date clause) | fb4363ad2e3af69b1f2f9e93a7f2a2fe8364c2e8ff29e37b77be29e4c3a547ff | https://github.com/TheDocter-dev/settle-hub/blob/main/disclosure-policy.md |
| 6 | Deployed catalog code, v3.2.2, published in full (sha256 of the deployed file; md5 d0063f2f… remains the deploy.log identity; seed and state files stay private — they are separate artifacts) | fd8b1ef0ebddc9afddc090c1ba5203275ef3a9edaceed593b70ba7f3b8eeb667 | https://github.com/TheDocter-dev/settle-hub/blob/main/chain-catalog-v3.py |
| 7 | solana-design-doc.md v0.5 | a57e924b18458c510300e675342944b8b180bcee17b1bb7da6bde51cea384a32 | https://github.com/TheDocter-dev/settle-hub/blob/main/solana-design-doc.md |
| 8 | chain-scoring-table.md v3 | d14ed9963ba0964cd4daa1244a6a8579f39ee3fa3a45ff2539b08a789eee4c3a | https://github.com/TheDocter-dev/settle-hub/blob/main/chain-scoring-table.md |
| 9 | artifact-hashes.txt (the report's own evidence manifest — Appendix B promises this anchor) | 2e821d3c26ebd72a29fab5f049028006ed7b8bd5e62756ad99dde8b9d188233f | https://github.com/TheDocter-dev/settle-hub/blob/main/assessments/001-artifact-hashes.txt |
| 10 | x402-procurement-checklist v1.0 (CC-BY, already public, linked from hub post and report) | d25590b606097bc258d2f86cf5c5ea7ef35bf0e2a6715f2539e8ea92ce9317da | https://github.com/TheDocter-dev/x402-procurement-checklist |

## Method version in force

Base chain catalog: **v3.2.2** (same-basis accounting, events_tracked/txs; legacy events for cluster threshold only).

**Code freeze declaration:** no change to the deployed measurement artifact between this anchor and publication (22 Sep). Cron (daily 06:17 UTC) writes *state*, not code, and is ledgered per run with pre/post state sha256 in deploy.log. Freeze is a code freeze, not a data freeze.

## Explicitly NOT anchored

Catalog state files, the internal accuracy record, cluster/batch address mappings (Policy S.1), VPS deploy.log (operational ledger, separate trail). The Ledger anchors hashes of publication-grade artifacts only — redaction-clean by construction.

## Pre-registrations and governing documents in this anchor

1. (via artifact 7) Solana first-run invariants: sighted facilitator feePayer set classifies as attributed; no sender classified batch-shaped before any sender reaches 20 tracked events; tier-two two-way check once slot sampling exists. Frozen 18 Sep, four weeks before the first Solana measurement run.
2. (via artifact 5) Governing document: disclosure policy v1.0, effective for 001 by its effective-date clause — a governing document, not a pre-registration.

## History

- 15 Sep 2026: settle-ledger live, verified signed commit.
- 17 Sep 2026: SECURITY.md, signing-key block, LICENSE, 002-pre-registration committed and verified.
- 18 Sep 2026: artifacts 7 and 8 finalized; artifact 7 independently recomputed from a separately transferred copy.
- 19 Sep 2026: GitHub key registration completed; retroactive Verified across history. Consistency gate PASS (4 governing docs, 0 mismatches).
- 19 Sep 2026: report v1.0 date inserted (22 September 2026); final sha256 25146292…e5fb (intermediate hash superseded by the Appendix-B hash-completeness fix — caught by the consistency gate). SHA256SUMS finalized (all 10 rows). Freeze executed this afternoon (MYT).
- 19 Sep 2026 (001a correction): freeze-date labels corrected from 20 Sep to 19 Sep — freeze actually executed afternoon MYT 19 Sep (UTC+8); commit messages of 12bf15f and 0646e35 retain the 20 Sep mislabel (immutable); SHA256SUMS and both OTS proofs carry no dates and are unaffected.
