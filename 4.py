def link(value, next_node=None):            # Define a function to link a node to the next node
    return [value, next_node]               # Return the value and reference to the next node

def empty():                                # Define a function to return an empty list
    return []                               # Return an empty list instead of None

def srt(lnk):                               # Define a function to check if the linked list is sorted
    if lnk == [] or lnk[1] == []:           # Base case: empty list or single element
        return True                         # Returns True (list is sorted)
    if lnk[0] > lnk[1][0]:                  # Check if current node value is greater than the next node value
        return False                        # Return False (list is not sorted)
    return srt(lnk[1])                      # Recursive call with the next node

def make_list():                            # Define a function to make a linked list
    values = input("\nType values for the linked list separated by comma ',' (e.g., 1,2,3): ").split(',')
    linked_list = empty()                   # Initialize with an empty linked list
    for val in reversed(values):            # Iterate over each value from last to first to maintain order
        linked_list = link(int(val.strip()), linked_list)           # Convert each value to integer, strip spaces and link
    return linked_list                      # Return the linked list

def show_list(linked_list):                 # Define a function to display the linked list
    if linked_list == []:                   # Base case: if the list is empty, return "[]".
        return "[]"                         # Return "[]"
    else:
        return f"[{linked_list[0]}, {show_list(linked_list[1])}]"   # Return the value and the next node

def main():
    user_linked_list = make_list()          # Get the User's Linked List
    print("=== Result ===")
    print("Constructed Linked List:", show_list(user_linked_list))  # Display the constructed linked list
    if srt(user_linked_list):               # Check if the linked list is sorted
        print("True: The linked list is sorted in ascending order.")
    else:
        print("False: The linked list is not sorted in ascending order.")

if __name__ == "__main__":
    while True:                             # Loop to allow the user to use the program repeatedly
        main()
        again = input("\nDo you want to use the program again? (y/n): ").lower()
        if again != 'y':
            print("Exit the program...")
            break
