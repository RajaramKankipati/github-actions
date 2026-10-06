import json
import subprocess

def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(r.stdout[-3000:])
    if r.returncode != 0:
        print(r.stderr[-2000:])
    print(f"[exit code {r.returncode}]")
    return r


# run("python -m pytest tests/test_data.py -q")
# run("python -m src.train")
# run("python -m pytest tests/test_model.py -q")


protection = {
    "required_status_checks": {"strict": True, "contexts": ["test-and-gate"]},
    "enforce_admins": False,
    "required_pull_request_reviews": {"required_approving_review_count": 1},
    "restrictions": None,
}
with open("protection.json", "w") as f:
    json.dump(protection, f)

run("gh api -X PUT repos/:owner/:repo/branches/main/protection --input protection.json")
run("gh api repos/:owner/:repo/branches/main/protection/required_status_checks")