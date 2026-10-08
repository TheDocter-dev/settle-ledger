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
9. PR #3471 rebase plan did not account for the repo's verified-signatures gate: the original commits were GitHub-web-signed and a local rebase left them unsigned; first force-push (4841ffd0) went public unsigned and triggered the repo's unverified gate. Corrected per reviewer ruling: dedicated contributor GPG key generated on the signing host, four commits re-signed and re-pushed (954fe97b). Sub-fault: first signing pass amended committer to root@srv1929364.hstgr.cloud (repo-local git identity absent in fresh clone); caught by the verify-before-push control, not by chance — corrected before the public push. Both sub-faults pre-empted by the same discipline: verify signatures and committer metadata before push.
10. Reviewer handoff claim "VPS holds no signing keys by design" — premise wrong; the Ledger secret key is resident on the VPS (signing host per policy v5) and the 26–27 Sep anchor signing ran there. Record-over-surface class, filed against the reviewer. Disposition: key-hygiene rulings now state the actual posture; existence table records both keys' backup postures.

## Entry 11 — 2026-09-30 — Ledger feed coverage gap, caught by first automated run
The README declared "every release gets a row" while the feed held 12 rows
against 36 published releases (12 of 36) — untrue for the two weeks the feed
was live. Caught by the first automated poll run (poll-pypi.py, 2026-09-30),
not by a reader. Corrected the same day: 24 pending rows added in commit
0be07ab; detection automated going forward. Gap was visibility, not
falsification: no row ever claimed coverage it didn't have; the README
sentence was the inaccurate artifact.

## Entry 12 — 2026-09-30 — Dormancy banner not activated on committed date
The independence policy committed the automated dormancy banner to activate
30 September 2026. Not activated on that date: the only implementation path
then designed (a job pushing to the hub repo) was ruled out on key-hygiene
grounds (unattended push = stored credential that can publish as Settle).
Mechanism redesigned same day (Fable ruling): scheduled GitHub Pages rebuild
keyed on the age of the newest signed Ledger commit (not the liveness feed,
which can emit unattended), no commits, no stored credentials. New activation
target: 3 October 2026. Miss logged on the date it was due, not discovered later.

## Entry 12 close — 2026-10-03

Banner mechanism first live run: 2026-10-02T08:58:26Z (dormancy-banner workflow
on settle-site, conclusion success). Site source is GitHub Actions; dormancy
signal = age of newest signed Ledger commit on settle-ledger, read via public
API; banner injected at edge if > 30 days; no stored credentials, no commits.
Entry 12 closed.

## Entry 13 — 2026-10-03: apex settleverify.com not serving (2026-09-30 to 2026-10-03)

What happened: switching the site repository to the GitHub Actions source on
30 Sep broke serving of the apex. From 30 Sep to 2 Oct, https://settleverify.com/
failed at the TLS handshake (connection reset; no certificate offered). Only
www.settleverify.com served. All nine reviewer-recruitment email signatures
point at the bare domain. The 24 Sep checklist claim "apex live, 7/7" remains
true for 24 Sep — the 30 Sep switch broke it afterwards.

Why it was invisible for ~2 days: the post-deploy gate compared deployed bytes
against the previous deploy. It checked content, not hostnames. www passed, so
the gate passed. The framing error is in the gate, not the 24 Sep record.

Diagnosis (2 Oct): GitHub Pages had no vhost for the apex — the TLS reset
occurred before any certificate was offered. Pages settings showed
NotServedByPagesError; the DNS check never passed for the apex despite correct
A records (four 185.199.x.x, no AAAA, no CAA blocking issuance). The documented
Remove/re-add cycle was executed once; the check still failed at the one-hour
mark.

