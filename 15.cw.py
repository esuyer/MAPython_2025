import random

def wordle():
    words = ["code", "cool", "fire", "blue", "tree", "game", "fast", "slow", "work", "play"]
    
    while True:
        target = random.choice(words)
        print("\nNew word! It's a 4-letter word.")
        
        while True:
            guess = input("Enter your 4-letter guess: ").lower()
            
            if len(guess) != 4:
                print("Please enter exactly 4 letters.")
                continue
                
            if guess == target:
                print("Correct! The word was:", target)
                break
            
            # Simple feedback
            feedback = ""
            for i in range(4):
                if guess[i] == target[i]:
                    feedback += "G" # Green: Correct position
                elif guess[i] in target:
                    feedback += "Y" # Yellow: Wrong position
                else:
                    feedback += "." # Grey: Not in word
            
            print(f"Feedback: {feedback} (G=Right, Y=Wrong Spot, .=No)")

wordle()
