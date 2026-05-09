# AS91896 Short Programming Assessment Tasks

**Standard:** AS91896 — Use advanced programming techniques to develop a computer program  
**Level:** 2  
**Suggested time:** 1–2 hours  
**Language:** Python, unless otherwise agreed by the teacher

---

## Assessment Purpose

You will develop a small working program that solves one clearly defined problem.

Your program must show evidence of:

- input and output
- variables using at least two data types
- sequence, selection, and iteration
- use of a collection such as a list or dictionary
- at least two advanced programming techniques
- testing and debugging evidence

Advanced programming techniques may include:

- functions with parameters and/or return values
- modifying or processing data stored in collections
- non-trivial string or numeric processing
- using additional task-relevant libraries
- storing structured or multidimensional data in collections

Your program should be organised into clear functions. For higher evidence, repeated logic should be placed in functions, key limits should be stored as constants, and the main program flow should be easy to follow.

---

# Required Evidence

Submit:

1. Your final working program file.
2. One screenshot or short screencast showing a successful full run.
3. A compact test table showing:
   - expected use
   - boundary cases
   - invalid or unexpected input
4. One short testing/debugging note explaining either:
   - a bug or issue you found and fixed, or
   - a test that helped confirm an important part of your program worked correctly.

Your test table should include:

| Test type | Minimum evidence |
|---|---|
| Expected use | At least 2 normal cases |
| Boundary | Below, on, and above at least one important limit |
| Invalid or unexpected | At least 1 invalid input, such as text where a number is expected, a blank input, or an out-of-range value |
| Robustness | Evidence that the program gives a useful message and continues instead of crashing |

---

# Task 1 — Fitness Tracker

## Context

The local recreation centre wants a simple program that tracks a person’s running times across several workout days and gives basic feedback.

## Functional Brief

Create a program that:

- asks for the user’s name
- collects 5 running times in minutes
- stores the running times in a list
- checks that each time is between 10 and 60 minutes
- rejects invalid entries and asks again
- calculates the average running time
- finds the best running time, where the lowest time is best
- prints a clear summary

The summary should show:

- user name
- all valid running times
- average time
- best time
- a feedback message based on the result

## Programming Requirements

Your program should include:

- at least one function with a parameter and a return value
- a list that is used meaningfully
- a loop to collect or process data
- selection to validate input and create feedback
- clear variable names
- useful comments
- readable layout and indentation

For higher evidence, consider:

- storing limits such as minimum and maximum time as constants
- using functions to separate input, calculation, feedback, and output
- making sure invalid input does not corrupt the list of valid times
- testing both normal and unusual inputs

## Testing Guidance

Important boundaries:

- 9 should be rejected
- 10 should be accepted
- 60 should be accepted
- 61 should be rejected

Invalid or unexpected examples:

- blank input
- text such as `fast`
- a number outside the allowed range

---

# Task 2 — Pet Weight Category Checker

## Context

A local vet clinic wants a simple demo program that records pet weights and places them into broad weight categories.

This is a programming task, not a real medical judgement tool.

## Functional Brief

Create a program that:

- asks for the pet’s name
- accepts pet weights in kilograms until the user types `done`
- stores valid weights in a list
- checks that each weight is between 0 and 100 kg
- rejects invalid entries and asks again
- classifies each valid weight as:

| Weight | Category |
|---|---|
| less than 5 kg | Small |
| 5 kg to 25 kg | Medium |
| more than 25 kg | Large |

At the end, print a clear report showing:

- pet name
- each valid weight and its category
- how many weights were in each category

## Programming Requirements

Your program should include:

- at least one function with a parameter and a return value
- a list used to store and process weights
- a loop that continues until the user types `done`
- selection to validate weights and classify categories
- clear variable names
- useful comments
- readable layout and indentation

For higher evidence, consider:

- storing limits and category thresholds as constants
- using functions to separate input, validation, classification, counting, and reporting
- making sure invalid entries are ignored and do not get added to the list
- handling unexpected input without crashing

## Testing Guidance

Range boundaries:

- -0.1 should be rejected
- 0 should be accepted
- 100 should be accepted
- 100.1 should be rejected

Category boundaries:

- 4.9 should be Small
- 5 should be Medium
- 25 should be Medium
- 25.1 should be Large

Invalid or unexpected examples:

- blank input
- text such as `cat`
- a negative number
- a number above 100

---

# Task 3 — Fruit Ripeness Logger

## Context

A fruit packhouse wants a small program to record ripeness scores and summarise the condition of stored fruit.

## Functional Brief

Create a program that:

- asks for the fruit type
- collects 5 ripeness scores
- stores the scores in a list
- checks that each score is between 1 and 10
- rejects invalid entries and asks again
- classifies each valid score as:

| Score | Category |
|---|---|
| 1 to 3 | Underripe |
| 4 to 7 | Ripe |
| 8 to 10 | Overripe |

At the end, print a clear report showing:

- fruit type
- each score and its category
- how many scores were in each category

## Programming Requirements

Your program should include:

- at least one function with a parameter and a return value
- a list used to store and process scores
- a loop to collect or process data
- selection to validate scores and classify ripeness
- clear variable names
- useful comments
- readable layout and indentation

For higher evidence, consider:

- storing score limits and category thresholds as constants
- using functions to separate input, validation, classification, counting, and reporting
- making sure invalid scores are not added to the list
- handling unexpected input without crashing
- keeping the main program flow easy to follow

## Testing Guidance

Important boundaries:

- 0 should be rejected
- 1 should be accepted as Underripe
- 3 should be Underripe
- 4 should be Ripe
- 7 should be Ripe
- 8 should be Overripe
- 10 should be Overripe
- 11 should be rejected

Invalid or unexpected examples:

- blank input
- text such as `apple`
- a negative number
- a number above 10

---

# Teacher Judgement Notes

These tasks are designed to produce a compact body of evidence for AS91896.

They are not marked by counting features or calculating a percentage. The final grade remains a professional judgement based on the full body of evidence.

## Achieved evidence may include

- a working program that performs the specified task
- input, output, sequence, selection, and iteration
- variables using at least two data types
- at least two advanced programming techniques
- a collection used meaningfully
- readable layout and useful comments
- testing evidence for expected cases

## Merit evidence may include

- appropriate names and comments that help explain function and behaviour
- conventions suited to the chosen programming language
- clear boundary testing
- evidence that testing informed debugging or confirmation

## Excellence evidence may include

- a well-structured and logical program
- reduced repetition
- sensible use of constants
- functions used for clear responsibilities
- invalid or unexpected input handled safely
- testing evidence that supports robustness
- comprehensive testing across expected, boundary, invalid, and unexpected cases

Do not require professional-scale software architecture. Judge structure, flexibility, and robustness in relation to the size and purpose of the task.
