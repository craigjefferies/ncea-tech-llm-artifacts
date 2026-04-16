# Context Engineering for NCEA Assessments

> **Think of this as a practical hack to get any LLM working like a teaching assistant in the NCEA space.**

The idea is simple: build a structured scaffold that shapes how an LLM behaves. Done right, it can act like a tutor, a grader, or a guide—always tied back to New Zealand’s NCEA standards. It’s about setting up the right input ecosystem so the model stays focused, accurate, and useful.

## Core Pieces

1. **LLM Instructions**  
2. **Assessment (Observable Micro-Indicators, OMIs)**  
3. **Content Knowledge** *(optional)*

---

## Breaking It Down

### 1. LLM Instructions  
These spell out the roles the LLM can take on:

- **Process Tutor**  
  Helps students work through a larger task or project—planning, structuring, and problem-solving.

- **Understanding Tutor**  
  Acts like a subject tutor—explains concepts, answers questions, and builds understanding for exam or knowledge-heavy content.

- **Grader**  
  Maps student work against observable indicators from NZQA Achievement Standards, giving feedback that’s structured and standards-based.

### 2. Assessment (OMIs)  
This is the backbone. OMIs turn standards into things you can actually see and check:

- **Observable Elements**  
  Clear, measurable markers of performance.

- **Evidence Guides**  
  Positive signals, negative signals, and common confusions that make grading more transparent.

- **Examples**  
  Sample responses that show what success looks like.

With OMIs, grading becomes transparent, consistent, and tied directly to NZQA criteria.

### 3. Content Knowledge *(Optional)*  
A bank of subject-specific stuff—definitions, examples, scaffolds. This narrows the LLM’s output, keeping it accurate and relevant.

---

## Why Bother?

Because when you put it together:

- **LLM Instructions** tell the model how to behave.  
- **OMIs** lock assessments to real, observable outcomes.  
- **Content Knowledge** keeps things grounded in fact.  

That’s context engineering: not just telling the model what to do, but building the environment it needs to actually work as an NCEA-aligned teaching assistant.

> Context engineering is basically “setting up the system so the LLM has the right info, in the right way, to get the job done.”
