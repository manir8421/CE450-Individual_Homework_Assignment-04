def link(value, next_node=None):                                    # define a function link with  parameters value and next_node
    return [value, next_node if next_node is not None else []]      # Return the value and reference to the next node in a list

def empty():                                                        # define  an empty function called "empty" with no parameters
    return []                                                       # return  an empty array if the input is not valid.

def insrt(l, elm, ind):                                             # define  a function to insert an element at the given index in list.
    def helper(l, elm, ind, current_index):                         # define function helper  to find the element in list l with value
        if l == empty() or ind == current_index:                    # If the list is empty, return None. Otherwise, get the element at index
            return link(elm, l)                                     # return  the linked element
        else:
            head, tail = l[0], l[1]                                 # head  and tail of list are extracted from tuple
            return link(head, helper(tail, elm, ind, current_index + 1))        # call recursively to add tail of list
    return helper(l, elm, ind, 0)                                   # return  the result of the recursive call

def make_list():                                                    # define  a function to create an empty list
    values = input("\nType the elements of the linked list separate by commas',' i.e.(1,2,3)\t: ").split(',')
    linked_list = empty()                                           # create an empty linked list
    for val in reversed(values):                                    # insert each value in reverse order
        linked_list = link(int(val.strip()), linked_list)           # convert and add to the linked list
    return linked_list                                              # return the created linked list

def main():
    user_linked_list = make_list()
    print("Initial Linked List entered by the user\t\t\t\t\t:", user_linked_list)
    elm = int(input("Type the new element to insert in the linked list\t\t\t: "))
    ind = int(input("Type the index, at which position insert the new element\t\t: "))
    modified_list = insrt(user_linked_list, elm, ind)               # insert the new element in the specified position
    print("\n=== Result ===")
    print("Modified new Linked List:", modified_list)

if __name__ == "__main__":
    while True:
        main()
        again = input("\nDo you want to use the program again? (y/n): ").lower()
        if again != 'y':
            print("Exit the program...")
            break
