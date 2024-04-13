def link(value, next_node=None):                                # define a linked list
    return [value, next_node if next_node is not None else []]  # if next_node is None, return an empty list


def empty():                                                     # define an empty linked list
    return []                                                    # return an empty list

def apnd(lnk, m):                                                # append a new node at the end of the linked list
    if lnk == empty():                          # If the list is empty, create a new list with the element 'm'
        return link(m)                          # Return the new list
    else:
        return link(lnk[0], apnd(lnk[1], m))    # Recursively call apnd to reach the end of the list and append the element

def make_list():                                                 # define a function to create a linked list
    values = input("\nType the elements of the linked list separated by commas ',' (e.g., 1,2,3)\t: ").split(',')
    linked_list = empty()                       # Create an empty linked list
    for val in values:                          # Removed reversed to maintain the order of input directly
        linked_list = apnd(linked_list, int(val.strip()))           # Append each value to the linked list
    return linked_list                          # Return the linked list

def list_to_string(lnk):                        # define a function to convert a linked list to a string
    if lnk == []:                               # If the list is empty, return an empty string
        return "[]"                             # Return an empty string
    else:
        return f"[{lnk[0]}, {list_to_string(lnk[1])}]"              # Recursively call list_to_string to reach the end of the list


def main():
    user_linked_list = make_list()              # Create a linked list from user input
    print("Initial input Linked List entered by user:", list_to_string(user_linked_list))
    m = int(input("Type the element to append to the end of the initial linked list\t: "))
    modified_list = apnd(user_linked_list, m)   # Appending a new node at the end of the linked list
    print("\n=== Result ===")
    print("Modified new Linked List:", list_to_string(modified_list))

if __name__ == "__main__":
    while True:
        main()
        again = input("\nDo you want to use the program again? (y/n): ").lower()
        if again != 'y':
            print("Exit the program...")
            break
