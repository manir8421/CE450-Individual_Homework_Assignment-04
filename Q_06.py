def link(value, next_node=None):  # define function link to create a new node of a linked list
    return [value, next_node if next_node is not None else []] #  return the value and reference to the next node, If next_node is not provided or is None, it defaults to an empty list [] to signify the end of the list

def change(lnk, u, v):  # recursively iterates through the linked list lnk, replacing every occurrence of the value u with v.
    if lnk == []:  # Base case: if the list is empty
        return []
    else:
        current_value = v if lnk[0] == u else lnk[0]  #  the current node's value equals u, it's replaced with v; otherwise, the current value is retained
        return link(current_value, change(lnk[1], u, v)) # link function is used to reconstruct the list with the replaced values

def list_to_string(lnk):
    elements = []
    while lnk != []:
        elements.append(str(lnk[0]))
        lnk = lnk[1]
    return ", ".join(elements)
'''convert a linked list to a string represent by iterating through the list and appending each value to a list of elements.
Join these elements with a comma and a space, returning a single string that represents the linked list's values. '''

def make_list():
    values = input("\nType values for the linked list separate by commas',' i.e.(1,2,3): ").split(',')
    linked_list = []
    for val in reversed(values):
        linked_list = link(int(val.strip()), linked_list)  # convert each value to integer and strip spaces
    return linked_list, values  # return both the linked list and the original input values for display

def main():
    user_linked_list, original_values = make_list()  # unpack the returned tuple to get both the list and original values
    inp = ", ".join(original_values)  # display the original values in a user-friendly format
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
