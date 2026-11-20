import sys
sys.path.insert(0, r'C:\Users\pc\Documents\M1\IACS\Project_EthicalHacking\aegis-p10-deepfake-light')
from src import deepfake_light_main as m
import json

# Test smoke
out = m.smoke("x", "y")
assert out["ok"] is True
assert out["project"] == "P10"
print("PASS: smoke test")

# Test main returns 0
ret = m.main([])
assert ret == 0
print("PASS: main([]) returns 0")

# Test main --json
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()) as buf:
    ret = m.main(["--json"])
data = json.loads(buf.getvalue())
assert data["project"] == "P10"
print("PASS: main --json outputs project=P10")

print("\nAll P10 tests passed!")