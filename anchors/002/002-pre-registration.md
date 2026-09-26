# Settle 002 Pre-Registration — Predictions Locked Before Execution

**Subject:** x402-rs facilitator, pinned image `ghcr.io/x402-rs/x402-facilitator@sha256:4ebe09d824bf6a5f342add8ae22eb44a2c56894ad22e7d3f5b83ba38023226b9`, self-hosted VPS localhost:8080, Base Sepolia (eip155:84532).
**Locked:** 17 Sep 2026, before any probe execution against the subject.
**Source of predictions:** assessment-002-probe-port-map.md (16 Sep) + x402.rs source read (handlers.rs, proto/mod.rs ErrorReason enum; no contact with any running instance).
**Purpose:** these predictions are hashed and anchored in the Settle Ledger BEFORE execution day. Confirmations and refutations are both reportable. A prediction that fails is not embarrassment — it is the method working in public. This document exists so that no 002 finding can be accused of being retrofitted to observations.

## P1 — Per-probe error-reason mappings (predicted, confirm on validation day)

| Probe | Defect | Predicted invalidReason | Prediction basis |
|---|---|---|---|
| A1 | Unparseable signature bytes → /verify | `invalidFormat` OR a 400/422 from the axum JSON layer (parser-level, distinct layer from 001's 500) | ErrorReason enum + axum handler structure |
| A2 | Same → /settle | Same as A1 | Same |
| C3 | Wrong domain chainId (8453) | `chainIdMismatch` OR `invalidSignature` — which one reveals WHERE binding is checked | Enum has both variants |
| C4 | Expired authorization | `invalidPaymentExpired` | Enum variant exists; twin available: not-yet-valid → `invalidPaymentEarly` |
| C5 | Value below requirement | `invalidPaymentAmount` | Enum variant exists |
| B5/R | Consumed-nonce replay + race losers → /settle | OnchainFailure-class → 500 with `errorReason`; known-condition vs malfunction signaling to be mapped | Status mapping: OnchainFailure → 500 |

## P2 — Structural predictions

1. **Verify depth:** x402.rs SIMULATES transactions at /verify (basis: `TransactionSimulation` ErrorReason variant exists). Faremeter did not. If confirmed: reported as a conformance-spectrum difference with security-relevant trade-offs (catches unfunded payers at verify; costs RPC load per verify) — NOT a finding against either implementation; the spec permits both.
2. **Status semantics:** logical verification failures → 400 with structured enum reason (except insufficient allowance → 412); on-chain failures → 500. Basis: handler doc comments + error-type mapping in source.
3. **Predicted divergence from 001:** Faremeter returned 200-with-isValid:false for logical failures and 500 for parse errors; x402.rs is predicted to return 400 + structured reason for logical failures and reserve 500 for on-chain. If confirmed, the report MUST state plainly that x402.rs implements structured failure semantics close to 001's own remediation suggestion. Tone discipline: identical rigor, no credit withheld, no inflation.
4. **001 Finding-1 analog:** predicted NO direct analog exists; the comparable claim becomes a cross-implementation semantics comparison (200+body vs 400+enum vs 412) — a conformance-spectrum observation, not a defect, unless spec text says otherwise. DO NOT force a finding to match 001's shape.
5. **Permit2 paths:** inactive in our exact-scheme config (predicted); `permit2AllowanceRequired` + 412 mapping noted as deliberate allowance semantics, observed only if reachable.

## P3 — V1/V2 appendix predictions (Fable point-4 locked rules)

1. **Through-line probe:** v2 handler gates settlement — /settle with (a) no prior /verify, (b) failing-verify payload → refusal BEFORE any on-chain submission (2.15.0 / PR #2826 behavior). Ties 002 to Settle's founding finding (#3465).
2. Twins only from three core classes (failure signalling A1/A2/C3/C4/C5; verify/settle split B5/R; race F2); each twin byte-identical except payload version + handler; anything not buildable that way is EXCLUDED — predicted exclusion risk: none identified pre-execution.
3. **Cross-routing watch:** does one payload version ever get served by the other handler? Predicted: no. If yes: divergence finding.

## P4 — Non-predictions (explicitly open, no prior committed)

- Race-harness numerical results (invariant: deliveries = settlements × value)
- /supported advertised-vs-accepted delta (both v1+v2 confirmed live at /health)
- GET-on-POST-endpoints behavior (schema-info responses expected; harmless observation candidate)
- README config-example drift in pinned image (observation candidate)

## Anchoring

- This file's SHA-256 is recorded in the Settle Ledger on 17 Sep 2026 with the Ledger signing key (fingerprint published in Ledger README).
- Post-execution, the 002 report cites this document per prediction: CONFIRMED / REFUTED / PARTIAL, with evidence pointers.
