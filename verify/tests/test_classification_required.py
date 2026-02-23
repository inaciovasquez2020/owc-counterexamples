from pathlib import Path

def test_all_witnesses_are_classified():
    wdir = Path("witnesses")
    for w in wdir.iterdir():
        if w.is_dir():
            assert (w / "CLASSIFICATION.md").exists(), f"{w.name} missing CLASSIFICATION.md"
