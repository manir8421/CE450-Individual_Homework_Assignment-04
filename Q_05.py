def link(value, next_node=None):
    return [value, next_node]
'''define function link that construct a new node for linked list, each node is represent by a 2-element list:
first element is the node's value, and second is reference to the next node. If no next node is provide, 
it default to None '''

def empty():
    return None
'''define function empty that represents an empty list by returning None.
This is useful for marking the end of the linked list '''

def sum_lnk(lnk, g):
    if lnk is None:  # check if the list is empty
        return 0
    else:
        return g(lnk[0]) + sum_lnk(lnk[1], g)  # apply g to the current element and recurse
'''define a function sum_lnk that recursively calculate the sum of the elements in the linked list lnk
after applying a function g to each element.
If the list is empty (lnk is None), it returns 0. Otherwise, it applies g to the current element (lnk[0]),
adds this to the sum of the rest of the list, and returns the total sum'''

def make_list():
    values = input("Type values for the linked list separate by comma ',' i.e.(1,2,3)\t: ").split(',')
    linked_list = empty()
    for val in reversed(values):
        linked_list = link(int(val.strip()), linked_list)  # Convert to integer and strip spaces
    return linked_list

def main():
    print("\n=== Sum Linked List Elements ===")
    user_linked_list = make_list() # call make_list to create a user-defined linked list
    
    # Define transformation functions
    sqr = lambda x: x * x
    dbl = lambda y: 2 * y
    # defines two lambda functions, sqr and dbl, to square or double an integer, respectively
    
    choice = input("Choose a function to apply ('sqr' for square, 'dbl' for double)\t\t: ").strip()
    print("=== Result ===")
    if choice == 'sqr':
        print("Sum after applying sqr:", sum_lnk(user_linked_list, sqr))
    elif choice == 'dbl':
        print("Sum after applying dbl:", sum_lnk(user_linked_list, dbl))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    while True:
        main()
        again = input("\nDo you want to use the program again? (y/n): ").lower()
        if again != 'y':
            print("Exit the program...")
            break
