class Junction:    # declares a class named Junction, which represent each "junction" in the linked list
    def __init__(self, value, next_junction=None):   #  is the constructor for the Junction class. It initializes a new instance of the class
        self.value = value
        self.next_junction = next_junction

def rvrs_lnk(s):   # define function to reverse a linked list. s is the start node of the list
    reverse_list = None   # initializes the reversed list as None. This will become the new head of the reversed list
    while s:              # loop that continues as long as s is not None
        reverse_list = link(s.value, reverse_list)   # call link function to prepend the current node's value to the reversed list
        s = s.next_junction    # move to the next node in the original list
    return reverse_list    # return the head of the reverse list after all node have been processed

def link(s, next_junction):  # define function that create a new link in the list, It returns a two-element list: the value of the node and a reference to the next node
    return [s, next_junction]

def show_list(linked_list):  # define a recursive function to display the linked list
    if linked_list is None:  # handles the base case of the recursion. If the list is empty, it returns "[]".
        return "[]"
    
    return "[" + str(linked_list[0]) + ", " + show_list(linked_list[1]) + "]"
'''construct a string representation of the list by concatenating the current value and the string
representation of the rest of the list. '''

def make_list():
    values = input("\nType values for the linked list separate by comma ',' i.e.(1,2,3): ").split(',')
    linked_list = None
    
    for val in reversed(values):
        linked_list = Junction(val.strip(), linked_list)  # .strip() removes any whitespace
    
    return linked_list

def main():
    user_linked_list = make_list()
    reversed_linked_list = rvrs_lnk(user_linked_list)
    
    print("=== Result ===")
    print("Reversed Linked List:", show_list(reversed_linked_list))

if __name__ == "__main__":
    while True:  # loop allows the user to use the program repeatedly
        main()
        again = input("\nDo you want to use the program again? (y/n): ").lower()
        if again != 'y':
            print("Exit the program...")
            break
