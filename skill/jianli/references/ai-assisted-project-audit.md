# AI-Assisted Project Audit

## Core rule

> AI generated output is not automatically a candidate capability asset.

Audit Codex, Claude Code, Cursor, Copilot, or other AI-assisted projects through the candidate's observable control of the work.

## Audit sequence

```text
Explain → Modify → Debug → Reproduce without prepared notes → Validate
```

### 1. Explain

Ask the candidate to explain:

- the user and problem;
- why the design was chosen;
- the core data and control flow;
- the candidate's own decisions;
- what AI generated versus what the candidate specified or corrected.

### 2. Modify

Find one material change the candidate personally made:

- behavior or requirement changed;
- key implementation or configuration changed;
- contract, state, prompt, tool, schema, or UI was revised;
- acceptance criteria were updated.

### 3. Debug

Require one reconstructable failure episode:

- symptom and expected behavior;
- evidence inspected;
- earliest failure owner;
- change made;
- regression or recheck.

### 4. Reproduce

Check whether the candidate can rebuild or demonstrate the core path without copying a prepared walkthrough. Reproduction can be product-level rather than full code reimplementation, but the boundary must be explicit.

### 5. Validate

Record what was actually validated: syntax, tests, runnable demo, offline Eval, expert review, pilot, production, or measured outcome. Do not collapse these stages.

## Project explanation-right gate

For every important AI project, require defensible answers to:

1. Why was it designed this way?
2. Why not use another approach?
3. What is the core data flow?
4. Why does an Agent exist?
5. What belongs to Rule, Workflow, Agent, and Human?
6. What is the success metric?
7. What happens on failure or missing evidence?
8. What is the core call chain?
9. What are the main Bad Cases?

If the candidate cannot answer the questions relevant to the claim, output:

> 先补项目解释权，不要继续强化简历 claim。

Then downgrade the wording or create a capability-gap action. Do not coach a memorized answer and immediately treat it as ownership evidence.

## Required synchronization

Write the audit result into:

- Fact Matrix — evidence, AI contribution, ownership and maturity;
- Capability Library — proven primitive, ownership level and boundary;
- Claim Defensibility Matrix — wording and interview risk;
- Interview Evidence Card — explanation, debugging, alternatives and failure handling;
- Final Resume Audit — no claim exceeds ownership or validation maturity;
- relevant Role Pack — role-specific interpretation only.
