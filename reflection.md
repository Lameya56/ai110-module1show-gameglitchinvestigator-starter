# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

---
   1) Hint messages are backwards.The hints kept saying to go lower even when the actual answer was a high number. If I guess a high number it says to go higher and if I guess a low number it says to go lower.
   2) Attempts left calculation is off. It says game over with one attempt left.
   3) The new game button doesn't work. It doesn't restart the game.
   4) The level hard is actually easy than normal 
   5) There's no bounds checking so negative numbers are accepted even though it's outside the valid game range. 
   6) Decimal numbers are truncated. 
   7) Guessing too high rewards points on even attempts, guessing too high gives +5 points instead of a penalty. There's no logical reason guessing wrong should ever increase your score. It should penalize like "Too Low" does.
   8) "Too Low" always deducts 5, but "Too High" deducts 5 only on odd attempts
   9) Score can go negative. There's no floor on the score, so a player who guesses wrong many times ends up with a negative score 


## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---
I used Claude Code as my main AI teammate throughout this project. I would highlight code sections and ask Claude to explain what the function was doing, identify bugs, and then apply fixes directly to the files.

**Example of a correct AI suggestion:** Claude correctly identified that the hint messages in `check_guess` were backwards — when `guess > secret` the message said "Go HIGHER!" when it should say "Go LOWER!". I verified this by manually tracing through the logic: if my guess is 60 and the secret is 50, I guessed too high so I need to go lower, but the original code told me to go higher. Once Claude swapped the messages I tested it in the running app and the hints pointed the right direction.

**Example of an incorrect or misleading suggestion:** Claude's comment in `test_update_score_win_early` says "Winning on attempt 1 should give maximum points" but the formula `100 - 10 * (attempt_number + 1)` with attempt 1 actually gives `100 - 20 = 80`, not the true maximum. Winning on attempt 0 would give 90. The test value of 80 is correct for attempt 1, but the comment is slightly misleading — I had to manually calculate the formula myself to confirm the expected value was right.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
I decided a bug was really fixed by combining two approaches: reading through the updated code logic manually to confirm it made sense, and running the app with `streamlit run app.py` to test the behavior directly in the browser.

For example, after fixing the hint messages in `check_guess`, I ran the app, set the difficulty to Normal, and intentionally guessed a number I knew was too high. The hint now correctly said "Go LOWER!" instead of "Go HIGHER!", which confirmed the fix worked. I also ran `pytest tests/test_game_logic.py -v` after writing the `update_score` tests, and all 6 new tests passed immediately — this gave me confidence that the scoring logic (deducting 5 for wrong guesses, flooring at 0, minimum 10 points on a win) was all behaving correctly.

Claude helped me design the `update_score` tests by walking through the edge cases I should cover: winning early vs. late, both wrong-guess directions, a score that would go below zero, and an unknown outcome. Without that guidance I might have only written one or two basic tests and missed the floor-at-zero edge case entirely.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---
Imagine every time you click a button or type something in the app, Streamlit completely re-runs your Python script from top to bottom — like refreshing a webpage. That means any regular variables you set get wiped out and reset on every interaction. `st.session_state` is a special dictionary that survives these reruns, so it's how you store anything that needs to persist across interactions, like the secret number, the attempt count, and the score.

This is why bugs like initializing `attempts = 1` instead of `0` matter so much — the initialization only runs once (when the key isn't in `st.session_state` yet), so if you start with the wrong value, every subsequent rerun builds on that wrong starting point. Understanding reruns also explained why the "New Game" button needed `st.rerun()` to force a fresh run after resetting state, otherwise the old UI values would still be displayed until the next natural interaction.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

---
One habit I want to reuse is asking AI to explain a function before asking it to fix anything. Also writing agents. 
This was my first time creating an agent and using it and I really enjoyed the process so I hope to continue making more specific agents for specific tasks. 

This project changed how I think about AI-generated code by showing me that it can contain plausible-looking bugs that are hard to spot without reading carefully — the type-switching in `check_guess` and the scoring reward for wrong guesses both looked intentional at first glance. AI is a fast starting point, but the code still needs to be read and reasoned about like any other code.
