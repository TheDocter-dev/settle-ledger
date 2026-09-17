# settle-ledger

A timestamped, append-only log of what the x402 Python SDK does at the payment-settlement boundary — verified release by release, against the published PyPI wheels.

PyPI attests what each wheel is (signed provenance, linked in every row). This log records what each wheel **does**: the exact settle-gate condition in both middleware adapters, so that a change at the settlement boundary is never silent.

## What each row contains

Every release gets a row in `releases/`, within 24 hours of the release appearing on PyPI. Fixed schema, no free text:

- `artifact_date` — when PyPI published the wheel
- `logged_at` — when we verified and recorded it (these differ on retroactive rows; the gap is stated, never hidden)
- `basis` — how the row was verified
- `wheel_sha256` — digest of the exact artifact checked
- `pypi_provenance` — link to PyPI's own signed attestation for that wheel
- `flask_settle_gate` / `fastapi_settle_gate` — the settle-gate condition, with file and line
- `status` — the operational bottom line

If a row says nothing is operator-facing, that means the wheel was pulled and diffed and nothing was found — silence here is a verified result, not an absence. If a release has not yet been verified, its row says `status: pending — not yet verified` rather than being absent.

## Integrity

Entries are GitHub-verified commits on a protected branch (`main`: force-push disabled, signed commits required). History can grow; it cannot be rewritten — including by us. Mirroring entry hashes to a public transparency log (Sigstore Rekor) is on the upgrade path.

## What this log is not

- Not a vulnerability feed. It records gate conditions and cites public issues (e.g. x402-foundation/x402#3465); it does not label releases.
- Not a grading service. No project, facilitator, or merchant is rated here. `dependents/` records pin *movement* in public libraries only — never named payment parties, never joined against the release feed.
- Not affiliated with or endorsed by the x402 Foundation or Coinbase.

## Method

See `METHOD.md`. Independent re-verification of any row: pull the named wheel from PyPI, read the cited file and line. Ten minutes, no trust required.

## Citing

Link the row file directly, e.g. `releases/2.22.0.md`. Each row is a permanent commit on an append-only branch.

## Signing key

Ledger entries and assessment anchors are signed with the Settle Ledger key:

```
ed25519  3C15C334 A2063681 67FB90C8 5324071C CD3C0642
Created 17 Sep 2026, expires 2028-09-16.
```

Verify any signed anchor: `gpg --verify <file>.asc`. If this key is ever rotated, the rotation notice is itself signed by the old key and committed here before the new key signs anything.

## Assessment anchors

`anchors/` holds the hash anchors for Settle conformance assessment reports — one entry per assessment, committed BEFORE or AT the report's publication, each with an OpenTimestamps proof (`.ots`) committed beside it so the hash's existence is anchored in Bitcoin independently of GitHub.

- `anchors/002-pre-registration.md` — 002 (x402-rs) predictions locked before execution (committed 17 Sep, before first probe)

## Licence

Ledger entries and anchors: CC-BY-4.0 (see LICENSE).
