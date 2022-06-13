import java.util.Scanner;
import java.util.Random;

/** A number guessing game. */
public class Game {
  public static void main(String[] args) {
    System.out.println("Welcome to the Guessing Game!");
 
    Scanner input = new Scanner(System.in);
    int target = new Random().nextInt(101);
    int guessCount = 0;
    boolean gameLoop = true;

    System.out.print("Hi! What's your name? ");
    String name = input.nextLine();
    System.out.print("Hey %s, I'm thinking of a number between 0 and 100.\n".formatted(name));

    while (gameLoop) {
      System.out.print("Please enter your guess: ");
      int guess = input.nextInt();
      guessCount += 1;

      if (guess < target) {
        System.out.print("Your guess is too low, guess again: \n");
      } else if (guess > target) {
        System.out.print("Your guess is too high, guess again: \n");
      } else {
        System.out.print("Congrats %s! You guessed the number in %d tries! \nThank you for playing!\n".formatted(name, guessCount));
        gameLoop = false;
      }
    }




  }
}
