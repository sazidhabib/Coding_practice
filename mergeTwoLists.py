class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    # Create a dummy node to act as the start of the merged list
    dummy = ListNode(-1)
    current = dummy

    # Merge the two lists
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Attach the remaining nodes from either list1 or list2
    current.next = list1 if list1 else list2

    return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example usage
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])
merged_list = merge_two_lists(list1, list2)
print(linked_list_to_list(merged_list))  # Output: [1, 1, 2, 3, 4, 4]
