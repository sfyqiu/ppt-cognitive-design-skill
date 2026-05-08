# Requirement Parser Engine

The requirement parser is the entrance of the presentation intelligence system.

Its responsibility is to transform vague user requests into structured presentation parameters.

---

# Core Objective

Convert:

raw user intention

into:

structured presentation reasoning signals.

---

# Required Parsing Dimensions

## 1. Presentation Scenario

Infer:

- teaching interview
- undergraduate lecture
- academic defense
- conference presentation
- business pitch
- project report
- scientific storytelling
- technical training

Scenario determines:

- narrative rhythm
- visual density
- professional depth
- explanation strategy

---

## 2. Audience Analysis

Infer:

- expertise level
- educational background
- cognitive tolerance
- attention span
- emotional expectations

Audience determines:

- terminology complexity
- slide density
- explanation style
- amount of detail

---

## 3. User Goal Extraction

Infer the true objective behind the presentation.

Possible goals:

- obtain approval
- demonstrate expertise
- teach concepts
- persuade audience
- reduce questioning risk
- establish credibility
- simplify complexity

---

## 4. Risk Identification

Infer presentation risks.

Examples:

- audience may not understand
- excessive technical complexity
- defensive questioning risk
- weak narrative coherence
- information overload
- insufficient visual hierarchy

---

## 5. Time Constraint Analysis

Infer:

- short presentation
- medium presentation
- long-form presentation

Time determines:

- number of slides
- information pacing
- narrative depth

---

## 6. Content-type Recognition

Identify whether the presentation contains:

- experimental results
- conceptual explanation
- workflows
- storytelling
- numerical data
- visual comparison
- GIS maps
- scientific diagrams
- educational illustrations

---

# Output Structure

The parser should generate:

```text
Scenario:
Audience:
Primary Goal:
Risk Factors:
Visual Style:
Narrative Strategy:
Recommended Density:
Teaching Level:
Visual Complexity:
```

---

# Design Principle

The parser should NOT directly generate slides.

It should generate:

presentation reasoning conditions.

---

# Philosophy

Bad presentations begin with:

premature slide design.

Good presentations begin with:

correct audience understanding.
