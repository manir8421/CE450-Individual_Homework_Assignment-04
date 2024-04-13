def make_linked_list(values):   # define a function that takes a list of values and returns a linked list
    if not values:              # if the list is empty, return an empty list
        return []               # return an empty list
    else:
        return [values[0], make_linked_list(values[1:])]    # return a list with the first element of the list and the rest of the list


def cntn_link(s, elm):          # define a function that takes a linked list and an element and returns a boolean value
    if not s:                   # if the linked list is empty, return False
        return False            # return False
    elif s[0] == elm:           # if the first element of the linked list is equal to the element, return True
        return True             # return True
    else:
        return cntn_link(s[1], elm)     # return the result of the function with the rest of the linked list and the element


def print_linked_list(s):               # define a function that takes a linked list and prints it
    print(format_linked_list(s))        # print the linked list


def format_linked_list(s):              # define a function that takes a linked list and returns a string
    if not s:                           # if the linked list is empty, return an empty string
        return "[]"                     # return an empty string
    else:   
        return f"[{s[0]}, {format_linked_list(s[1])}]"    # return a string with the first element of the linked list and the rest of the linked list


def user_input():                       # define a function that takes no arguments and returns a linked list
    node_values = input("\nEnter node's values, separate by commas (e.g., 1,2,3):\t")
    nodes = [node.strip() for node in node_values.split(',')]    # split the node values by commas and strip the values
    return make_linked_list(nodes)       # return the linked list


def main():
    while True:
        new_linked_list = user_input()
        print("Constructed Linked List:")
        print_linked_list(new_linked_list)

        search_element = input("Enter the element to search for:\t").strip()
        result = cntn_link(new_linked_list, search_element)

        print("\n=== Result ===")
        if result:
            print(f"True: The element '{search_element}' is present in the linked list.")
        else:
            print(f"False: The element '{search_element}' is not present in the linked list.")

        again = input("\nDo you want to use the program again? (y/n):\t").lower()
        if again != 'y':
            print("Exiting the program...")
            break

if __name__ == "__main__":
    main()
