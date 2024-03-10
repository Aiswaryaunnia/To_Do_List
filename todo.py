 #Function to display the to-do list
def display_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("Your to-do list:")
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item}")

# Function to add an item to the to-do list
def add_item(todo_list, item):
    todo_list.append(item)
    print(f"Added '{item}' to your to-do list.")

# Function to remove an item from the to-do list
def remove_item(todo_list, index):
    if 1 <= index <= len(todo_list):
        removed_item = todo_list.pop(index - 1)
        print(f"Removed '{removed_item}' from your to-do list.")
    else:
        print("Invalid index!")

# Function to save the to-do list to a file
def save_list(todo_list, filename):
    with open(filename, 'w') as f:
        for item in todo_list:
            f.write(item + '\n')

# Function to load the to-do list from a file
def load_list(filename):
    todo_list = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                todo_list.append(line.strip())
    except FileNotFoundError:
        pass
    return todo_list

# Main function
def main():
    todo_list = load_list('todo_list.txt')

    while True:
        print("\nWhat would you like to do?")
        print("1. Display to-do list")
        print("2. Add item to to-do list")
        print("3. Remove item from to-do list")
        print("4. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_list(todo_list)
        elif choice == '2':
            item = input("Enter the item you want to add: ")
            add_item(todo_list, item)
        elif choice == '3':
            index = int(input("Enter the index of the item you want to remove: "))
            remove_item(todo_list, index)
        elif choice == '4':
            save_list(todo_list, 'todo_list.txt')
            print("Your to-do list has been saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()