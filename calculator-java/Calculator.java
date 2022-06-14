import java.io.*;

/** Methods for performing arithmetic calculations. */
class Arithmetic {
  public static float add(float num1, float num2) {
    return num1 + num2;
  }

  public static float subtract(float num1, float num2) {
    return num1 - num2;
  }

  public static float multiply(float num1, float num2) {
    return num1 * num2;
  }

  public static float divide(float num1, float num2) {
    return num1 / num2;
  }

  public static float modulo(float num1, float num2) {
    return num1 % num2;
  }

  public static float square(float num1) {
    return num1 * num1;
  }

  public static float cube(float num1) {
    return num1 * num1 * num1;
  }

}

/** The calculator program. */
public class Calculator {
  public static void main(String[] args) {
    // Main program loop
    while (true) {
      // Get user input
      String input = getUserInput("Enter your equation:");
      if (input == null) {
        System.out.println("Please enter an equation.");
        continue;
      }

      // Splits user input into a String array
      String[] tokens = input.split(" ");

      // Get the operator token, quit if user input is "q"
      String operator = tokens[0];
      if (operator.toLowerCase().equals("q")) {
        System.out.println("Quitting the program. Goodbye!");
        break;
      }

      // Get the numbers to be operated on
      Float num1, num2;
      try {
        num1 = Float.parseFloat(tokens[1]);

        if (tokens.length >= 3) {
          num2 = Float.parseFloat(tokens[2]);
        } else {
          num2 = 0f;
        }
      } catch (ArrayIndexOutOfBoundsException e) {
        // Throw the following error if token list is only 1 element and it's not 'q'
        System.out.println("Error: enter at least 1 number.");
        continue;
      } catch (NumberFormatException e) {
        // Throw the following error if input after operator is not numbers
        System.out.println("Error: not able to parse the numbers you entered.");
        continue;
      }

      Float result;
      switch (operator) {
        case "+":
          result = Arithmetic.add(num1, num2);
          break;

        case "-":
          result = Arithmetic.subtract(num1, num2);
          break;

        case "*":
          result = Arithmetic.multiply(num1, num2);
          break;

        case "/":
          result = Arithmetic.divide(num1, num2);
          break;

        case "%":
          result = Arithmetic.modulo(num1, num2);
          break;

        case "square":
          result = Arithmetic.square(num1);
          break;
        
        case "cube":
          result = Arithmetic.cube(num1);
          break;

        default:
          result = null;
          break;
      }

      if (result == null) {
        System.out.println("Invalid operator.");
      } else {
        System.out.println("=> " + result);
      }
    }
  }

  /** Works exactly like Python's input() function. */
  static String getUserInput(String prompt) {
    String inputLine = null;
    System.out.print(prompt + " ");
    try {
      BufferedReader is = new BufferedReader(new InputStreamReader(System.in));
      inputLine = is.readLine();
      if (inputLine.length() == 0) {
        return null;
      }
    } catch (IOException e) {
      System.out.println("IOException: " + e);
    }
    return inputLine;
  }
}
