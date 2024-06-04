import os
import time
import shutil
import random

# Displaying the operating system name
def display_os_name():
    os_name = "MyOS"
    print(f"Starting {os_name}...")
    time.sleep(2)
    print(f"Welcome to {os_name}!\n")

# Getting system specifications from the user
def get_system_specs():
    ram = input("Enter RAM size (GB): ")
    hard_drive = input("Enter hard drive size (GB): ")
    cores = input("Enter number of CPU cores: ")
    print(f"System specifications: RAM={ram}GB, Hard Drive={hard_drive}GB, Cores={cores}\n")

# Notepad application with auto-save and file management
def notepad():
    print("Welcome to Notepad.")
    while True:
        print("1. Create new file")
        print("2. Open existing file")
        print("3. Exit Notepad")
        choice = input("Choose an option: ")
        if choice == "1":
            file_name = input("Enter new file name: ")
            with open(file_name, "w") as file:
                print("Type your text below. Type 'EXIT' to quit.")
                while True:
                    text = input()
                    if text.upper() == "EXIT":
                        break
                    file.write(text + "\n")
                    file.flush()  # Auto-save
        elif choice == "2":
            print("Existing files:")
            files = [f for f in os.listdir() if os.path.isfile(f)]
            for file in files:
                print(file)
            file_name = input("Enter the name of the file to open: ")
            try:
                with open(file_name, "r") as file:
                    print("File content:")
                    print(file.read())
                action = input("Do you want to (1) Write to the file or (2) Only view it? Enter 1 or 2: ")
                if action == "1":
                    with open(file_name, "a") as file:
                        print("Type your text below. Type 'EXIT' to quit.")
                        while True:
                            text = input()
                            if text.upper() == "EXIT":
                                break
                            file.write(text + "\n")
                            file.flush()  # Auto-save
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "3":
            break
        else:
            print("Invalid option. Please try again.")

# Calculator application
def calculator():
    print("Welcome to Calculator. Enter 'exit' to quit.")
    while True:
        try:
            expression = input("Enter expression: ")
            if expression.lower() == "exit":
                break
            result = eval(expression)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

# Displaying current time
def display_time():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"Current time: {current_time}")

# Creating a file
def create_file():
    file_name = input("Enter file name to create: ")
    with open(file_name, 'w') as file:
        print(f"File '{file_name}' created successfully.")

# Moving a file
def move_file():
    src = input("Enter source file path: ")
    dst = input("Enter destination file path: ")
    try:
        shutil.move(src, dst)
        print(f"File moved from '{src}' to '{dst}'.")
    except Exception as e:
        print(f"Error: {e}")

# Copying a file
def copy_file():
    src = input("Enter source file path: ")
    dst = input("Enter destination file path: ")
    try:
        shutil.copy(src, dst)
        print(f"File copied from '{src}' to '{dst}'.")
    except Exception as e:
        print(f"Error: {e}")

# Deleting a file
def delete_file():
    file_name = input("Enter file name to delete: ")
    try:
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Checking file information
def check_file_info():
    file_name = input("Enter file name to check info: ")
    try:
        file_info = os.stat(file_name)
        print(f"File info for '{file_name}':\n{file_info}")
    except Exception as e:
        print(f"Error: {e}")

# Mini-game: Guess the number
def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0
    print("Guess the number between 1 and 100. Type 'exit' to quit.")
    while True:
        guess = input("Enter your guess: ")
        if guess.lower() == "exit":
            break
        attempts += 1
        guess = int(guess)
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

# Scheduling algorithm: Round Robin
def round_robin():
    print("Round Robin Scheduling")
    processes = []
    n = int(input("Enter number of processes: "))
    for i in range(n):
        process = {}
        process['pid'] = input(f"Enter process ID for process {i+1}: ")
        process['bt'] = int(input(f"Enter burst time for process {i+1}: "))
        processes.append(process)
    quantum = int(input("Enter time quantum: "))

    total_bt = sum(p['bt'] for p in processes)
    t = 0
    while total_bt > 0:
        for p in processes:
            if p['bt'] > 0:
                if p['bt'] > quantum:
                    print(f"Process {p['pid']} executed for {quantum} units.")
                    t += quantum
                    p['bt'] -= quantum
                    total_bt -= quantum
                else:
                    print(f"Process {p['pid']} executed for {p['bt']} units.")
                    t += p['bt']
                    total_bt -= p['bt']
                    p['bt'] = 0
    print(f"Total time: {t} units.")

