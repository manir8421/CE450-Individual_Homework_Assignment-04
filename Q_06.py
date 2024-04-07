def link(value, next_node=None):                                    # define function link to create a new node of a linked list
    return [value, next_node if next_node is not None else []]      #  return the value and reference to the next node, If next_node is not provided or is None, it defaults to an empty list [] to signify the end of the list

def change(lnk, u, v):                                              # recursively iterates through the linked list lnk, replacing every occurrence of the value u with v.
    if lnk == []:                                                   # Base case: if the list is empty
        return []                                                   # Return an empty list as there are no links to follow
    else:
        current_value = v if lnk[0] == u else lnk[0]                #  the current node's value equals u, it's replaced with v; otherwise, the current value is retained
        return link(current_value, change(lnk[1], u, v))            # link function is used to reconstruct the list with the replaced values

def list_to_string(lnk):                                            # Function to convert a linked list into a string
    elements = []                                                   # Create an empty list to store the elements of the
    while lnk != []:                                                # While there are still elements in the list
        elements.append(str(lnk[0]))                                # Add first element to list of elements
        lnk = lnk[1]                                                # Remove first element from linked list
    return ", ".join(elements)                                      # Join all elements in a string with commas

def make_list():                                                    # Function to create a new linked list with user input
    values = input("\nType values for the linked list separate by commas',' i.e.(1,2,3): ").split(',')
    linked_list = []
    for val in reversed(values):
        linked_list = link(int(val.strip()), linked_list)           # convert each value to integer and strip spaces
    return linked_list, values                                      # return both the linked list and the original input values for display

def main():
    user_linked_list, original_values = make_list()                 # unpack the returned tuple to get both the list and original values
    inp = ", ".join(original_values)                                # display the original values in a user-friendly format
    u = int(input(f"Type the existing value from the list [{inp}] to replace: "))
    v = int(input("Tope the new value to replace: "))
    modified_list = change(user_linked_list, u, v)
    print("\n=== Result ===")
    print("Modified Linked List:", modified_list)

if __name__ == "__main__":
    while True:
        main()
        again = input("\nDo you want to use the program again? (y/n): ").lower()
        if again != 'y':
            print("Exit the program...")
            break
