def create_linked_list(elements):           # define a function to create a linked list
    if not elements:                        # if the list is empty
        return []                           # return an empty list
    else:
        return [elements[0], create_linked_list(elements[1:])]      # return a list with the first element and the rest of the list

def prnt_lnk(s):                            # define a function to print the linked list
    print("Constructed Linked List: ")      # print the constructed linked list
    print(f"{format_linked_list(s)}")       # print the linked list
    print("Your Linked List: ")             # print the user's linked list
    print(f"<{' '.join(map(str, flatten_linked_list(s)))}>")        # print the user's linked list

def format_linked_list(s):                  # define a function to format the linked list
    if not s:                               # if the list is empty
        return "[]"                         # return an empty list
    else:
        return f"[{s[0]}, {format_linked_list(s[1])}]"              # return a list with the first element and the rest of the list

def flatten_linked_list(s):                 # define a function to flatten the linked list
    result = []                             # define a list to store the flattened linked list
    while s:                                # while the list is not empty
        result.append(s[0])                 # append the first element to the list
        s = s[1]                            # set the list to the rest of the list
    return result                           # return the flattened linked list

def get_user_input():                       # define a function to get the user's input
    elements = input("\nEnter the linked list elements separated by commas (e.g., 1,2,3,4): ").split(',')
    elements = [element.strip() for element in elements]            # strip the elements
    return create_linked_list(elements)                             # return the linked list

def main():
    while True:
        user_linked_list = get_user_input()
        print("\n=== Result ===")
        prnt_lnk(user_linked_list)

        again = input("\nDo you want to use the program again? (y/n): ").lower()
        if again != 'y':
            print("Exiting the program...")
            break

if __name__ == "__main__":
    main()
