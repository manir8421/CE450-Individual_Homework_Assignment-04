def prnt_lnk(s):                                            # function prints a representation of a linked list
    if s is None:                                           # Checks if the list is empty. If is None, it prints empty brackets <> and returns
        print("<>")
        return                                              #vprints nothing, just returns to the next line of code.
    elements = []                                           # Initialize an empty list to store the elements of the linked list for later
    while s is not None:                                    # Iterates each node of the linked list, The loop continues as long as the current node s is not None
        elements.append(str(s[0]))                          # Adds the current node's value (s[0]) as a string to the elements list. This converts the node value to a string
        s = s[1]                                            # Move to the next node in the linked list by updating s to s[1]
    print("<" + " ".join(elements) + ">")                   # Once all elements are collected, then joined into a single string with spaces between them and enclosed in brackets < >

def create_linked_list(elements):
    linked_list = None                                      # Initializes linked list as empty (None), which will serve as the end marker for the linked list
    for element in reversed(elements):                      #  Create a new linked list with the given elements in reverse order
        linked_list = (element, linked_list)                # The tuple contains the current element and reference to the next node
    return linked_list                                      # return the constructed linked list

def get_user_input():
    elements = input("\nType the linked list separate by ',' comma i.e.(1,2,3): ").split(',')
    elements = [element.strip() for element in elements]    # Strip whitespace from each element in the list, which clean the user input
    return create_linked_list(elements)                     # Pass the cleaned list of elements to create_linked_list to construct the linked list, then returns this linked list

def main():
    while True:                                             # Start an infinite loop that will run until user decides to exit
        user_linked_list = get_user_input()
        print("\n=== Result ===")
        print(f"Your Linked List:")
        prnt_lnk(user_linked_list)

        again = input("\nDo you want to use the program again? (y/n): ").lower()
        if again != 'y':
            print("Exit the program...")
            break

if __name__ == "__main__":
    main()
