**Status:** Frozen (see FREEZE.md)

# OWC Counterexamples

Canonical counterexamples and boundary constructions for OWC-style claims.

## Repo goals
- Store explicit witnesses (constructors + parameters)
- Provide verifiers that check a witness against a stated target property
- Keep results reproducible via CI

## Structure
- docs/ : specification + policy
- witnesses/ : explicit witness constructions
- verify/ : verification scripts + tests
- metrics/ : summaries produced by verification runs

## Quickstart
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -r requirements.txt
pytest -q
python verify/verify_witness.py witnesses/witness_0001/parameters.json
