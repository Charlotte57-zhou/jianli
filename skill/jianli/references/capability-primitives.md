# Capability Primitive Library

## Purpose

Capability primitives describe repeatable work behaviors below job titles and above personality labels. They are not JD keywords and do not prove themselves. Each primitive must point to concrete episodes, evidence, ownership level, and boundaries.

## Primitives

### `complex_workflow_decomposition`

- **Definition:** Decompose a rule-dense process into actors, stages, decisions, exceptions, and outputs.
- **Observable behavior:** Draws the real flow, identifies branches/non-goals, and assigns owners.
- **Typical evidence:** workflow map, state model, PRD, exception list, acceptance cases.
- **Common miswrite:** “逻辑能力强” or “擅长复杂问题.”
- **Transfers to:** enterprise operations, finance, compliance, support, supply-chain workflows.
- **Role mapping:** PM/BA/AI PM/Project roles weight different artifacts; the primitive stays unchanged.

### `relation_boundary_state_modeling`

- **Definition:** Model entities, relationships, system boundaries, state transitions, and ownership.
- **Observable behavior:** Separates employer/client/platform/module/contribution and defines valid transitions.
- **Typical evidence:** domain model, schema, lifecycle, state machine, responsibility matrix.
- **Common miswrite:** “负责系统架构” without scope.
- **Transfers to:** platform products, data governance, workflow engines, Agent state management.
- **Role mapping:** technical roles emphasize implementation; product roles emphasize contract and decision ownership.

### `anomaly_inconsistency_detection`

- **Definition:** Detect contradictions, missing evidence, invalid states, or cross-source mismatch.
- **Observable behavior:** Finds where data or behavior diverges from an explicit invariant.
- **Typical evidence:** Bad Cases, reconciliation rules, defect examples, diagnostic queries.
- **Common miswrite:** “洞察力强” or “容易发现问题.”
- **Transfers to:** quality, risk, audit, analytics, operations, AI reliability.
- **Role mapping:** map to the target role's anomaly consequence, not a generic trait.

### `closure_validation`

- **Definition:** Verify that an issue moves from detection through ownership, action, recheck, and durable closure.
- **Observable behavior:** Defines done, rechecks outcomes, and prevents silent open loops.
- **Typical evidence:** acceptance criteria, regression tests, lifecycle records, closure metrics.
- **Common miswrite:** “责任心强.”
- **Transfers to:** delivery, incident management, customer support, financial exceptions, Agent remediation.
- **Role mapping:** PM emphasizes acceptance; project roles emphasize owner/SLA; engineering emphasizes regression.

### `business_product_technology_translation`

- **Definition:** Translate business consequences into product contracts and technical constraints in both directions.
- **Observable behavior:** Makes jargon reviewable, surfaces trade-offs, and preserves decision meaning.
- **Typical evidence:** PRD, interface contract, decision note, stakeholder review, readable architecture.
- **Common miswrite:** “沟通能力强.”
- **Transfers to:** B2B products, solution roles, FDE, technical PM, AI PM.
- **Role mapping:** choose evidence that matches the target evaluator's decision.

### `data_source_and_ownership_reasoning`

- **Definition:** Determine where a value came from, who owns it, what it measures, and what it cannot prove.
- **Observable behavior:** Separates public/internal/estimated data and resolves system or metric attribution.
- **Typical evidence:** lineage, metric definition, source mapping, fact matrix, ownership correction.
- **Common miswrite:** attributing platform-scale data or inferred ROI to a module.
- **Transfers to:** analytics, data products, finance, compliance, evaluation governance.
- **Role mapping:** Role Packs may prioritize different metrics but cannot relax source boundaries.

### `ai_native_product_building`

- **Definition:** Use AI tools to move from product intent to a runnable, inspectable artifact with explicit acceptance.
- **Observable behavior:** Specifies tasks, reviews changes, modifies behavior, debugs failures, and validates output.
- **Typical evidence:** runnable demo, commits, issue traces, tests, acceptance notes.
- **Common miswrite:** “独立全栈开发” based only on generated output.
- **Transfers to:** AI PM, prototyping, internal tools, workflow automation.
- **Role mapping:** engineering claims require stronger code ownership than product-building claims.

### `evaluation_and_bad_case_design`

- **Definition:** Turn desired behavior and failure consequences into cases, labels, metrics, gates, and iterations.
- **Observable behavior:** Defines denominators, separates model result from routing, and traces Bad Case ownership.
- **Typical evidence:** Eval set, rubric, regression report, failure taxonomy, gate decision.
- **Common miswrite:** “模型准确率高” without protocol or denominator.
- **Transfers to:** AI products, quality systems, experimentation, policy workflows.
- **Role mapping:** AI PM emphasizes decision usefulness; engineering may emphasize harness reliability.

### `cross_system_coordination`

- **Definition:** Coordinate contracts, dependencies, owners, and acceptance across systems or teams.
- **Observable behavior:** Identifies interface owners, resolves sequence conflicts, and closes cross-boundary issues.
- **Typical evidence:** interface map, dependency plan, decision log, delivery record.
- **Common miswrite:** “跨部门沟通能力强.”
- **Transfers to:** enterprise delivery, platforms, integrations, operations.
- **Role mapping:** distinguish coordination from authority over every system.

### `evidence_based_iteration`

- **Definition:** Change the smallest responsible owner based on observed evidence and verify the result.
- **Observable behavior:** Preserves baseline, identifies root cause, changes one owner, and reruns focused checks.
- **Typical evidence:** before/after artifact, test result, Bad Case fix, decision log.
- **Common miswrite:** “快速迭代” without evidence or learning.
- **Transfers to:** product discovery, AI behavior, quality, growth, operations.
- **Role mapping:** select the evidence tier relevant to the target role; do not upgrade regression into production outcome.

## Usage rules

1. Start from episodes, not from selecting attractive primitive names.
2. Require at least one strong episode; prefer two independent episodes before calling a pattern stable.
3. Record counterevidence and conditions where the primitive does not hold.
4. Map a primitive to a Role Pack only after ownership and evidence are recorded.
5. Keep direct similarity ahead of primitive-based transferability.