# Scheduling algorithm: First Come First Serve
def first_come_first_serve():
    print("First Come First Serve Scheduling")
    processes = []
    n = int(input("Enter number of processes: "))
    for i in range(n):
        process = {}
        process['pid'] = input(f"Enter process ID for process {i+1}: ")
        process['bt'] = int(input(f"Enter burst time for process {i+1}: "))
        processes.append(process)
    
    t = 0
    for p in processes:
        print(f"Process {p['pid']} executed for {p['bt']} units.")
        t += p['bt']
    print(f"Total time: {t} units.")

# Scheduling algorithm: Shortest Job First
def shortest_job_first():
    print("Shortest Job First Scheduling")
    processes = []
    n = int(input("Enter number of processes: "))
    for i in range(n):
        process = {}
        process['pid'] = input(f"Enter process ID for process {i+1}: ")
        process['bt'] = int(input(f"Enter burst time for process {i+1}: "))
        processes.append(process)
    
    processes.sort(key=lambda x: x['bt'])
    
    t = 0
    for p in processes:
        print(f"Process {p['pid']} executed for {p['bt']} units.")
        t += p['bt']
    print(f"Total time: {t} units.")

# Memory management: Simple allocation
def memory_management():
    print("Simple Memory Management")
    memory_size = int(input("Enter total memory size (KB): "))
    allocations = []
    while True:
        print("1. Allocate memory")
        print("2. Free memory")
        print("3. Display memory")
        print("4. Exit memory management")
        choice = input("Choose an option: ")
        if choice == "1":
            process_id = input("Enter process ID: ")
            size = int(input("Enter memory size to allocate (KB): "))
            if sum(a['size'] for a in allocations) + size <= memory_size:
                allocations.append({'pid': process_id, 'size': size})
                print(f"Allocated {size}KB to process {process_id}.")
            else:
                print("Not enough memory available.")
        elif choice == "2":
            process_id = input("Enter process ID to free: ")
            allocations = [a for a in allocations if a['pid'] != process_id]
            print(f"Freed memory for process {process_id}.")
        elif choice == "3":
            print("Current memory allocations:")
            for a in allocations:
                print(f"Process {a['pid']}: {a['size']}KB")
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")

# Displaying available commands
def display_help():
    commands = """
    Available commands:
    1. Notepad - Open Notepad
    2. Calculator - Open Calculator
    3. Time - Display current time
    4. Create a File- Create a file
    5. Move a File - Move a file
    6. Copy a File- Copy a file
    7. Delete a File- Delete a file
    8. Info - Check file info
    9. Guess the Number - Play 'Guess the Number' game
    10. RoundRobin - Round Robin Scheduling
    11. First Come First Serve - First Come First Serve Scheduling
    12. Shortest JOb First - Shortest Job First Scheduling
    13. Memory Management- Memory Management
    14. Help - Display this help message
    15. Exit - Exit the OS
    """
    print(commands)

# Main function to run the OS simulator
def main():
    display_os_name()
    get_system_specs()
    display_help()

    while True:
        command = input("Enter command: ").lower()
        if command == "notepad":
            notepad()
        elif command == "calculator":
            calculator()
        elif command == "time":
            display_time()
        elif command == "create":
            create_file()
        elif command == "move":
            move_file()
        elif command == "copy":
            copy_file()
        elif command == "delete":
            delete_file()
        elif command == "info":
            check_file_info()
        elif command == "guess":
            guess_the_number()
        elif command == "roundrobin":
            round_robin()
        elif command == "fcfs":
            first_come_first_serve()
        elif command == "sjf":
            shortest_job_first()
        elif command == "memory":
            memory_management()
        elif command == "help":
            display_help()
        elif command == "exit":
            print("Exiting MyOS. Goodbye!")
            break
        else:
            print("Invalid command. Type 'help' to see the list of available commands.")

if __name__ == "__main__":
    main()
