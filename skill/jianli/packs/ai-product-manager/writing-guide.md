# AI Product Manager — Writing Guide

## Two-layer communication

### Layer 1 — Recruiter-readable

Answer:

- Who has the problem?
- What is the problem?
- What does AI do?
- What remains rule-based or human-controlled?
- What did the candidate deliver?
- How was it validated?

### Layer 2 — Technical proof

Then add:

- Agent;
- Tool Calling;
- MCP;
- Human-in-the-loop;
- Eval;
- SDK;
- architecture;
- failure handling.

## Example

Weak:

> Built an Agent Harness with MCP and Eval.

Better:

> Designed an AI exception-handling workflow for finance users who previously had to investigate issues across several systems. Stable cases remain rule-based; the Agent gathers cross-system evidence and produces reviewable correction suggestions for ambiguous exceptions, with human confirmation before high-risk actions.

Technical proof:

> Implemented tool-based investigation, Human-in-the-loop controls, structured outputs and offline Eval / Bad Case regression.

## Product judgment matters more than jargon

A strong AI PM bullet demonstrates decisions such as:

- why not use the model for every case;
- why a human confirms a write action;
- what counts as success;
- what happens when evidence is incomplete;
- how failure is surfaced.

## Personal AI projects

A personal project is valid evidence when it has:

- real problem definition;
- runnable product or prototype;
- meaningful architecture;
- evaluation/testing;
- clear boundaries.

Do not imply production use, customers, revenue, or accuracy that does not exist.
