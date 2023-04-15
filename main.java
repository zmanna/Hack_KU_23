import java.util.Scanner;
import java.io.IOException;

public class ScrambledGame {

    public static void main(String[] args) throws IOException {
        Scanner input = new Scanner(System.in);
        System.out.println("====================");
        System.out.println("Welcome to Scrambled");
        System.out.println("====================");
        System.out.print("Enter a username: ");
        String username = input.nextLine();
        Game game1 = new Game();
        game1.select_category();
        game1.play(username);
        while (true) {
            System.out.println("1) Try again\n2) Change category\n3) Display leaderboard\n4) Change user\n5) Try hard mode\n6) Exit");
            String usi = input.nextLine();
            if (usi.equals("1")) {
                game1.play(username);
            } else if (usi.equals("2")) {
                game1.select_category();
                game1.play(username);
            } else if (usi.equals("3")) {
                game1.display_leaderboard();
            } else if (usi.equals("4")) {
                System.out.print("Enter a username: ");
                username = input.nextLine();
                game1.select_category();
                game1.play(username);
            } else if (usi.equals("5")) {
                game1.hard_mode();
            } else {
                System.out.println("Thank you for playing. Come back soon.");
                break;
            }
        }
        input.close();
    }
}
