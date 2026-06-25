---
description: Research codebase and produce architecture decisions for a feature or change
---

# SPEC_OUT WORKFLOW
You are running the **SPEC_OUT** workflow. Your goal is to understand the request, explore the relevant code, and produce a spec document.
This document contains relevant references to the codebase, pseudo code, diagrams and detailed specifications for a developer to pick up later; with all the architecture considerations needed.

# Request
$ARGUMENTS

# Steps
1. **Explore** — Invoke @deep_diver with specific files, keywords, or patterns related to the request.
Collect findings: relevant files, existing implementations, dependencies, and conventions in use.
Go back and forth until you have all the context required.

2. **Write** — produce **OPENCODE-ARTIFACTS/DECISIONS.md** in root containing:
  - Summary of the change and its scope.
  - Architecture decisions with rationale.
  - Pseudo code or interface contracts for complex parts.
  - Alternatives considered (if any) with trade-offs.
Create this spec file YOURSELF.

3. **Present** — Show DECISIONS.md to the user for review. Ask if anything needs refinement.
