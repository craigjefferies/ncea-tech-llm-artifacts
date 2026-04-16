You are designing **three original NCEA programming assessment tasks** for **AS92004: Create a computer program**.

Use the supplied Achievement Standard material, OMI rubric JSON, and `evidence_guide` as the source of truth.

The tasks must preserve assessment validity while still feeling fresh, motivating, and usable in a real classroom.

---

## Required Output

Generate **exactly three tasks**, in this order:

1. **Task 1 (Counter)** — a task where the program tallies items or events that meet a rule  
2. **Task 2 (Classifier)** — a task where the program sorts or labels inputs into categories  
3. **Task 3 (Countdown / Accumulator)** — a task where the program maintains a running total, countdown, or changing state until a stop condition is reached

Each task must be clearly distinct in context and student experience.

---

## Source-of-Truth Rules

- Use the AS92004 OMI rubric to decide what evidence the task must make possible.
- Treat each relevant OMI `description` as the actual requirement.
- Use `positive_signals` to decide what the task should naturally elicit.
- Use `negative_signals` and `common_confusion` to avoid setting traps, weak cues, or misleading task wording.
- Do not invent extra achievement requirements that are not supported by the supplied rubric.
- Do not expose JSON keys, OMI ids, or schema language to students.

---

## Global Design Rules

### 1. Theme originality
- Pick fresh, everyday, scientific, playful, or creative contexts.
- Avoid stale or overused examples.
- Do **not** use: money, banking, teachers/students as the core scenario, porridge, Goldilocks, batteries, voltages, or obvious recycled programming tropes.
- If a context overlaps too closely with a common classroom example, retheme it automatically.

### 2. Assessment validity
- Each task must create a real opportunity for a student to demonstrate the core Achieved evidence in AS92004.
- Merit and Excellence opportunities should emerge through stronger testing, clearer structure, stronger documentation, more effective control logic, and better handling of edge/invalid cases, where the rubric supports that.
- Do not reduce the task to a toy exercise with no believable reason for using input, iteration, selection, and a collection.

### 3. Student usability
- Write in clear, student-facing language.
- Avoid giving code solutions.
- Make the task brief specific enough to guide programming decisions, but open enough that students still have to think.
- Ensure the context feels suitable for secondary learners in Aotearoa New Zealand.

### 4. Structural expectations
- Each task should naturally support:
  - repeated input or repeated processing
  - a meaningful stop condition
  - sequence, selection, iteration, and collection use
  - visible testing opportunities
  - comments/documentation opportunities
- Use the supplied rubric to determine which of these must be explicit in the brief and which can sit in teacher notes.

### 5. Termination style
- Choose a stop method that fits the context:
  - string sentinel
  - numeric sentinel
  - automatic stop condition
  - state-based completion

---

## Output Format

Repeat this full structure for each of the three tasks.

### Task X (Tracking Type): Title

**Story Setup (2-3 sentences):**  
An engaging context that explains what the program is for, who it helps, and why the task matters.

**Student Brief:**  
A compact paragraph beginning with “Create a program that...”

**Core Requirements:**  
4-6 bullets describing:
- what the program takes in
- what it stores or tracks
- what it processes or decides
- what it outputs
- how or when it stops

**Merit / Excellence Stretch Built Into the Task:**  
2-4 bullets describing the kinds of stronger design, testing, documentation, or input-handling decisions the task invites, without turning into a marking schedule.

**Testing Guidance:**  
Give:
- 3-5 expected-case examples
- at least one likely boundary area to test if the task supports boundary testing
- at least one likely invalid case if the task supports invalid-input handling

**Teacher Note (not for students):**  
Short bullets only:
- which parts of the AS92004 rubric this task is especially good at surfacing
- one likely misconception or weak implementation pattern
- one reason this task is meaningfully different from the other two

---

## Design Heuristics for the Three Task Types

### Counter
- Best for tallying, counting, tracking frequencies, or monitoring repeated events
- The counting rule must be meaningful, not arbitrary

### Classifier
- Best for sorting, grouping, labelling, or categorising inputs
- The classification rules must be clear enough to program but rich enough to test properly

### Countdown / Accumulator
- Best for running totals, changing resources, progress toward a threshold, or state change over time
- The stop condition should feel natural to the scenario

---

## Quality Bar

The three tasks must be:
- **distinct**
- **original**
- **assessment-valid**
- **student-usable**
- **rich enough to invite stronger testing and structure**

Do not output:
- code solutions
- pseudo-OMI labels like `A1` / `M1` / `E1`
- generic filler contexts
- assessment briefs that could fit any standard

When run, the model must output:
- three fully written programming task briefs
- one Counter, one Classifier, one Countdown / Accumulator
- tasks that are visibly aligned to the AS92004 rubric and its `evidence_guide`
