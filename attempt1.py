import random

# Set the initial time for the game
time_left = 60

# Set the initial score to 0
score = 0

# Set the initial word length to 3
word_length = 3

# Set the number of correct guesses required to increment word length to 5
correct_guesses_needed = 5

# Load a dictionary of words
with open('words.txt', 'r') as file:
    dictionary = [line.strip() for line in file]

# Initialize the correct guess counter
correct_guesses = 0

#Initalize timer
import time
duration = 60
start_time = time.time()
end_time = start_time + duration

# Loop while there is still time left
while time_left > 0:

    # Select a random word of the current word length from the dictionary
    word = random.choice([w for w in dictionary if len(w) == word_length])

    # Scramble the word
    scrambled_word = ''.join(random.sample(word, len(word)))

    # Display the scrambled word to the user
    print('Scrambled word:', scrambled_word)

    # Read the user's guess for the unscrambled word
    guess = input('Your guess: ')

    # If the guess is correct
    if guess == word:
        # Add the length of the unscrambled word times 10 to the score
        score += len(word) * 10

        # Add a fixed amount of time to the remaining time
        time_left += 5
        end_time += 3

        # Increment the correct guess counter
        correct_guesses += 1

        # If the correct guess counter reaches the required number
        if correct_guesses == correct_guesses_needed:
            # Increment the word length
            word_length += 1

            # Reset the correct guess counter
            correct_guesses = 0

    # If the guess is incorrect
    else:
        # Subtract the length of the scrambled word times 10 from the score
        score -= len(scrambled_word) * 10
        if score < 0:
            score = 0

        # Subtract a fixed amount of time from the remaining time
        #time_left -= 5

    # Print the remaining time and current score
    current_time = time.time()
    time_remaining = max(0, int(end_time - current_time))
    print(f"Time remaining: {time_remaining} seconds")

    if time_remaining == 0:
        print("Countdown complete!")
        break

    time.sleep(1)  # Sleep for 1 second
    print('Current score:', score)

# Display the final score to the user
print('Game over! Your final score is:', score)