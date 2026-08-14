# Core Architecture

## The product model

Jianli treats resume optimization as a small evidence system rather than a one-shot writing task.

```text
Career Evidence Base
├── Facts
├── Metrics
├── Artifacts
├── Bullet Library
└── Capability Library
        ↓
Master Resume
        ↓
Role Profile / Role Pack
        ↓
JD Match
        ↓
Tailored Resume
        ↓
Interview Evidence
```

## Why this architecture

The same career history can support different truthful narratives.

Example:

One enterprise integration project may support:

- a Product Manager resume through requirement and product ownership;
- a Project Manager resume through coordination and delivery;
- a Business Analyst resume through process and data modeling;
- a Technical Product resume through interfaces and system constraints.

The facts remain the same.

The **view changes**.

## Core vs Role Pack

### Core owns

- truth;
- evidence classes;
- JD matching;
- transferable capabilities;
- quantification;
- information architecture;
- versioning;
- project hierarchy;
- interview defensibility.

### Role Pack owns

- role-specific hiring dimensions;
- market vocabulary;
- which evidence tends to matter most;
- portfolio strategy;
- role-specific bullet patterns;
- red flags;
- examples.

Role packs cannot relax core integrity rules.

## Master vs tailored

The Master Resume is not “the one perfect resume.”

It is a structured evidence inventory.

A tailored resume is a role-specific projection of that inventory.

## Design objective

The system should make it easy to answer:

1. What did this person actually do?
2. What capabilities does that prove?
3. Which of those capabilities matter here?
4. What should be surfaced for this JD?
5. Can every visible claim survive an interview?
