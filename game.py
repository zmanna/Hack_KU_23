
import random
import time


class Game:
    def __init__(self):
        self.score = 0
        self.words = []
        self.leaderboard = {}
        self.dictionary = []
        with open('dictionary.txt', 'r') as file:
            self.dictionary = [line.strip() for line in file]
            file.close()

    def select_category(self):
        print('What version would you like to play? :\n 1) General \n 2) Animals \n 3) Drinks \n 4) Foods \n 5) Music \n ')
        # Prompt the user to select a category of words to play the game with
        while True:
            user_num = input('Input the number of the category you want to play the game with: ')
            if user_num == "1":
                selected_category_name = 'dictionary.txt'
                break
            elif user_num == "2":
                selected_category_name = 'animals.txt'
                break
            elif user_num == "3":
                selected_category_name = 'drinks.txt'
                break
            elif user_num == "4":
                selected_category_name = 'foods.txt'
                break
            elif user_num == "5":
                selected_category_name = 'music.txt'
                break
            else:
                print("That was not an option. Try again.")
        with open(selected_category_name, 'r') as file:
            self.words = [line.strip() for line in file]
            file.close()
    def play(self, username):
        # Set the initial score to 0
        score = 0
        # Set the initial word length to 3
        word_length = 3
        # Set the number of correct guesses required to increment word length to 5
        correct_guesses_needed = 5
        # Initialize the correct guess counter
        correct_guesses = 0
        incorrect_guesses = 0
        duration = 60
        start_time = time.time()
        end_time = start_time + duration
        used_words = []

        # Loop while there is still time left
        while True:



            # Select a random word of the current word length from the dictionary
            word = random.choice([w for w in self.words if len(w) == word_length])
            while word in used_words:
                word = random.choice([w for w in self.words if len(w) == word_length])
            used_words.append(word)

            # Scramble the word
            scrambled_word = ''.join(random.sample(word, len(word)))

            while scrambled_word == word:
                scrambled_word = ''.join(random.sample(word, len(word)))

            # Display the scrambled word to the user
            print('Scrambled word:', scrambled_word)

            # Read the user's guess for the unscrambled word
            guess = input('Your guess: ')



            # Check if the detected language is English
            correct = True
            if guess in self.dictionary:
                for letter in guess:
                    if letter not in word:
                        correct = False
                # Add the length of the unscrambled word times 10 to the score
                if correct:
                    score += len(word) * 10

                    # Add a fixed amount of time to the remaining time
                    end_time += 3

                    # Increment the correct guess counter
                    correct_guesses += 1
                if correct == False:
                    score -= 10
                    print(f"Wrong. One correct answer was {word}.")
                    incorrect_guesses += 1
                    if score < 0:
                        score = 0
            # If the guess is incorrect
            else:
                # Subtract the length of the scrambled word times 10 from the score
                score -= 10
                print(f"Wrong. One correct answer was {word}.")
                incorrect_guesses += 1
                if score < 0:
                    score = 0
            if correct_guesses == correct_guesses_needed:
                # Increment the word length
                word_length += 1

                # Reset the correct guess counter
                correct_guesses_needed += 5

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
        print('======Game Stats=======')
        print(f'Final score: {score}')
        print(f"Correct guesses: {correct_guesses}")
        print(f"Incorrect guesses: {incorrect_guesses}")
        total_time = 60 + correct_guesses*3
        print(f"Total elapsed time: {total_time}")
        print(f'Rate: {total_time // correct_guesses} words per second')
        print('========================')
        try:
            if self.leaderboard[username] > score:
                self.leaderboard[username] = score
        except:
            self.leaderboard[username] = score #Need to change so it doesn't change your score to a lower one
    def display_leaderboard(self):
        print('======Leaderboard======')
        sorted_dict = dict(sorted(self.leaderboard.items(), key=lambda x: x[1], reverse=True))
        rank = 1
        for key,item in sorted_dict.items():
            print(f"{rank}: {key} -- {item}")
            rank += 1
        print('=======================')
    def hard_mode(self, username):
        print("In hard mode, you will have to unscramble the letters into 2 separate words.")
        # Set the initial score to 0
        score = 0
        # Set the initial word length to 3
        word_length = 3
        # Set the number of correct guesses required to increment word length to 5
        correct_guesses_needed = 5
        # Initialize the correct guess counter
        correct_guesses = 0
        incorrect_guesses = 0
        duration = 60
        start_time = time.time()
        end_time = start_time + duration
        used_words = []

        # Loop while there is still time left
        while True:



            # Select a random word of the current word length from the dictionary
            word = random.choice([w for w in self.words if len(w) == word_length]) + random.choice([w for w in self.words if len(w) == word_length])

            # Scramble the word
            scrambled_word = ''.join(random.sample(word, len(word)))

            while scrambled_word == word:
                scrambled_word = ''.join(random.sample(word, len(word)))

            # Display the scrambled word to the user
            print('Scrambled word:', scrambled_word)

            # Read the user's guess for the unscrambled word
            guess1 = input('First word: ')
            guess2 = input('Second word: ')



            # Check if the detected language is English
            correct = True
            if guess1 in self.dictionary and guess2 in self.dictionary:
                for letter in guess1:
                    if letter not in word:
                        correct = False
                for letter in guess2:
                    if letter not in word:
                        correct = False
                # Add the length of the unscrambled word times 10 to the score
                if correct:
                    score += len(word) * 10

                    # Add a fixed amount of time to the remaining time
                    end_time += 3

                    # Increment the correct guess counter
                    correct_guesses += 1
                if correct == False:
                    score -= 10
                    incorrect_guesses += 1
                    print(f"Wrong. One correct answer was {word}.")
                    if score < 0:
                        score = 0
            # If the guess is incorrect
            else:
                # Subtract the length of the scrambled word times 10 from the score
                score -= 10
                incorrect_guesses += 1
                print(f"Wrong. One correct answer was {word[:len(word)//2]} {word[len(word)//2:]}.")
                if score < 0:
                    score = 0
            if correct_guesses == correct_guesses_needed:
                # Increment the word length
                word_length += 1

                # Reset the correct guess counter
                correct_guesses_needed += 5

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
        print('======Game Stats=======')
        print(f"Correct guesses: {correct_guesses}")
        print(f"Incorrect guesses: {incorrect_guesses}")
        print(f"Total elapsed time: {end_time}")
        print('========================')
        try:
            if self.leaderboard[username] > score:
                self.leaderboard[username] = score
        except:
            self.leaderboard[username] = score #Need to change so it doesn't change your score to a lower one
