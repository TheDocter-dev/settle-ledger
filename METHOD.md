# METHOD

How every settle-ledger row is produced and how to re-verify it independently.

## Scope

The x402 Python SDK ships exactly two HTTP middleware adapters (Flask, FastAPI). Each has a single settle-gate: the condition on the HTTP response status under which a verified payment is settled. The log records that condition, per release, for both adapters.

## Procedure per release

1. Download the wheel from PyPI (`bdist_wheel` artifact only — never mirrors, forks, or checkouts).
2. Record the sha256 digest and confirm it matches PyPI's published digest.
3. Extract `x402/http/middleware/flask.py` and `x402/http/middleware/fastapi.py` (v2 paths; v1 paths differ and are noted in the row).
4. Read the settle-gate condition and its line number(s) in each adapter.
5. Write the row with the fixed schema. No fields may be added ad hoc; schema changes are their own logged commit.

## Two-date discipline

- `artifact_date`: the PyPI upload timestamp (PyPI's record, linked via `pypi_provenance`).
- `logged_at`: the date the row was verified and committed.
- Rows logged after their release date carry `basis: retroactive verification against the published wheel`. The gap between the two dates is always visible.

## Cadence and the 24-hour rule

New releases are diffed and rowed within 24 hours of appearing on PyPI. If verification cannot complete in that window, a row is committed with `status: pending — not yet verified` and updated in place (new commit) when done. A missing row is a process failure; a pending row is an honest one.

## Guardrails (mechanical, not aspirational)

- Facts and citations only. No severity labels, no "vulnerable", no interpretive prose — the schema has no field for them.
- Affected-range references cite the public issue (x402-foundation/x402#3465) and the fixing PR (#2826), nothing more.
- The dependents feed records pin movement in public SDKs/libraries only. Facilitators and merchants are never listed. Pins are never resolved against the release feed inside this repo.
- Findings about new releases go upstream (x402-foundation/x402 issue tracker) before any public commentary.

## Independent re-verification

1. `pip download x402==<version> --no-deps` (or fetch the wheel URL from `pypi.org/pypi/x402/<version>/json`).
2. `sha256sum` the wheel; compare with the row.
3. Unzip; open the cited file at the cited line; read the gate condition.

If any row fails this check, open an issue on this repository — a wrong row is a defect, and correcting it publicly is the design.
