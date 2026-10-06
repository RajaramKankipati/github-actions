import os

for d in [".github/workflows", "src", "tests"]:
    os.makedirs(d, exist_ok=True)
open("src/__init__.py", "w").close()

print("\n".join(sorted(
    os.path.join(r, f)
    for r, _, fs in os.walk(".")
    for f in fs
    if not r.startswith("./.git/") and (r.startswith("./src") or r.startswith("./tests")
                                        or r.startswith("./.github"))
)))