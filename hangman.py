import random

words = {
    "PYTHON": "A programming language",
    "LAPTOP": "A portable computer",
    "PLANET": "Earth is one",
    "CODING": "Writing computer instructions",
    "GARDEN": "A place where plants grow"
}

word = random.choice(list(words.keys()))
guessed = set()
wrong = 0
max_wrong = 6

print("🎮 Welcome to Hangman!")
print("Hint:", words[word])

while wrong < max_wrong:
    display = " ".join(
        letter if letter in guessed else "_"
        for letter in word
    )
    print("\nWord:", display)
    print("Wrong guesses:", wrong, "/", max_wrong)

    if all(letter in guessed for letter in word):
        print("🎉 You win!")
        break

    guess = input("Guess a letter: ").strip().upper()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter one letter, please.")
        continue

    if guess in guessed:
        print("You already guessed that letter!")
        continue

    guessed.add(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        wrong += 1
        print("❌ Wrong!")

else:
    print("😢 Game over! The word was:", word)

if all(letter in guessed for letter in word):
    print("The word was:", word)