Resolution (2026-10-03 ~05:24 UTC): custom domain restored to
www.settleverify.com (GitHub serves www with its own certificate), and at
Cloudflare the four apex A records set to Proxied plus a Page Rule
settleverify.com/* -> 301 -> https://www.settleverify.com/$1 (path preserved).
The redirect executes at Cloudflare's edge and never contacts GitHub, so the
missing apex vhost is irrelevant. Verified live: apex / and /releases/ return
301 to the www equivalents; www returns 200; both handshakes hold valid
certificates. Inbound mail path verified unchanged (DMARC aggregate reports
continued arriving at the rua address through the change window).

Reviewer bounce, logged per protocol: on 2 Oct the reviewer ruled a fallback of
orange-clouding the apex to GitHub behind Cloudflare SSL/TLS "Full" mode.
Surface evidence (reset before any certificate was offered) showed GitHub's
edge offers no TLS for the apex at all; the fallback would have failed at the
origin handshake. The reviewer accepted the correction and substituted the
edge-redirect plan above. The bounce belongs to the reviewer; the surface
observation that caught it is recorded here.

Gate change, effective 2026-10-03: after any hosting or DNS change, verify BOTH
https://settleverify.com/ and https://www.settleverify.com/ return 200, or a
301 whose target returns 200, each with a valid certificate.

## Entry 14 — 2026-10-04 — v2 Flask gate boundary error: "unread interval between verified endpoints"

On 2026-09-15 this ledger and the draft settlement-gating note claimed the v2 Flask settle gate was 2xx-only for all releases `>= 2.0.0, < 2.15.0` and called the boundary map "exhaustive". The claim rested on read endpoints — 2.0.0, 2.10.0, and 2.15.0 — with the releases in between unread. In fact the gate widened to <400 at 2.11.0 (PR #2388, merged 2026-05-20); PR #2826 (2.15.0) fixed a main-branch regression of the same guard that did not reach a shipped release. Error class: unread interval between verified endpoints — the class the bounty all-files rule was written to prevent. Caught by the 2026-10-03/04 backlog verification, nineteen days after the claim.

Correction (4 Oct 2026): the v2 Flask settlement gate widened from 2xx-only to <400 at release 2.11.0 (PR #2388, merged 20 May 2026), not at 2.15.0 as previously stated; PR #2826 (2.15.0) fixed a main-branch regression of the same guard that did not reach a shipped release. Affected range for the 2xx-only Flask gate: >= 2.0.0, < 2.11.0. Verified wheel-by-wheel; see Ledger rows 2.11.0-2.15.0.

Errata applied in this push: rows 2.13.0, 2.13.1, 2.14.0 upgraded bracket-inferred -> verified (direct wheel read 2026-10-04); row 2.15.0 carries an appended erratum (row body unchanged); the same dated correction ships in scanner v0.3, upstream PR #3471 (settle-gating-tests branch), and the draft settlement-gating note (settle-gating-note branch). Remaining exposures per reviewer list: procurement checklist M1, report 001 citations, website Assessments/Home copy, x402-rs disclosure text.

## Entry 15 — 2026-10-08 — wave-two send count: intent recorded as completion
Claim: register entry of 29 Sep recorded "Wave two SENT… van Eeten, van Wegberg, Woods, Weaver, Savage" (5 sends). Surface: Gmail Sent shows 4 sends on 29 Sep; van Wegberg's ratified letter was never sent. Caught by the operator at the send surface during the 7 Oct nudge batch; corrected same day (original letter sent 7 Oct 13:17 MYT, delivery confirmed by recipient OOO auto-reply). Class: register-vs-surface — a plan recorded as a completed fact without a post-send surface check. Standing mitigation: register entries for sends are written from the Sent folder, not from the plan.

## Entry 15a — 2026-10-07 — reviewer-side pass-through (logged at the reviewer's own request)
The reviewer repeated "61% of transactions cut" from a 7 Oct paste without checking the arithmetic against figures in the same message (178.3M → 109.6M is 38.5% removed; 61% is the retained share). Class: SHOWN figure passed through unverified. Corrected in the memo v3.3 with the arithmetic shown. Logged against the reviewer per the mutual drift rule — the log is symmetric.
