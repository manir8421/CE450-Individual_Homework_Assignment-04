def cntn_link(s, elm):                                                          # define  a function to count the number of links in an element with parameters s and elm
    if s is None:                                                               # Check if the linked list s is (None). If it is, the search ends, and False is returned, indicating the element elm is not in the list   
        return False                       
    elif s[0] == elm:                                                           # Compares the current node's value (s[0]) to the search element elm. If they match, True is returned, indicating the element is found  
        return True                
    return cntn_link(s[1], elm)                                                 # call the function recursively with the rest of the string and element.

def make_linked_list(values):                                                   #  recursively build a linked list from the provided values list. Each element in values becomes a node in the linked list
    return fold_right(lambda value, acc: (value, acc), None, values)            # use fold right to build the linked list from


def fold_right(func, acc, lst):                                                 # recursive  function to perform right fold on list
    return acc if not lst else func(lst[0], fold_right(func, acc, lst[1:]))     #  recursion with tail call optimization (fold right) and return 


def user_input():                                                               #  get input from the user
    node_values = input("\nType node's values, separate by ',' commas i.e. (1,2,3)\t: ")
    nodes = [node.strip() for node in node_values.split(',')]                   # split and remove spaces
    return make_linked_list(nodes)                                              #  convert list to linked list

def main():
    while True:
        new_linked_list = user_input()                                          #  get a new linked list from the user
        search_element = input("Type the search_element to search for\t\t\t: ").strip()
        result = cntn_link(new_linked_list, search_element)                     #  check if element is in the linked list
        
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
