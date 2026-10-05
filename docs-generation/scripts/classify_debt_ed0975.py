#!/usr/bin/env python3
"""Classify ed0975a95 en.md changes: Required Yes->No flips vs description drift."""
import subprocess, re, json, sys

REPO = "/Users/linmoumou/Documents/embedded-docs"
diff = subprocess.run(
    ["git", "diff", "ed0975a95^", "ed0975a95", "--", "comfyui_embedded_docs/docs/*/en.md"],
    cwd=REPO, capture_output=True, text=True).stdout

ROW = re.compile(r'^\| `[^`]+` \| .*\| [A-Z_]+ \| (Yes|No) \|')
file_stat = {}
cur = None

def bump(f, kind):
    file_stat.setdefault(f, {"flip": 0, "footer": 0, "other": 0})[kind] += 1

for l in diff.splitlines():
    m = re.match(r"diff --git a/(\S+) b/", l)
    if m:
        cur = m.group(1)
        continue
    if cur is None:
        continue
    if not (l.startswith("-") or l.startswith("+")) or l.startswith("---") or l.startswith("+++"):
        continue
    body = l[1:]
    if "Source fingerprint" in body:
        bump(cur, "footer")
        continue
    if ROW.match(body):
        bump(cur, "flip")
        continue
    bump(cur, "other")

flip_files = {f: d["flip"] for f, d in file_stat.items() if d["flip"]}
other_files = {f: d["other"] for f, d in file_stat.items() if d["other"]}
# A file needs translation sync if it has any content change beyond pure fingerprint churn
drift_files = {f: d["other"] for f, d in file_stat.items() if d["other"]}

print(f"total en.md files in diff: {len(file_stat)}")
print(f"files with Required flips: {len(flip_files)}, flip lines (en): {sum(flip_files.values())}")
print(f"files with description/overview drift: {len(drift_files)}, drift lines (en): {sum(drift_files.values())}")

# drift nodes list (dir names)
drift_nodes = sorted(f.split("/")[2] for f in drift_files)
flip_nodes = sorted(f.split("/")[2] for f in flip_files)
with open("/tmp/drift_nodes.json", "w") as fp:
    json.dump({"nodes": drift_nodes}, fp)
with open("/tmp/flip_nodes.json", "w") as fp:
    json.dump({"nodes": flip_nodes, "files": flip_files}, fp)
print("drift nodes:", drift_nodes)
print("flip-only nodes (no drift):", sorted(set(flip_nodes) - set(drift_nodes)))
