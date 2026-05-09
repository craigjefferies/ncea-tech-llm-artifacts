# AS91896 Short Assessment Task  
## Rugby Match Stats Tracker

**Context**  
A rugby coach wants a simple program to track one player’s tackle count across several games. The program should help the coach see the player’s total work rate, average tackles per game, best game, and a short feedback message.

This is a small programming task. It is not a full sports app.

---

## Functional Brief

Create a Python program that:

- asks for the player’s name
- collects tackle counts for 5 games
- stores the tackle counts in a single list of integers
- checks that each tackle count is between 0 and 40
- rejects invalid entries and asks again
- calculates:
  - total tackles
  - average tackles per game
  - best game, where the highest tackle count is best
- prints a clear coach summary

The summary should show:

- player name
- all 5 tackle counts
- total tackles
- average tackles per game
- best tackle count
- a feedback message based on the average

Example feedback:

| Average tackles | Feedback |
|---|---|
| less than 5 | Low involvement |
| 5 to 12 | Solid contribution |
| more than 12 | High defensive work rate |

---

## Programming Requirements

Your program should include:

- input and output
- variables using at least two data types  
  For example: string for player name, integers for tackles, float for average.
- sequence, selection, and iteration
- one single list of integers
- at least one function with a parameter and a return value
- clear variable names
- useful comments
- readable layout and indentation

Your program should be organised into clear functions. For higher evidence, repeated logic should be placed in functions, key limits should be stored as constants, and the main program flow should be easy to follow.

---

## Possible Advanced Programming Techniques

Your program may show advanced programming techniques through:

- using a list to store and process tackle counts
- adding valid tackle counts to the list
- looping through the list to calculate totals or feedback
- using functions with parameters and return values

For example:

- `calculate_average(tackles)`
- `get_feedback(average_tackles)`
- `get_valid_tackle_count()`

These are examples only. You may use different function names.

---

## Required Evidence

Submit:

1. Your final working Python file.
2. One screenshot or short screencast showing a successful full run.
3. A compact test table showing:
   - expected use
   - boundary cases
   - invalid or unexpected input
4. One short testing/debugging note explaining either:
   - a bug or issue you found and fixed, or
   - a test that helped confirm an important part of your program worked correctly.

---

## Testing Guidance

Your test table should include:

| Test type | Minimum evidence |
|---|---|
| Expected use | At least 2 normal tackle counts |
| Boundary | Below, on, and above an important limit |
| Invalid or unexpected | At least 1 invalid input |
| Robustness | Evidence that the program gives a useful message and continues instead of crashing |

Important boundaries:

- `-1` should be rejected
- `0` should be accepted
- `40` should be accepted
- `41` should be rejected

Invalid or unexpected examples:

- blank input
- text such as `lots`
- a negative number
- a number above 40

---

## Example Program Run

Player name: Arama

Game 1 tackles: 8  
Game 2 tackles: 11  
Game 3 tackles: 5  
Game 4 tackles: 14  
Game 5 tackles: 9  

Summary for Arama

Tackle counts: [8, 11, 5, 14, 9]  
Total tackles: 47  
Average tackles: 9.4  
Best game: 14 tackles  
Feedback: Solid contribution

---

## Teacher Judgement Notes

This task is designed to be short, but still produce evidence for AS91896.

It can support Achieved evidence through:

- a working program
- input and output
- variables, sequence, selection, and iteration
- a single list used meaningfully
- at least two advanced programming techniques
- expected-case testing

It can support Merit evidence through:

- clear names and comments
- Python conventions
- boundary testing

It can support Excellence evidence through:

- clear structure
- useful constants such as `MIN_TACKLES` and `MAX_TACKLES`
- functions with clear responsibilities
- invalid input handled without crashing
- testing that supports robustness

The task should not be judged by counting features. The final grade remains a professional judgement based on the full body of evidence.
