# Starter Prompt Toolkit for AI Tutor

## Overview and Purpose
This toolkit contains 21 generalized starter prompts designed to initiate effective, diagnostic learning dialogues in any domain (e.g., HCI, math, biology). These prompts mimic a teacher's proactive initiation: Use them at session start, after pauses, or for vague user inputs to build momentum, diagnose knowledge levels, and scaffold learning.

### Key Principles
- **Bloom's Taxonomy Ordering**: Prompts progress from foundational (Remember/Understand) to advanced (Create/Evaluate) to support scaffolded journeys.
- **Generalization**: Replace placeholders like [concept] (e.g., "heuristics" in HCI), [topic] (e.g., "HCI"), [outcome] (e.g., "user experience"), or [related field] (e.g., "psychology") with domain-specific details from OMI JSON file.
- **Integration with AI Tutor Components**:
  - **Observable Micro Indicators (OMIs)**: After using a prompt, observe student responses for accuracy, confidence, hesitation, elaboration, etc., to adapt (e.g., escalate to higher # if successful).
  - **Instruction Prompt**: Refer to your core instructions for overall behavior (e.g., be encouraging, provide feedback).
  - **Content Knowledge**: Pull examples, facts, or scenarios from the topic-specific file to fill prompts.
- **When to Use**:
  - **Proactive Initiation**: Select one at session start or if user input is vague (e.g., "Help me learn [topic]").
  - **Selection Logic**: 
    - Start with low #s (1-5) for beginners or unknown levels.
    - Use mid #s (6-10) for analysis/evaluation if basics are solid.
    - Escalate to high #s (11-16) for creation/synthesis when momentum builds.
    - Choose metacognitive #s (17-21) for reflection or misconception checks anytime.
    - Adapt based on OMIs (e.g., if low confidence, pick #18).
  - **Transition**: After 2-3 successful exchanges, shift to reactive mode (e.g., "What would you like to explore next?").
- **Use Cases**:
  - Diagnostic Start: #1-4 to probe basics.
  - Building Skills: #5-10 for application/analysis.
  - Advanced Engagement: #11-16 for creativity/problem-solving.
  - Reflection: #17-21 to check understanding and adjust.
- **Version**: 1.0 (Update by replacing this file).

## Prompt Library
The table below lists all prompts. Columns: # (ID), Task Category (Bloom level), Starter Prompt (template), Rationale (pedagogical value), OMI Opportunities (what to observe).

| # | Task Category (Bloom) | Starter Prompt (Template) | Rationale | OMI Opportunities |
|---|-----------------------|---------------------------|-----------|-------------------|
| 1 | Remember | “Quiz me, one term at a time: what does [concept] mean in [topic]?” | Baseline recall; fast check on precision & confidence. | Accuracy of definitions; hesitation in responses. |
| 2 | Understand | “Explain [concept] in simple words, then ask me to rephrase it.” | Checks conceptual grasp via student paraphrase. | Quality of rephrasing; reveals partial understanding. |
| 3 | Apply | “Show a real example from [topic]; ask how [concept] applies.” | Tests knowledge transfer to authentic context. | Application accuracy; transfer to new scenarios. |
| 4 | Apply (effects) | “Present a feature in [topic]; ask how it changes [outcome].” | Probes cause-and-effect reasoning. | Causal explanations; depth of impact analysis. |
| 5 | Apply (Interdisciplinary) | “Link [concept] from [topic] to [related field]; ask me to explain the connection.” | Encourages cross-domain application; builds broader relevance. | Creative connections; reveals siloed thinking. |
| 6 | Analyze (patterns) | “Give a mini-case; ask which [concept] it illustrates and why.” | Surfaces pattern-recognition skill. | Pattern-spotting speed; justification strength. |
| 7 | Analyze (root-cause) | “Describe a flaw in [topic]; guide me to pinpoint causes via [concept].” | Decomposition of complex problems. | Breakdown logic; identification of root issues. |
| 8 | Evaluate (improve) | “Show an example in [topic]; ask me to propose two improvements using [concept] and justify.” | Combines critique with principled reasoning. | Improvement creativity; evidence in justifications. |
| 9 | Evaluate (evidence) | “Give a scenario; ask me to rate [concept]'s effectiveness with evidence.” | Encourages explicit justification. | Evidence quality; balanced evaluation. |
| 10 | Compare | “Contrast two approaches in [topic]; ask which better fits [concept] and defend.” | Forces evidence-based comparison. | Comparison depth; bias in defenses. |
| 11 | Create (design) | “Outline a situation; challenge me to invent a solution using [concept] and explain.” | Stimulates synthesis & creativity. | Originality of ideas; reasoning coherence. |
| 12 | Create (analogy) | “Ask me to create an everyday analogy for [concept] in [topic].” | Deep synthesis; checks conceptual restructuring. | Analogy relevance; clarity of abstraction. |
| 13 | Create (teach-back) | “Pretend I’m explaining [concept] to a novice; ask me to do it clearly.” | High-fidelity proxy for mastery; reveals fuzzy edges. | Explanation simplicity; omissions in teaching. |
| 14 | Create (Prediction) | “Give half a worked example; ask me to predict the next step using [concept].” | Measures forward-thinking application skill. | Prediction accuracy; anticipatory reasoning. |
| 15 | Apply (simulation) | “Role-play a scenario; ask me to decide using [concept].” | Immersive practice elicits decision-making. | Decision rationale; real-time adaptability. |
| 16 | Analyze (Error) | “Present a common error in [topic]; ask me to fix it using [concept] and explain why.” | Builds resilience through deliberate mistake correction. | Error detection speed; correction thoroughness. |
| 17 | Diagnose misconception | “State a common misunderstanding about [concept]; ask if I agree and to correct it.” | Surfaces latent errors early. | Agreement/disagreement; correction accuracy. |
| 18 | Confidence check | “Ask me a question on [concept], then rate my confidence 1-5.” | Provides double OMI: accuracy + self-efficacy. | Confidence calibration; correlation with correctness. |
| 19 | Reflect (metacog) | “After recapping [concept], ask what still confuses me and why.” | Self-reported gaps steer adaptive follow-ups. | Self-awareness; specificity of confusion points. |
| 20 | Summarise learning | “Have me summarise key points about [topic] in three bullets.” | Tests consolidation & highlights retention gaps. | Summary completeness; key idea prioritization. |
| 21 | Prediction | “Give the first half of an example; ask me to predict next using [concept].” | Measures forward-thinking application skill. | Predictive logic; handling uncertainty. |

## Additional Notes
- **Parsing Tips for LLM**: To retrieve, query like "Get Prompt #5 template and rationale" or "Select a Create-level prompt for [topic]".
- **Customization**: Adapt prompts on-the-fly (e.g., add encouragement: "Great job—now...").
- **Updates**: If modified, update the version number and re-upload.
