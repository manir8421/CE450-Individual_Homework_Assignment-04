def link(value, next_node=None):                            # define function link that construct a single node of a linked list, value is the data stored in the node, next_node is an optional argument that references the next node in the list. It defaults to None
    return [value, next_node]                               #  Return the value and reference to the next node

def empty():                                                # Check if list is empty
    return None                                             # If empty, return None. Else, return False

def srt(lnk):                                               # Sorts a linked list using merge sort algorithm
    if lnk is None or lnk[1] is None:                       # Base case: empty list or single element
        return True                                         # Returns True (list is sorted)
    if lnk[0] > lnk[1][0]:                                  # Check if current node value is greater than the next node value
        return False                                        # return  False (list is not sorted)
    return srt(lnk[1])                                      # Recursive call with the next node

def make_list():                                            # Function to create an empty Linked List
    values = input("\nType values for the linked list separate by comma ',' i.e.(1,2,3): ").split(',')
    linked_list = empty()                                   # Create an empty Linked List
    for val in reversed(values):                            # Iterate over each value from last to first
        linked_list = link(int(val.strip()), linked_list)   # Convert each value to integer and strip spaces
    return linked_list

def main():
    user_linked_list = make_list()                          # Get the User's Linked List
    print("=== Result ===")
    if srt(user_linked_list):
        print("True : The linked list is sorted in ascending order.")
    else:
        print("False : The linked list is not sorted in ascending order.")

if __name__ == "__main__":
    while True:                                             # Loop to allow the user to use the program repeatedly
        main()
        again = input("\nDo you want to use the program again? (y/n): ").lower()
        if again != 'y':
            print("Exit the program...")
            break
