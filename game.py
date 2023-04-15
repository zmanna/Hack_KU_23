import time
class Game:
    def __init__(self):
        self.score = 0
        self.word_length = 3
        self.correct_guesses = 0
        self.correct_needed = 5
    def play(self):
        start_time = time.time()
        end_time = start_time + 60

        # Loop while there is still time left
        while True:
            # Select a random word of the current word length from the dictionary
            word = random.choice([w for w in chosen_list if len(w) == word_length])

            # Scramble the word
            scrambled_word = ''.join(random.sample(word, len(word)))

            while scrambled_word == word:
                scrambled_word = ''.join(random.sample(word, len(word)))

            # Display the scrambled word to the user
            print('Scrambled word:', scrambled_word)

            # Read the user's guess for the unscrambled word
            guess = input('Your guess: ')

            # If the guess is correct
            if guess == word:
                # Add the length of the unscrambled word times 10 to the score
                self.score += len(word) * 10

                # Add a fixed amount of time to the remaining time
                self.end_time += 3

                # Increment the correct guess counter
                self.correct_guesses += 1

                # If the correct guess counter reaches the required number
                if self.correct_guesses == self.correct_needed:
                    # Increment the word length
                    self.word_length += 1

                    # Reset the correct guess counter
                    correct_guesses = 0

            # If the guess is incorrect
            else:
                # Subtract the length of the scrambled word times 10 from the score
                self.score -= len(scrambled_word) * 10
                print(f"Wrong. One correct answer was {word}.")
                if self.score < 0:
                    self.score = 0

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
            print('Current score:', self.score)

        # Display the final score to the user
        print('Game over! Your final score is:', self.score)
