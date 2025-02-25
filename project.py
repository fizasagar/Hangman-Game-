import random 
words = ['enum', 'python', 'collab', 'vscode', 'game']

word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome To The Hangman Game")
print("_ " * len(word)) 

while attempts > 0:
    guess = input("\n Guess the letters: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Write one alphabet only!")
        continue

    if guess in guessed_letters:
        print("This letter is already guessed, choose another one.")
        continue
    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess! ")
    else:
        attempts -= 1
        print(f"Wrong guess! Remaining attempts: {attempts}")

    displayed_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print(displayed_word)

    if "_" not in displayed_word:
        print(f"Congratulations! The correct word is: {word}")
        break

else:
    print(f"Game Over! The correct word was: {word}")
