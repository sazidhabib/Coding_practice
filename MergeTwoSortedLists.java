class ListNode {
    int val;
    ListNode next;

    ListNode() {}

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

public class MergeTwoSortedLists {
    public static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // Create a dummy node to act as the start of the merged list
        ListNode dummy = new ListNode(-1);
        ListNode current = dummy;

        // Merge the two lists
        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                current.next = list1;
                list1 = list1.next;
            } else {
                current.next = list2;
                list2 = list2.next;
            }
            current = current.next;
        }

        // Attach the remaining nodes from either list1 or list2
        current.next = (list1 != null) ? list1 : list2;

        return dummy.next;
    }

    // Helper function to create a linked list from an array
    public static ListNode createLinkedList(int[] arr) {
        if (arr.length == 0) {
            return null;
        }
        ListNode head = new ListNode(arr[0]);
        ListNode current = head;
        for (int i = 1; i < arr.length; i++) {
            current.next = new ListNode(arr[i]);
            current = current.next;
        }
        return head;
    }

    // Helper function to convert a linked list to an array
    public static void printLinkedList(ListNode node) {
        while (node != null) {
            System.out.print(node.val + " ");
            node = node.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        ListNode list1 = createLinkedList(new int[]{1, 2, 4});
        ListNode list2 = createLinkedList(new int[]{1, 3, 4});
        ListNode mergedList = mergeTwoLists(list1, list2);
        printLinkedList(mergedList);  // Output: 1 1 2 3 4 4
    }
}
