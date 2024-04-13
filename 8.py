def link(value, next_node=None):                                # define a function to create a linked list
    return [value, next_node if next_node is not None else []]  # return the linked list

def empty():                                                    # define a function to create an empty linked list
    return []                                                   # return the empty linked list

def insrt(l, elm, ind):                                         # Insert an element at a specified index in a linked list
    def helper(l, elm, ind, current_index):                     # Helper function to recursively traverse the linked list
        if l == empty() or ind == current_index:                # Insert new element if correct index is reached or at the end if index is out of bounds
            return link(elm, l)                                 # Return the new linked list
        else:
            return link(l[0], helper(l[1], elm, ind, current_index + 1))    # Recursively traverse to the correct index
    return helper(l, elm, ind, 0)                               # Call the helper function to insert the new element at the specified index

def make_list():                                                # Define a function to create a linked list from user input
    values = input("\nType the elements of the linked list separated by commas ',' (e.g., 1,2,3)\t: ").split(',')
    linked_list = empty()                                       # Create an empty linked list
    for val in values:                                          # Directly append each value to maintain input order and simplify
        linked_list = insrt(linked_list, int(val.strip()), len(linked_list))  # Use 'insrt' to append to the end of the list
    return linked_list                                          # Return the linked list


def list_to_string(lnk):                                        # Define a function to convert a linked list to a string
    if lnk == []:                                               # If the linked list is empty, return '[]'
        return "[]"                                             # Return '[]'
    else:
        return f"[{lnk[0]}, {list_to_string(lnk[1])}]"          # Return the linked list in string format

def main():
    user_linked_list = make_list()                              # Create a linked list from user input
    print("Initial Linked List entered by the user\t\t\t:", list_to_string(user_linked_list))
    elm = int(input("Type the new element to insert in the linked list\t\t\t: "))
    ind = int(input("Type the index, at which position to insert the new element\t: "))
    modified_list = insrt(user_linked_list, elm, ind)           # Insert the new element at the specified position
    print("\n=== Result ===")
    print("Modified new Linked List:", list_to_string(modified_list))   # Display the modified linked list

if __name__ == "__main__":
    while True:
        main()
        again = input("\nDo you want to use the program again? (y/n): ").lower()
        if again != 'y':
            print("Exiting the program...")
            break
