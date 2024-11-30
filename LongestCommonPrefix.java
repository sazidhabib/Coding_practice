import java.util.*;
public class LongestCommonPrefix {
    

    public static String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) {
            return "";
        }

        // Sort the array
        Arrays.sort(strs);

        // Compare the first and last strings in the sorted array
        String first = strs[0];
        String last = strs[strs.length - 1];
        StringBuilder commonPrefix = new StringBuilder();

        // Find the common prefix between the first and last strings
        for (int i = 0; i < Math.min(first.length(), last.length()); i++) {
            if (first.charAt(i) == last.charAt(i)) {
                commonPrefix.append(first.charAt(i));
            } else {
                break;
            }
        }

        return commonPrefix.toString();
    }

    public static void main(String[] args) {
        String[] strs = {"flower", "flow", "flight"};
        System.out.println(longestCommonPrefix(strs));  // Output: "fl"
    }
}


