import json
import subprocess
from pathlib import Path

def test_verifier_produces_results_json(tmp_path):
    repo_root = Path(__file__).resolve().parents[2]
    params = repo_root / "witnesses" / "witness_0001" / "parameters.json"
    assert params.exists()

    p = subprocess.run(
        ["python", str(repo_root / "verify" / "verify_witness.py"), str(params)],
        cwd=str(repo_root),
        capture_output=True,
        text=True
    )
    assert p.returncode == 0
    results = repo_root / "verify" / "results.json"
    assert results.exists()
    obj = json.loads(results.read_text(encoding="utf-8"))
    assert obj["witness_id"] == "witness_0001"
    assert obj["verdict"] in ("PASS", "FAIL", "INCONCLUSIVE")
