def link(value, next_node=None):                                #  define function link with  value and next node as parameters
    return [value, next_node]                                   # return  a list containing the value and next node

def empty():                                                    #  define an empty function called 'empty'
    return None                                                 # return None if linked list is empty

def sum_lnk(lnk, g):                                            #   define a recursive function to calculate the sum of values in a linked list lnk
    if lnk is None:                                             # check if linked list object (lnk) exists
        return 0                                                # if not exist then return 0
    else:
        return g(lnk[0]) + sum_lnk(lnk[1], g)                   # call recursive function g to get the value of current node and add it to the result

def make_list():                                                # create a new empty linked list
    values = input("Type values for the linked list separate by comma ',' i.e.(1,2,3)\t: ").split(',')
    linked_list = empty()                                       #  initialize linked list to None
    for val in reversed(values):                                # loop through each element of the list in reverse order
        linked_list = link(int(val.strip()), linked_list)       # Convert to integer and strip spaces
    return linked_list

def main():
    print("\n=== Sum Linked List Elements ===")
    user_linked_list = make_list()                              # call make_list to create a user-defined linked list
    
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
