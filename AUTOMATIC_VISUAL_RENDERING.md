# Automatic Visual Rendering — Phase Plan

This document defines the next evolution stage of the PPT Cognitive Design Skill framework.

The goal is to move from:

- cognitive presentation reasoning

into:

- executable visual slide rendering.

---

# Core Evolution

Current framework status:

```text
User Requirement
    ↓
Cognitive Reasoning
    ↓
Narrative Planning
    ↓
Layout Reasoning
    ↓
Visual Semantic Reasoning
    ↓
Structured Slide Design
```

Next-stage target:

```text
User Requirement
    ↓
Cognitive Reasoning
    ↓
Narrative Planning
    ↓
Layout Planning
    ↓
Visual Rendering Engine
    ↓
Rendered Slide Output
```

---

# Stage Goal

The system should eventually generate:

- real slide layouts
- rendered diagrams
- visual hierarchy
- positioned text blocks
- semantic color systems
- exportable PPT pages

instead of only reasoning descriptions.

---

# Recommended Technical Path

The recommended evolution path is:

```text
Reasoning Framework
    ↓
Wireframe Rendering
    ↓
HTML Slide Rendering
    ↓
SVG Diagram Rendering
    ↓
PPT Export System
```

---

# Why Start With HTML

HTML is recommended before PPT generation because:

- easier layout control
- easier visual rendering
- easier iteration
- easier AI generation
- easier browser preview
- easier SVG integration

HTML acts as:

an intermediate visual rendering layer.

---

# Recommended Architecture

```text
User Prompt
    ↓
Presentation Reasoning Engine
    ↓
Slide JSON Structure
    ↓
Layout Engine
    ↓
HTML/SVG Renderer
    ↓
Visual Slide Output
```

---

# First Executable Goal

The first rendering milestone should be:

# Generate one visually rendered teaching slide.

Recommended target slide:

```text
How Water Affects Crop Growth
```

because it includes:

- mechanism flow
- semantic arrows
- cognitive hierarchy
- educational explanation
- GIS semantic linkage

---

# Phase 1 — Rendering Prototype

## Objective

Generate one HTML-rendered slide.

---

## Required Components

### 1. Slide Structure Schema

The system should define:

```json
{
  "title": "How Water Becomes Yield",
  "layout": "horizontal_mechanism_flow",
  "components": [
    "title",
    "mechanism_diagram",
    "supporting_labels",
    "teaching_note",
    "GIS_note"
  ]
}
```

---

### 2. Layout Engine

The layout engine should determine:

- object positions
- spacing
- hierarchy
- visual flow
- alignment

---

### 3. Semantic Visual Engine

The rendering system should map:

| Semantic Meaning | Visual Style |
|---|---|
| Water | Blue |
| Crop Growth | Green |
| Stress | Orange |
| Neutral System | Gray |

---

### 4. Diagram Rendering Layer

The renderer should generate:

- arrows
- process flows
- semantic icons
- hierarchy blocks
- labels

using:

- SVG
- HTML
- CSS

---

# Recommended Rendering Technology

## Best Starting Stack

```text
HTML
CSS
SVG
```

Reason:

- lightweight
- visual
- AI-friendly
- easy iteration
- exportable

---

# Future Stack Evolution

Possible future stack:

```text
React
Tailwind
SVG Engine
PptxGenJS
Figma API
```

---

# Phase 2 — Multi-slide Rendering

After one successful slide:

expand into:

- cover slides
- workflow slides
- GIS map layouts
- comparison layouts
- scientific storytelling slides

---

# Phase 3 — Interactive AI Design Agent

Future interaction mode:

```text
User:
"Reduce cognitive density"

AI:
- increase whitespace
- reduce labels
- enlarge diagram
- simplify flow
```

The system becomes:

an interactive presentation design agent.

---

# Long-term Rendering Goal

The final rendering system should support:

- automatic layout generation
- semantic diagram generation
- adaptive visual hierarchy
- audience-aware rendering
- exportable presentation systems

---

# Immediate Next Step

The next concrete implementation target is:

# Build a single HTML-rendered teaching slide.

Target:

```text
How Water Affects Crop Growth
```

with:

- semantic arrows
- blue-green color system
- centered mechanism flow
- teaching-oriented hierarchy
- low cognitive load

---

# Final Principle

Rendering should NOT prioritize:

visual decoration.

Rendering should prioritize:

cognitive communication efficiency.
