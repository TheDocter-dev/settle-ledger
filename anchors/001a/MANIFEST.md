# anchor-001a — Corrective Freeze Anchor

**Date:** 22 Sep 2026 (publication day, MYT)
**Supersedes:** anchor-001 (commit 12bf15ff8f304a704a0213462d4d09db0802c82f) — which remains in the Ledger untouched; this anchor is the forward correction. Anchor-001's History section already records one prior correction (freeze-date labels); this is the second.
**Reason:** Pre-publication mechanism sweep found present-tense claims in two anchored artifacts that were false on the intended publication day — designed-but-never-built mechanisms asserted as existing. Corrected before publication; no reader ever saw the false text.

## What changed (exact before/after)

### independence-policy.md
`6940031bc164ae39cb7186a7d001c5f5706cc198f00bbce8e268f3a8bcffcf93` → `f0af474253585c8ffef89fd664e726e2bcd70ec00bac5f5583a0f25db4ac6740`

1. Continuity intro — BEFORE: "Two arrangements limit single-operator risk, and both are public in existence, trigger, and powers — the trustee's *identity* stays private, the arrangement does not:" / AFTER: "Two arrangements address single-operator risk — one in force today in manual form, one planned — and both are public in existence, trigger, and powers:"
2. Key escrow — BEFORE: "Signing and infrastructure credentials are held in escrow with a trustee, released on the operator's death or incapacity…" (present tense; no trustee arrangement existed) / AFTER: "**Key escrow (planned).** …No trustee arrangement is in place yet. Escrow is planned by 31 October 2026 with a named trustee whose powers will be enumerated and bounded — publish the dormancy banner, and publish a signed revocation of the signing key — and nothing else…" (full text in the artifact)
3. Dormancy banner — BEFORE: "A job on the hub checks the liveness feed daily… the banner is posted by the job itself" (no such job existed) / AFTER: "**Dormancy banner (automated, planned).** A job on the hub will check the liveness feed daily… Activation target: 30 September 2026. Until activation, the same 30-day rule applies and the banner is posted manually by the operator."

### about.md
`492742e68cc2b1b5b55647e87ec404cfca3939ad2b3b3ff9bb17c0e1d01b8950` → `46f7e02dec093020b7c0d606db581776ad82cf7467273415e7372ae8c8e5ac69`

Line 27 — BEFORE: "Continuity arrangements — key escrow and a dormancy banner rule — are described in the Independence Policy." / AFTER: "Continuity arrangements — a dormancy banner rule and a planned key-escrow arrangement — are described in the Independence Policy, together with their current status."

## What was added

- `MECHANISMS.md` (`01125f714af2c5c23dd0b23ecc037fbeccaf68f53f69b4c758892ce58797f3ee`) — internal mechanism inventory: every mechanism claimed by any public artifact, typed job / procedure / planned, with implementing path and last-observed run. Structural fix for the failure class that caused this correction: no present-tense mechanism claim without an inventory row backed by an observed run.

## What did NOT change

Every other row of anchor-001's SHA256SUMS is hash-identical here: assessment 001 report, external-reviewer-seat, disclosure-policy, chain-catalog-v3.py, solana-design-doc, chain-scoring-table, artifact-hashes.txt, x402-procurement-checklist/README.md (published at its own repo, TheDocter-dev/x402-procurement-checklist, per anchor-001 MANIFEST row 10). Verified by re-hash on 22 Sep 2026.

## Method note

x402 2.23.0 (PyPI, 15 Sep 2026) was rowed in the Ledger release feed on 22 Sep 2026 (`releases/2.23.0.md`, settle-ledger) — logged within the corrected manual-check cadence; the missed detection window is recorded in the internal accuracy record. Ledger METHOD/README cadence sentences updated to manual-interim wording in the same commit series (unanchored files, ordinary signed commits).

**OTS proofs:** SHA256SUMS.ots stamped at commit time; upgraded .ots committed after Bitcoin confirmation (non-blocking), same procedure as anchor-001.
