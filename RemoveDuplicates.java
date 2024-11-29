public class RemoveDuplicates {
    public static int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        // Initialize a pointer for the unique elements
        int k = 1;

        for (int i = 1; i < nums.length; i++) {
            // If the current element is not equal to the last unique element
            if (nums[i] != nums[k - 1]) {
                nums[k] = nums[i];  // Place the unique element in the correct position
                k++;
            }
        }

        return k;
    }

    public static void main(String[] args) {
        int[] nums = {1, 1, 2,3,3,3,3,5,5,5,5,6,6};
        int k = removeDuplicates(nums);
        System.out.println(k);  // Output: 2

        // Print the unique elements
        for (int i = 0; i < k; i++) {
            System.out.print(nums[i] + " ");  // Output: 1 2
        }
    }
}
