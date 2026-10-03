#!/usr/bin/env python3
"""
Settle PyPI release poll v4 — runs as settlecat. Detects new x402 SDK releases;
writes pending rows to a settlecat-owned staging dir (never into the Ledger clone);
opens a timestamped public issue via the issues:write-only token in settlecat's home.
Rows reach the public Ledger via the human signed-commit step (copy, review, sign, push).
"""
import json, os, time, urllib.request

PKG = "x402"
REPO = "TheDocter-dev/settle-ledger"
STAGING = "/home/settlecat/poll-staging/releases"
LEDGER_RELEASES = "/root/settle-ledger/releases"
LOG = "/home/settlecat/poll-staging/poll-pypi.log"
TOKEN_FILE = os.path.expanduser("~settlecat/.poll-issue-token")

def log(msg):
    line = f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {msg}"
    with open(LOG, "a") as f:
        f.write(line + "\n")
    print(line)

def open_issue(ver, artifact, wheel, sha):
    if not os.path.exists(TOKEN_FILE):
        log(f"{ver}: issue NOT opened — token absent; staged row only")
        return False
    token = open(TOKEN_FILE).read().strip()
    if not token:
        log(f"{ver}: issue NOT opened — token empty; staged row only")
        return False
    body = {
        "title": f"Release detected: x402 {ver} (published {artifact})",
        "body": ("Automated detection by poll-pypi.py (settlecat). Public detection record; "
                 "the signed Ledger row follows in the next human commit cycle.\n\n"
                 f"- version: {ver}\n- artifact_date: {artifact}\n- wheel: {wheel}\n"
                 f"- wheel_sha256: {sha}\n- provenance: https://pypi.org/integrity/{PKG}/{ver}/{wheel}/provenance\n\n"
                 "status: pending — not yet verified"),
        "labels": ["release-detection"]
    }
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/issues",
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {token}",
                 "Accept": "application/vnd.github+json",
                 "User-Agent": "SettlePoll/4.0"},
        method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            log(f"{ver}: issue opened {json.load(r)['html_url']}")
            return True
    except Exception as e:
        log(f"{ver}: issue FAILED ({type(e).__name__}) — staged row only; retry next run")
        return False

def main():
    with urllib.request.urlopen(f"https://pypi.org/pypi/{PKG}/json", timeout=30) as r:
        data = json.load(r)
    existing = {f[:-3] for f in os.listdir(LEDGER_RELEASES) if f.endswith(".md")}
    existing |= {f[:-3] for f in os.listdir(STAGING) if f.endswith(".md")}
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
basis: automated detection via PyPI JSON release-list poll (poll-pypi.py, settlecat); settle-gate verification pending
wheel: {wheel}
wheel_sha256: {sha}
pypi_provenance: https://pypi.org/integrity/{PKG}/{ver}/{wheel}/provenance
flask_settle_gate: (pending)
fastapi_settle_gate: (pending)
status: pending — not yet verified
---"""
        with open(os.path.join(STAGING, f"{ver}.md"), "w") as f:
            f.write(row + "\n")
        log(f"NEW RELEASE DETECTED: {ver} (artifact {artifact}) — staged")
        open_issue(ver, artifact, wheel, sha)
        found = True
    if not found:
        log("no new releases")

if __name__ == "__main__":
    main()
