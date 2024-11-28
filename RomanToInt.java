// import java.util.*;

// public class RomanToInt {
//      public static int romanToInt(String s) {
//         // Map Roman numerals to their integer values
//         HashMap<Character, Integer> romanToValue = new HashMap<>();
//         romanToValue.put('I', 1);
//         romanToValue.put('V', 5);
//         romanToValue.put('X', 10);
//         romanToValue.put('L', 50);
//         romanToValue.put('C', 100);
//         romanToValue.put('D', 500);
//         romanToValue.put('M', 1000);

//         // Initialize result
//         int total = 0;

//         // Loop through the string
//         for (int i = 0; i < s.length(); i++) {
//             // Get the value of the current symbol
//             int current = romanToValue.get(s.charAt(i));
            
//             // Get the value of the next symbol if it exists
//             if (i < s.length() - 1 && current < romanToValue.get(s.charAt(i + 1))) {
//                 total -= current;
//             } else {
//                 total += current;
//             }
//         }

//         return total;
//     }

//     public static void main(String[] args) {
//         String s = "III";
//         System.out.println(romanToInt(s));  // Output: 3
//     }
// }
