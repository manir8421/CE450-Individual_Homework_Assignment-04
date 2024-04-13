def create_linked_list(elements):              # Create a linked list from a list of elements.
    if not elements:                            # Base case: if the list is empty, return an empty list.
        return []                               # Return an empty list.
    else:
        return [elements[0], create_linked_list(elements[1:])]           # Return a list containing the first element and the rest of the list.

def rvrs_lnk(s):                                # Reverse a linked list.
    reverse_list = []                           # Initializes the reversed list as an empty list.
    while s:                                    # Loop until the original list is empty.
        reverse_list = [s[0], reverse_list]     # Prepend the current node's value to the reversed list.
        s = s[1]                                # Move to the next node in the original list.
    return reverse_list                         # Return the head of the reversed list after all nodes have been processed.

def show_list(linked_list):                     # Display a linked list.
    if not linked_list:                         # Base case: if the list is empty, return "[]".
        return "[]"                             # Return an empty list.
    else:
        return f"[{linked_list[0]}, {show_list(linked_list[1])}]"       # Return a string containing the first element and the rest of the list.

def make_list():
    values = input("\nType values for the linked list separated by a comma ',' (e.g., 1,2,3): ").split(',')
    return create_linked_list([val.strip() for val in values])          # Process input and create linked list directly.

def main():
    user_linked_list = make_list()                                      # Create a linked list from user's input.
    print("Constructed Linked List:", show_list(user_linked_list))
    reversed_linked_list = rvrs_lnk(user_linked_list)                   # Reverse the created linked list.
    print("Reversed Linked List:", show_list(reversed_linked_list))     # Display the reversed linked list.

if __name__ == "__main__":
    while True:                                                         # Loop allows the user to use the program repeatedly.
        main()
        again = input("\nDo you want to use the program again? (y/n): ").lower()
        if again != 'y':
            print("Exiting the program...")
            break
