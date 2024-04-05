def link(value, next_node=None):
    return [value, next_node if next_node is not None else []]
'''create a new node (element) of a linked list.
Each node is a list containing a value and a reference to the next_node.
If next_node is not specified, it defaults to an empty list [], indicating the end of the list'''

def empty():
    return []
'''return an empty list [], representing an empty linked list.
This function represent an empty list'''

def apnd(lnk, m):
    if lnk == empty():  # check if the list is empty
        return link(m)
    else:
        head, tail = lnk[0], lnk[1]
        if tail == empty():
            return link(head, link(m))
        else:
            return link(head, apnd(tail, m))
'''recursively appends an element m to the end of the linked list lnk.
If lnk is empty, link(m) creates a new list with m as its only element.
Otherwise, it deconstructs lnk into its head (first value) and tail (the rest of the list),
then recursively applies itself to tail until it reaches the end of the list, where it appends m.'''

def make_list():
    values = input("\nType the elements of the linked list separate by ','comma i.e.(1,2,3)\t: ").split(',')
    linked_list = empty()
    for val in reversed(values):
        linked_list = link(int(val.strip()), linked_list)
    return linked_list
'''prompt the user to enter values separated by commas to create a linked list.
it process the input string, reverse the order of value to maintain the order when constructing the list backward,
and convert each to an integer and strip any whitespace.
for each value, it call link to add the value to the list, effectively building the list from the end to the start.'''

def main():
    user_linked_list = make_list()
    print("Initial input Linked List enterd by user\t\t\t\t:", user_linked_list)
    m = int(input("Type the element to append to the end of the initial linked list\t: "))
    modified_list = apnd(user_linked_list, m) 
    print("\n=== Result ===")
    print("Modified new Linked List:", modified_list)

if __name__ == "__main__":
    while True:
        main()
        again = input("\nDo you want to use the program again? (y/n): ").lower()
        if again != 'y':
            print("Exit the program...")
            break
