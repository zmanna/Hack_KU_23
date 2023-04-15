import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Random;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Game {
    private int score;
    private List<String> words;
    private HashMap<String, Integer> leaderboard;
    private List<String> dictionary;

    public Game() throws IOException {
        this.score = 0;
        this.words = new ArrayList<>();
        this.leaderboard = new HashMap<>();
        this.dictionary = new ArrayList<>();
        BufferedReader reader = new BufferedReader(new FileReader("dictionary.txt"));
        String line = reader.readLine();
        while (line != null) {
            this.dictionary.add(line.trim());
            line = reader.readLine();
        }
        reader.close();
    }

    public void selectCategory() {
        System.out.println("What version would you like to play? :\n 1) General \n 2) Animals \n 3) Drinks \n 4) Foods \n 5) Music \n");
        // Prompt the user to select a category of words to play the game with
        while (true) {
            Scanner sc = new Scanner(System.in);
            String userNum = sc.nextLine();
            if (userNum.equals("1")) {
                this.words = this.dictionary;
                break;
            } else if (userNum.equals("2")) {
                this.words = readWordsFromFile("animals.txt");
                break;
            } else if (userNum.equals("3")) {
                this.words = readWordsFromFile("drinks.txt");
                break;
            } else if (userNum.equals("4")) {
                this.words = readWordsFromFile("foods.txt");
                break;
            } else if (userNum.equals("5")) {
                this.words = readWordsFromFile("music.txt");
                break;
            } else {
                System.out.println("That was not an option. Try again.");
            }
        }
    }

    private List<String> readWordsFromFile(String fileName) {
        List<String> words = new ArrayList<>();
        try {
            BufferedReader reader = new BufferedReader(new FileReader(fileName));
            String line = reader.readLine();
            while (line != null) {
                words.add(line.trim());
                line = reader.readLine();
            }
            reader.close();
        } catch (IOException e) {
            System.out.println("Error reading words from file: " + e);
        }
        return words;
    }

    public void play(String username) {
        // Set the initial score to 0
        score = 0;
        // Set the initial word length to 3
        int wordLength = 3;
        // Set the number of correct guesses required to increment word length to 5
        int correctGuessesNeeded = 5;
        // Initialize the correct guess counter
        int correctGuesses = 0;
        int incorrectGuesses = 0;
        int duration = 60;
        long startTime = System.currentTimeMillis();
        long endTime = startTime + TimeUnit.SECONDS.toMillis(duration);
        List<String> usedWords = new ArrayList<>();

        // Loop while there is still time left
        while (true) {
            // Select a random word of the current word length from the dictionary
            List<String> wordsOfCurrentLength = new ArrayList<>();
            for (String word : words) {
                if (word.length() == wordLength && !usedWords.contains(word)) {
                    wordsOfCurrentLength.add(word);
                }
            }
            Random rand = new Random();
            String word = wordsOfCurrentLength.get(rand.nextInt(wordsOfCurrentLength.size()));
            usedWords.add(word);

           
