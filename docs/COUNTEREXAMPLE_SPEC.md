# Counterexample Specification (OWC)

## Objects
- A "target property" P stated as a checkable predicate on a witness input.
- A "witness" W consisting of:
  - parameters.json (machine-readable)
  - description.md (human-readable)
  - generator (optional): generate.py or generate.lean

## Verification contract
A verifier must:
- accept a witness parameter file
- output a JSON result with fields:
  - witness_id
  - target_property
  - verdict ∈ {"PASS","FAIL","INCONCLUSIVE"}
  - evidence (free-form text / structured fields)
  - timestamp (ISO 8601)

## Classification
- boundary case: violates an auxiliary assumption while preserving the core statement form
- true counterexample: violates the stated target property under the stated assumptions

## Minimal acceptance for v0.1
- at least 1 witness folder with parameters.json + description.md
- 1 verifier script producing verify/results.json
- pytest covering: (i) schema sanity, (ii) deterministic output, (iii) exit codes
