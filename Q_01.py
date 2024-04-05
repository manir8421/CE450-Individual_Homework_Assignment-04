def cntn_link(s, elm):  # cntn_link(s, elm) function checks if an element 'elm' exists within a linked list 's'
    if s is None:       # base case for recursion. If the linked list is empty (None), there's no element to find, it returns False
        return False
    elif s[0] == elm:   # if the current node's value (s[0]) is equal to the element 'elm'. If it is,then the function returns True
        return True
    return cntn_link(s[1], elm)  #  If the current node is not the one we're looking for, the function calls itself recursively with the rest of the list (s[1]). This step moves down the list one node at a time, checking each node's value against elm.

def make_linked_list(values):  # This function creates a linked list from a list of values using 'fold_right'
    return fold_right(lambda value, acc: (value, acc), None, values)
''' It uses the fold_right function to recursively build the linked list.
The lambda function takes two arguments: value (the current value to add to the linked list) 
and acc (the accumulator, which is the partially constructed linked list). It constructs
a tuple representing a node with value and acc (the rest of the list). Initially, acc is None, 
representing the end of the list. '''

def fold_right(func, acc, lst): # This is a recursive function that applies a function 'func' to each item in a list 'lst', right-to-left, accumulating a result
    return acc if not lst else func(lst[0], fold_right(func, acc, lst[1:]))
'''If lst is empty, it returns the accumulator acc. Otherwise,
it applies func to the first item in the list (lst[0]) and the 
result of recursively calling fold_right on the rest of the list (lst[1:]). 
This constructs the list from the end, attaching each preceding element to the front of the accumulated list. '''

def user_input():
    node_values = input("\nType node's values, separate by ',' commas i.e. (1,2,3)\t: ")
    nodes = [node.strip() for node in node_values.split(',')]   # Splits the input string into a list of strings, stripping whitespace from each input
    return make_linked_list(nodes)

def main():
    """Main function to control the flow of the program."""
    while True:
        new_linked_list = user_input()
        search_element = input("Type the search_element to search for\t\t\t: ").strip()

        result = cntn_link(new_linked_list, search_element) # Calls cntn_link to check if the element exists in the linked list
        
        print("\n=== Result ===")
        if result:
            print(f"True: The element '{search_element}' is present in the linked list.")
        else:
            print(f"False: The element '{search_element}' is not present in the linked list.")

        again = input("\nDo you want to use the program again? (y/n): ").lower()
        if again != 'y':
            print("Exit the program....")
            break

if __name__ == "__main__":
    main()
