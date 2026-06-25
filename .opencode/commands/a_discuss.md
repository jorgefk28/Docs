---
description: Spec Discussion Workflow — analyze, debate, and resolve requirements, use cases, data models, or architecture decisions
---

# SPEC DISCUSSION WORKFLOW
You are running the **DISCUSS** workflow. Your goal is to take a requirements topic and produce a final resolved specification document through an adversarial process.

# Request
$ARGUMENTS

# Steps
1. **Write** — Invoke @spec_writer to produce a structured specification document in Markdown. Tell them exactly WHAT to document (e.g., "modelo de datos del subsistema de laboratorio", "casos de uso de gestión de turnos").

2. **Attack** — Invoke @spec_attacker with the document from step 1. They will return a numbered list of findings with severity.

3. **Defend** — Invoke @spec_defender with:
   - The original document (step 1)
   - The list of attacks (step 2)
   They will respond to each attack with ACCEPTED, REJECTED, or FLAG.

4. **Resolve** — Invoke @spec_tie_breaker with:
   - The original document (step 1)
   - The attacks (step 2)
   - The defenses (step 3)
   They will produce the final resolved version.

5. **Present** — Write the final resolved document to **OPENCODE-ARTIFACTS/** and present a summary to the user:
   - What changed from the original
   - How many attacks were accepted/rejected
   - The most important decisions made
