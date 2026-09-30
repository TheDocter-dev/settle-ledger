#!/usr/bin/env python3
"""
Settle PyPI release poll v2 — detects new x402 SDK releases and writes a
'pending — not yet verified' row within 24h. Rows carry automatable fields
(version, artifact_date, wheel, wheel_sha256, pypi_provenance); the
settle-gate verdict is manual. No git operations in this job.
"""
import json, os, time, urllib.request

PKG = "x402"
LEDGER = os.path.dirname(os.path.abspath(__file__))
REL = os.path.join(LEDGER, "releases")
LOG = os.path.join(LEDGER, "poll-pypi.log")

def log(msg):
    line = f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {msg}"
    with open(LOG, "a") as f:
        f.write(line + "\n")
    print(line)

def main():
    with urllib.request.urlopen(f"https://pypi.org/pypi/{PKG}/json", timeout=30) as r:
        data = json.load(r)
    existing = {f[:-3] for f in os.listdir(REL) if f.endswith(".md")}
    found = False
    for ver, files in sorted(data["releases"].items()):
        if not files or ver in existing:
            continue
        files = sorted(files, key=lambda x: x["upload_time"])
        first = files[0]
        artifact = first["upload_time"][:10]
        wheel = first["filename"]
        sha = first.get("digests", {}).get("sha256", "(sha256 not provided by index)")
        row = f"""---
version: {ver}
artifact_date: {artifact}
logged_at: {time.strftime('%Y-%m-%d', time.gmtime())}
basis: automated detection via PyPI JSON release-list poll (poll-pypi.py); settle-gate verification pending
wheel: {wheel}
wheel_sha256: {sha}
pypi_provenance: https://pypi.org/integrity/{PKG}/{ver}/{wheel}/provenance
flask_settle_gate: (pending)
fastapi_settle_gate: (pending)
status: pending — not yet verified
---"""
        with open(os.path.join(REL, f"{ver}.md"), "w") as f:
            f.write(row + "\n")
        log(f"NEW RELEASE DETECTED: {ver} (artifact {artifact}) — pending row written")
        found = True
    if not found:
        log("no new releases")

if __name__ == "__main__":
    main()
