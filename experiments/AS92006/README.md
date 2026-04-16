# How to Build a Context-Engineered LLM Tutor for AS92006

**Goal:** Enable teachers to quickly assemble a purpose-built LLM tutoring tool using pre-made context artifacts, aligned to NCEA Achievement Standard AS92006.

---

##  Overview

This guide shows how to construct a **context-engineered LLM assistant** by combining:

1. **LLM Instructions** – defining the role (Process Tutor, Understanding Tutor, Grader)  
2. **Assessment (OMIs)** – finely—decomposed indicators  
3. **Content-Knowledge** – focused domain resources  

Rather than creating these artifacts yourself, you’ll **download the premade files** from the repository and integrate them into your chosen LLM platform.

---

##  Step-by-Step Guide

### 1. Download the Pre-Made Artifacts

From the repository (AS92006 experiment), grab:

- `AS92006.json` — contains the **OMIs**
- `content-knowledge.txt` — contains targeted domain material  
  *These files are accessible in the `experiments/AS92006` directory.* :contentReference[oaicite:1]{index=1}

### 2. Prepare Your LLM Environment

Open your preferred LLM-as-service platform:
- **Gemini Gem**, **CustomGPT**, or similar

### 3. Upload or Paste the Artifacts

- **File Upload Area**: Upload both `AS92006.json` and `content-knowledge.txt`.
- **Instruction Prompt Field**: Open the `instruction-prompt.txt` and **copy the instructions** into the instruction/system prompt area of your LLM.

### 4. Finalize and Test

- Save your LLM setup.
- Try out simple prompts like:
  - *“Explain usability in a human-computer interface.”*
  - *“Evaluate this student response: [insert answer].”*
- Observe how the assistant responds—instructor mode, grader mode, etc.
