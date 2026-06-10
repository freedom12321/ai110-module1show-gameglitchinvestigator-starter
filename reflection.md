# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| guess of 1 | go higher| go lower | actual result is 6 but it let us go lower when i guess 1 |
| new game | click the new game it will start| click new game it stuck | cannot start the new game |
| any guess |should show exact the hint| if it truelly lower it show go lower if it is higher it show higher |the hint is littile bit wierd(and also find sometime if guess is even number the comparison is weird) |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). 

if guess > secret:
    return "Too High", "📈 Go HIGHER!"
else:
    return "Too Low", "📉 Go LOWER!"


The bug is: The messages are backwards! When your guess is too high (guess > secret), the game tells you to "Go HIGHER!" when you should actually go lower. Similarly, when your guess is too low, it tells you to "Go LOWER!" when you should go higher. Here's why this happens:

i try do it in the game and see this problem, and then seems this is backward and AI explain correct

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
right now i do not find one for that since the wrong cases i find is real problem and the AI fix it reasonably so i do not find failure casses
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
first i will double check the ai suggesiton is reasonable and then write a test to see whether it pass and then play with it to see whether it is really resolved

- Describe at least one test you ran (manual or using pytest)  

I test the logic of the guess and the correct answer comparison like if true is 50 and guess is 50 it should win. if true is 50 and guess is 60 it should say go lower.

  and what it showed you about your code. 

it show the logic of the code that is the foundation of the game

- Did AI help you design or understand any tests? How?
yes i let it help me design this and tell me what this use for which cases test 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

is like a language that you can reopen a local webpage and then you can interact with it. you can play and double check 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

write down the bugs and then fix it with documentation

  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
might be first figure the wrong things and then i can tell AI more detail to fix the bugs

- In one or two sentences, describe how this project changed the way you think about AI generated code.
not all right and also might not can fix the bugs in one prompt we might need to back and forth to make it perfect.