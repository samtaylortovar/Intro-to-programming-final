import datetime

# Create a dictionary to store tasks with specific times
tasks = {}

def add_task(task, time):
    # Add the task to the dictionary with the specific time
    tasks[task] = time

def print_tasks():
    # Get the current time
    now = datetime.datetime.now()

    # Loop through the tasks and print them out if it's time
    for task, time in tasks.items():
        if now.time() >= time:
            print(f"Time to {task}!")

def main():
    while True:
        print("1. Add task")
        print("2. Print tasks")
        print("3. Quit")
        choice = input("What would you like to do? ")

        if choice == "1":
            task = input("Enter a task: ")
            hour = int(input("Enter the hour: "))
            minute = int(input("Enter the minute: "))
            time = datetime.time(hour, minute)
            add_task(task, time)
        elif choice == "2":
            print_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
