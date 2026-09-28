# Settle — Accuracy Log

Shared record of claim-vs-surface errors, filed same-day per the Mutual Verified-From Protocol.
Format: date filed · claim · surface that caught it · disposition.

## 26 Sep 2026

1. Stated file hash (2f1c6e54...) in the same message as the edit it described — the stated hash did not match the bytes Fable received (bada29b6...). Caught by Fable in the read-2 preamble. Disposition: rule 3b adopted — hashes computed only after all edits to a file are complete; corrected hash (9b6a456d...) stated and freeze completed.
2. Sent Fable a stale report attachment (0.2 bytes, d26a0b37...) while reporting 0.2 fixes as current — the operator's download was from the previous day. Caught by Fable: received hash did not match stated content. Disposition: versioned filenames (DRAFT-0.3, -0.4 as new files) + stated hash in cover text; rule adopted.

## 25 Sep 2026

3. Dupe-sweep report element attributed to a 17 Sep ruling; no operator-side surface carries it (handovers began 21 Sep; bench folder's earliest is 21 Sep). Reviewer record only, never upgraded to SHOWN. Disposition: re-issued and bound 25 Sep per Fable ruling; recorded as reviewer-record-only.

## Pre-protocol backfills (reviewer-side, recorded 24 Sep — the drift class this log exists to catch)

4. PayAI proposed as open-source assessment subject — hosted-only; caught by research before execution.
5. 001 "misreported reason" claim — facilitator was correct; caught by isolation probes.
6. Ledger-procedure content reviewed before its premise (git init on existing repo); caught by 17 Sep status.
7. 22 Sep pre-staged accuracy entries — correct outcome but record-over-surface until pointers landed.

## 28 Sep 2026

8. Checklist register listed "coinbase/x402" for issues #3465/#3471; correct repo is x402-foundation/x402. Caught during reviewer read prep, self-caught before any execution against the wrong register. Disposition: register corrected; all PR/issue references re-verified against the x402-foundation org repo.
9. PR #3471 rebase plan did not account for the repo's verified-signatures gate: the original commits were GitHub-web-signed and a local rebase left them unsigned; first force-push (4841ffd0) went public unsigned and triggered the repo's unverified gate. Corrected per reviewer ruling: dedicated contributor GPG key generated on the signing host, four commits re-signed and re-pushed (954fe97b). Sub-fault: first signing pass amended committer to root@srv1929364.hstgr.cloud (repo-local git identity absent in fresh clone); caught by verify-before-push, corrected before the public push. Both sub-faults pre-empted by the same discipline: verify signatures and committer metadata before push.
10. Reviewer handoff claim "VPS holds no signing keys by design" — premise wrong; the Ledger secret key is resident on the VPS (signing host per policy v5) and the 26–27 Sep anchor signing ran there. Record-over-surface class, filed against the reviewer. Disposition: key-hygiene rulings now state the actual posture; existence table records both keys' backup postures.
