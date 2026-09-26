# Settle 002 — Prediction Scoring vs Anchored Pre-Registration
**Compiled:** 24 Sep 2026 ~13:00 MYT · Evidence: settle-evidence @ cc8bdc0 (audit e027fad8…, twins ded05260…, v2own 9b05f5e1…, Day-1 c04679c line)
**Against:** 002-pre-registration-PREDICTIONS.md, anchored 17 Sep 2026, sha256 9de15c58…

## P1 — Per-probe error-reason mappings

| Probe | Predicted | Observed (v1 / v2) | Score |
|---|---|---|---|
| A1 garbage sig → /verify | `invalidFormat` or parser 400/422 (layer check) | 500 `unexpected_error` + ECRecover revert leak (both versions) | **REFUTED** — rejection happens at chain simulation, not parser; raw revert data leaked (FC-2/FC-3) |
| A2 garbage sig → /settle | same as A1 | 500 `unexpected_error` + ECRecover revert leak, 936ms, `hasTxHash: false`, zero on-chain effect (v2, 24 Sep) | **REFUTED** — rejection at chain simulation, not parser; settle path leaks and mislabels exactly like verify — confirms FC-3 on `/settle` (results-002-a2settle.json sha256 e41d8553…) |
| C3 wrong domain (8453) → /verify | `chainIdMismatch` or `invalidSignature` (reveals binding location) | 500 `unexpected_error` + FiatTokenV2 "invalid signature" leak (v1 V3; v2 T2) | **REFUTED** — no structured reason; binding enforced only by on-chain recovery. Port-map checkpoint (rejection in signature recovery vs earlier JSON validation): rejection IS in signature recovery ✓ probe tested the right property |
| C4 expired → /verify | `invalid_payment_expired` | 400 + exact enum reason, 2–3ms, local (v1 Day-1; v2 T3) | **CONFIRMED** — evaluated by facilitator, NOT passed to chain sim (port-map checkpoint ✓) |
| C5 low value → /verify | `invalid_payment_amount` | 400 + exact enum reason (v1 Day-1; v2 T4) | **CONFIRMED** — amount comparison in facilitator logic (port-map checkpoint ✓) |
| B5/R replay + race losers → /settle | OnchainFailure-class → 500 with `errorReason` | T5b: 500, `errorReason: unexpected_error` + "authorization is used or canceled" revert leak. Rejection confirmed; reason is generic, not a known-condition code | **CONFIRMED (status); reason-discrimination not achieved → FC-3** |

## P2 — Structural predictions

| # | Prediction | Score |
|---|---|---|
| 1 | x402.rs simulates at /verify | **CONFIRMED** — signature/nonce-class failures carry on-chain revert text in verify responses |
| 2 | Logical failures → 400 structured; on-chain → 500 | **CONFIRMED** — but 500s carry the FC-2 leak; the mapping is as predicted, the leak is the defect |
| 3 | Divergence from 001 (200+body vs 400+enum) | **CONFIRMED** — 400+structured enum observed for locally-evaluated failures; credit to x402.rs belongs in the report narrative, not this sheet |
| 4 | "001 Finding-1 analog: predicted NO direct analog exists" (001 Finding 1 = failure-signalling status split) | **REFUTED** — FC-3 IS the analog: locally-evaluable failures return structured 400s while signature/nonce-class failures route to chain simulation and surface as 500 `unexpected_error` + revert leak. Observed value: FC-3, both versions. (Note: the no-#3465-class-analog claim is separate — confirmed by T7's pre-broadcast refusal; it does not rescue this row's prediction.) |
| 5 | Permit2 inactive in exact config | **CONFIRMED** — all activity EIP-3009; Permit2 paths never observed |

## P3 — V1/V2 appendix

| # | Prediction/Rule | Score |
|---|---|---|
| 1 | Through-line: v2 settle gated; (a) no-verify and (b) failing-verify attempts refused before on-chain submission | **CONFIRMED** — T7 (expired, no verify): 400 in 3ms, no tx hash, no broadcast, zero delta. T6 (valid, no verify): 200 + tx + receipt — the control proving `/settle` re-validates independently and `/verify` is advisory. Settle-side gating per the #3465/#2826 fix class holds in x402-rs v2 |
| 2 | Twins only from three core classes, byte-identical except version | **PARTIAL** — failure-signalling twins (A1/C3/C4/C5) and verify/settle split (B5) executed under v2. Race (F2) twin not run: not observed under v2; expected from the shared settlement path (`provider.rs:303, 310–315, 320–323`; `config.rs:95–97`); status: inferred. Maintainer asked to confirm on reply. |
| 3 | Cross-routing watch: no payload version served by the other handler | **CONFIRMED** — no evidence of cross-routing; version dispatch is content-derived via `scheme_handler_slug`, all probes routed as constructed |

## P4 — Non-predictions (open items, no committed prior)

| Item | Outcome |
|---|---|
| Race-harness numerical results | FC-1 discovered here — **unpredicted**; own labelled section in report per Fable ruling. Rate 2/7 N=10, 0/8 N=1; mechanism: 30s receipt timeout → 500+null (source: provider.rs:303/310–323, config.rs:95–97, facilitator.rs:1059 @ e75adda) |
| /supported advertised-vs-accepted delta | **Closed, no delta** — v1 and v2 kinds accepted exactly as advertised once envelope is correct (v2own: strings matched, verify+settle 200) |
| GET-on-POST endpoints | Partially observed Day 1 (B3b 404 class); low value, observation only |
| README config-example drift | Not systematically checked in pinned image — recorded as unexecuted observation candidate |

## FC-1 — the headline, explicitly unpredicted
No P1–P4 entry predicted charged-without-delivery under concurrency. FC-1 stands in its own section, labelled as an unanticipated observation discovered by the pre-registered race harness and confirmed by reproduction, source read, and the independent on-chain census (audit rows 10–11: nonce consumed + payer debited while API reported failure).

## Port-map validation-day checkpoints — status
- A1 layer check ✓ (rejection at chain sim, not parser — recorded, that's the refutation)
- C3 rejection location ✓ (signature recovery)
- C4 evaluator location ✓ (facilitator-local)
- C5 comparison location ✓ (facilitator-local)
- B5/R revert-shape mapping ✓ (recorded; known-condition vs malfunction = FC-3)
- F2 stateless-verify ✓ (conformant, Day-1 V4/V5)
- Domain separator ✓ (verified on-chain, Day-1)
- /supported checkpoint ✓ (no advertised-not-accepted kinds after envelope fix)

## Open items before report (26–27 Sep)
1. ~~v2 race twin~~ RESOLVED (Fable 24 Sep): excluded, scored "inferred" with source citation; if maintainer replies, ask him to confirm v2 — stronger than a bench observation
2. ~~A2 direct probe~~ DONE 24 Sep: 500 + ECRecover leak, txHash false — row scored REFUTED (prediction refuted; observation confirms FC-3 on /settle, e41d8553…)
3. GET-on-POST + README drift — optional observations, report appendix only
4. Report checklist (from sheet, moved per Fable): credit x402.rs's structured-400 semantics near 001's remediation suggestion, with identical rigor — tone discipline; FC-1 section header must read "explicitly unpredicted"
