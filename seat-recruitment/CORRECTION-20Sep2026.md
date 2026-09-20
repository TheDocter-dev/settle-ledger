# Correction — date error in 623c811
Commit 623c811 ("seat: anchor wave-1 send-time record") is dated 21 Sep 2026.
Actual date of the events it records (mailbox auth, mail-tester gate, warm-up,
pool/criteria hashing): 20 Sep 2026 (MYT, UTC+8). The error originated in a
session-summary date drift and was propagated, not a falsification of events.
Per append-only rule, 623c811 is NOT rewritten; this commit is the correction.
All downstream records carry both the erroneous label and this correction.
