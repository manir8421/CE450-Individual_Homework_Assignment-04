def link(value, next_node=None):    # Define a function to link a node to the next node
    return [value, next_node]       # Return a list containing the value and the next node

def empty():                        # Define a function to create an empty linked list
    return []                       # Return an empty list to signify the end of the linked list

def sum_lnk(lnk, g):                # Define a function to sum the elements of a linked list
    if not lnk:                     # Check if the linked list is empty
        return 0                    # If the linked list is empty, return 0
    else:
        return g(lnk[0]) + sum_lnk(lnk[1], g)                   # Apply function 'g' to the current node value and add it to the sum of the rest

def show_list(lnk):                 # Define a function to show the elements of a linked list
    if not lnk:                     # Base case: if the list is empty, return "[]"
        return "[]"                 # Return "[]" to signify the end of the linked list
    else:
        return f"[{lnk[0]}, {show_list(lnk[1])}]"               # Format the list as nested lists

def make_list():                    # Define a function to create a linked list from user input
    values = input("Type values for the linked list separated by a comma ',' (e.g., 1,2,3)\t: ").split(',')
    linked_list = empty()           # Initialize the linked list as empty
    for val in reversed(values):    # Iterate through each value in reverse order
        linked_list = link(int(val.strip()), linked_list)       # Convert to integer, strip spaces, and link
    return linked_list              # Return the linked list

def main():                         # Define a function to run the program
    print("\n=== Sum Linked List Elements ===")
    user_linked_list = make_list()  # Create a user-defined linked list
    print("Constructed Linked List:", show_list(user_linked_list))  # Print the constructed linked list
    
    sqr = lambda x: x * x           # Function to square an integer
    dbl = lambda y: 2 * y           # Function to double an integer
    
    print("Choose a function to apply:")
    print("  1: Square the elements")
    print("  2: Double the elements")
    choice = input("Enter your choice (1 or 2)\t\t: ").strip()
    
    print("=== Result ===")
    if choice == '1':
        print("Sum after applying 'sqr' (square):", sum_lnk(user_linked_list, sqr))     # Calculate and print the sum of squares of the elements
    elif choice == '2':
        print("Sum after applying 'dbl' (double):", sum_lnk(user_linked_list, dbl))     # Calculate and print the sum of doubles of the elements
    else:
        print("Invalid choice. Please select '1' for square or '2' for double.")        # Handle invalid input

if __name__ == "__main__":
    while True:
        main()
        again = input("\nDo you want to use the program again? (y/n): ").lower()
        if again != 'y':
            print("Exiting the program...")
            break
