shopping_list = []

instructions = """
Enter 'DONE' to stop adding items.
Enter 'HELP' to show instructions.
Enter 'SHOW' to see your current list.
"""
print instructions
print "What should we pick up at the store? "

while True:
    user_input = raw_input("> ")

    if user_input == "SHOW":
        print "Here's your list so far:"
        for item in shopping_list:
            print item

    elif user_input == "HELP":
        print instructions

    elif user_input == "DONE":
        print "Here's your list:"
        for item in shopping_list:
            print item

        # Ask user if they want to save the list
        save_list = raw_input("Do you want to save your list? (y/n) ").lower()
        if save_list == "y":
            file_name = raw_input("Enter your file name: ")
            print "List saved!"
            saved_list = open(file_name, "w")
            saved_list.write(", ".join(shopping_list))
            saved_list.close()

        # Ask user if they want to make a new list
        new_list = raw_input("Do you want to make another list? (y/n) ").lower()
        if new_list == "y":
            shopping_list = []
            print instructions
            print "What should we pick up at the store? "
        else:
            print "Bye!"
            break

    # If user didn't say any keywords, add the item to the list and show the current list, start loop again
    else:
        shopping_list.append(user_input)
        print "Added %s. Shopping list now has %d items." % (user_input, len(shopping_list))
