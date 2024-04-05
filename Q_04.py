def link(value, next_node=None):  # define function link that construct a single node of a linked list, value is the data stored in the node, next_node is an optional argument that references the next node in the list. It defaults to None
    return [value, next_node]
# function return two-element list: the first element is the node's value, and the second is a reference to the next node

def empty():
    return None
'''Defines a function empty that represents an empty list.
It simply returns None, which is used to signify the end of the list or entirely empty list '''

def srt(lnk):
    if lnk is None or lnk[1] is None:  # Base case: empty list or single element
        return True
    if lnk[0] > lnk[1][0]:  # Check if current node value is greater than the next node value
        return False
    return srt(lnk[1])  # Recursive call with the next node
'''srt check if the linked list lnk is sorted in ascending order.
The base case checks if the list is empty (lnk is None) or has a single element (lnk[1] is None). In either case, it is considered sorted, returning True.
It then checks if the current node's value (lnk[0]) is greater than the next node's value (lnk[1][0]). If so, the list is not sorted, and it returns False.
If none of the above conditions are met, it makes a recursive call to srt with the next node (lnk[1]), effectively moving down the list to repeat the checks. '''

def make_list():
    values = input("\nType values for the linked list separate by comma ',' i.e.(1,2,3): ").split(',')
    linked_list = empty()
    for val in reversed(values):
        linked_list = link(int(val.strip()), linked_list)  # Convert each value to integer and strip spaces
    return linked_list

def main():
    user_linked_list = make_list()
    print("=== Result ===")
    if srt(user_linked_list):
        print("True : The linked list is sorted in ascending order.")
    else:
        print("False : The linked list is not sorted in ascending order.")

if __name__ == "__main__":
    while True:  # Loop to allow the user to use the program repeatedly
        main()
        again = input("\nDo you want to use the program again? (y/n): ").lower()
        if again != 'y':
            print("Exit the program...")
            break
