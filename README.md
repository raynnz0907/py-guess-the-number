# py-guess-the-number
A simple Python command-line number guessing game where the player tries to guess a randomly generated number. Great for beginners learning loops, conditions, and basic input handling.

# 🎯 Python Number Guessing Game

A simple and fun command-line number guessing game written in Python.  
The program generates a random number between **0 and 10**, and the player must guess the correct number.  
Perfect for beginners learning about loops, conditionals, and user input in Python.

---

## 🚀 Features
- Random number generation  
- Unlimited attempts until correct  
- Beginner-friendly code  
- Clear success and failure messages  

---

## 📌 How It Works
1. The program picks a random number using `random.randrange(11)`.
2. The user enters guesses using the input prompt.
3. The loop continues until the correct number is guessed.
4. The game congratulates the player when they win.

---

## 🧩 Code Example

```python
import random 

r_num = random.randrange(11)

while True:
    player_guess = int(input("Enter the number you want to guess: "))

    if player_guess == r_num:
        print(f" It was {r_num} congrats!!, You guessed it right")
        break
    else:
        print("You guessed it wrong.")
▶️ How to Run
Install Python (if not already installed)

Save the script as guess.py

Run the game in terminal:

bash
Copy code
python guess.py
🙌 Contributions
Feel free to open issues or submit pull requests to improve the game!

📄 License
This project is open-source and available under the MIT License.

yaml
Copy code

---

If you want, I can also:  
✅ Add advanced features to the code  
✅ Make a version with difficulty levels  
✅ Add a flowchart or screenshots for README  

Just tell me!
