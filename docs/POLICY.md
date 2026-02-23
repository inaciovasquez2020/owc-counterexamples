# Policy

## Scope
This repository contains adversarial examples, boundary constructions, and verification harnesses.

## Non-goals
- No edits to upstream core statements are performed here.
- No claims of refutation beyond the stated target_property for each witness.

## Reproducibility
- All verifiers must run non-interactively.
- CI must execute the verifier on the canonical witness set.

## Classification requirement
Every witness MUST include CLASSIFICATION.md declaring:
- boundary vs counterexample
- scope of violation
- whether core claims are affected
