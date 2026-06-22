### Shopping Manager List ###

def Manager_list():
    shopping_list = []

### This line codes asks user what action they would like to take ###
    while True:
        action = input("\nWhat would you like to do? (add / view / remove / done): ").strip().lower()

        if action == "add":
            item = input("Enter item to add: ").strip()
            shopping_list.append(item)
            print(f" '{item}' added to your list.")

### This line has function of showing lists, "enumerate" shows list with index number as well ###
        elif action == "view":
            if shopping_list:
                print("\n your shopping list: ")
                for i, item in enumerate(shopping_list, start=1):
                    print(f" {i}. {item}")
                
            else:
                    print("Your list is empty")
        
### This line removes specific item from lists ###
        elif action == "remove":
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f" '{item}' removed from your list.")

            else:
                print(f" '{item}' could not be found")

        elif action == "done":
            print("Good Bye")
            break

        else:

            print("not available options")


Manager_list()
