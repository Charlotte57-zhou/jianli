# AI Product Manager — Keyword and Claim Gate

This is not a keyword-stuffing list. Use a term only when the candidate can explain its role, boundary, evidence, ownership and maturity.

| Term | Required meaning | Evidence gate | Ownership / maturity boundary |
|---|---|---|---|
| LLM | model materially affects product behavior | actual interaction or design evidence | explain limitations and failure handling |
| Agent | model investigates/plans/uses tools across uncertain steps | concrete Agent loop and tool/action boundary | explain why Agent exists and what remains deterministic |
| Workflow | multi-step product/business flow | actual state or flow design | do not imply Agent autonomy |
| Tool Calling | model invokes external capability | tool/API contract and result handling | separate design from implementation ownership |
| RAG | retrieval augments model context | real retrieval pipeline | no term from JD without evidence |
| MCP | MCP materially used in implementation | server/tool contract or runtime evidence | state personal scope |
| Human-in-the-loop | human owns a defined review/approval point | explicit state, consequence and owner | not a decorative fallback phrase |
| Eval | systematic decision-linked evaluation | cases, labels, denominator, metrics and gates | Offline Eval is not real-user validation |
| Bad Case | failure reconstructed to an owner | raw example, expected behavior and regression | do not count anecdotes as a complete taxonomy |
| POC / Demo | runnable proof of concept | inspectable artifact and core path | no production or customer implication |
| AI Coding | AI agent materially supports implementation | Explain/Modify/Debug/Reproduce/Validate audit | default to AI-native product building, not full-stack |
| 0→1 | candidate helped define and deliver a new capability | exact scope and before/after state | module 0→1 is not platform 0→1 |
| Production | supported live workflow | deployment/operation evidence and scope | does not prove personal L5 ownership alone |
| Business Outcome | measured attributable result | baseline, denominator, period and attribution | strongest maturity gate |

Showing where AI is **not** used is often a stronger product signal than adding another AI keyword.

## Placement order

1. problem and consequence;
2. product decision and why AI;
3. deterministic versus uncertain boundary;
4. human control and failure handling;
5. validation and evidence;
6. supported technical terms.

Keywords improve retrieval only after the recruiter can understand what the candidate solved.
