import java.util.*;

public class PalindromeChecker {
     public static boolean isPalindrome(int x) {
        // Negative numbers are not palindromes
        if (x < 0) {
            return false;
        }

        // Convert the number to a string and check if it's equal to its reverse
        String strX = Integer.toString(x);
        return strX.equals(new StringBuilder(strX).reverse().toString());
    }

    // Check if a string is a palindrome
    public static boolean isPalindrome(String s) {
        // Compare the string with its reverse
        return s.equals(new StringBuilder(s).reverse().toString());
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input for integer
        System.out.print("Enter an integer: ");
        int num = scanner.nextInt();
        System.out.println("Is the integer a palindrome? " + isPalindrome(num));

        // Input for string
        System.out.print("Enter a string: ");
        scanner.nextLine(); // Consume newline
        String str = scanner.nextLine();
        System.out.println("Is the string a palindrome? " + isPalindrome(str));

        scanner.close();
    }
}
