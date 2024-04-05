def link(value, next_node=None):
    return [value, next_node if next_node is not None else []]
'''define a function link that creates a node of a linked list.
each node is represent a two-element list: the node's value and a reference to the next node.
if the next_node parameter is not provided (or is None), it defaults to an empty list [],
representing the end of the list'''

def empty():
    return []
'''function that return an empty list [].
this represent an empty linked list or the end of a linked list'''

def insrt(l, elm, ind):
    def helper(l, elm, ind, current_index):
        if l == empty() or ind == current_index:
            return link(elm, l)
        else:
            head, tail = l[0], l[1]
            return link(head, helper(tail, elm, ind, current_index + 1))
    return helper(l, elm, ind, 0)
'''insrt is a function to insert an element elm at a specified index ind in a linked list l.
it define a nested function that take an additional argument, current_index, which tracks the
recursion depth or the current index in the list.
if l is empty or the current index matches the target index ind, elm is inserted at this position
by creating a new link with elm pointing to the remainder of the list l.
Otherwise, it deconstructs the list into head and tail, recursively calls itself with the tail,
and reconstructs the list by linking head with the result of the recursive call. This continues
until the condition to insert elm is met.
Finally, insrt starts the recursive process by calling helper with the initial list l, the element elm,
the target index ind, and 0 as the initial current_index.'''

def make_list():
    values = input("\nType the elements of the linked list separate by commas',' i.e.(1,2,3)\t: ").split(',')
    linked_list = empty()
    for val in reversed(values):
        linked_list = link(int(val.strip()), linked_list)
    return linked_list
'''prompt the user to input elements for the linked list, separated by commas.
split the input string into a list of values, reverses it to maintain the order when constructing the list backwards,
and iteratively creates the linked list using the link function.
and return the constructed linked list.'''

def main():
    user_linked_list = make_list()
    print("Initial Linked List entered by the user\t\t\t\t\t:", user_linked_list)
    elm = int(input("Type the new element to insert in the linked list\t\t\t: "))
    ind = int(input("Type the index, at which position insert the new element\t\t: "))
    modified_list = insrt(user_linked_list, elm, ind)
    print("\n=== Result ===")
    print("Modified new Linked List:", modified_list)

if __name__ == "__main__":
    while True:
        main()
        again = input("\nDo you want to use the program again? (y/n): ").lower()
        if again != 'y':
            print("Exit the program...")
            break
