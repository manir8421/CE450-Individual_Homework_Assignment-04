def link(value, next_node=None):                                    # Create a linked list
    return [value, next_node if next_node is not None else []]      # If next_node is None, create an empty list

def change(lnk, u, v):                                              # Replace the value of a node
    if lnk == []:                                                   # If the linked list is empty, return an empty list
        return []                                                   # Return an empty list
    else:
        current_value = v if lnk[0] == u else lnk[0]                # If the current value is equal to u, replace it with v
        return link(current_value, change(lnk[1], u, v))            # Recursively call the function to replace the value of the next node

def list_to_string(lnk):                                            # Convert the linked list to a string
    if lnk == []:                                                   # If the linked list is empty, return an empty list
        return "[]"                                                 # Return an empty list
    else:
        return f"[{lnk[0]}, {list_to_string(lnk[1])}]"              # Return the current value and the next node


def make_list():                                                    # Create a linked list
    values = input("\nType values for the linked list separated by commas ',' (e.g., 1,2,3): ").split(',')
    linked_list = []                                                # Create an empty linked list
    for val in reversed(values):                                    # Iterate through the values in reverse order
        linked_list = link(int(val.strip()), linked_list)           # Convert each value to integer and strip spaces
    return linked_list                                              # Return the linked list

def main():
    print("\n=== Create and Modify Linked List ===")
    user_linked_list = make_list()                                  # Create a user-defined linked list
    print("Original Linked List:", list_to_string(user_linked_list))        # Display the original linked list

    u = int(input("Type the existing value from the list to replace: "))
    v = int(input("Type the new value to replace with: "))
    modified_list = change(user_linked_list, u, v)                  # Replace the value of the node
    
    print("\n=== Result ===")
    print("Modified Linked List:", list_to_string(modified_list))   # Display the modified linked list

if __name__ == "__main__":
    while True:
        main()
        again = input("\nDo you want to use the program again? (y/n): ").lower()
        if again != 'y':
            print("Exiting the program...")
            break
