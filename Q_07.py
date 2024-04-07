def link(value, next_node=None):                                # define function link with  value and next node as parameters
    return [value, next_node if next_node is not None else []]  # return a list containing the value and  the next node (or an empty list)

def empty():                                                    # define  an empty function called 'empty'
    return []                                                   # this function returns an empty list, i.e., [].

def apnd(lnk, m):                                               # define a new function called 'apnd', which takes two arguments lnk and m
    if lnk == empty():                                          # check if the list is empty
        return link(m)                                          # if it is, create a new linked list with m as its only element and return it
    else:
        head, tail = lnk[0], lnk[1]                             # separate the linked list into its head and tail elements
        if tail == empty():                                     # check if there are no more nodes in the linked
            return link(head, link(m))                          # add a new node to the head of the linked list with value m and return
        else:
            return link(head, apnd(tail, m))                    # append to linked list if not empty and return it

def make_list():                                                # define a function to create a new linked list and
    values = input("\nType the elements of the linked list separate by ','comma i.e.(1,2,3)\t: ").split(',')
    linked_list = empty()
    for val in reversed(values):
        linked_list = link(int(val.strip()), linked_list)       # create a new node with the value and add it to the front of the list
    return linked_list


def main():
    user_linked_list = make_list()
    print("Initial input Linked List enterd by user\t\t\t\t:", user_linked_list)
    m = int(input("Type the element to append to the end of the initial linked list\t: "))
    modified_list = apnd(user_linked_list, m)                   # appending a new node at the end of the linked list
    print("\n=== Result ===")
    print("Modified new Linked List:", modified_list)

if __name__ == "__main__":
    while True:
        main()
        again = input("\nDo you want to use the program again? (y/n): ").lower()
        if again != 'y':
            print("Exit the program...")
            break
