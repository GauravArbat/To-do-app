import mysql.connector as mysql

# Connect to MySQL
conn = mysql.connect(host="localhost", user="root", password="#Mayurkotwal7506")
cursor = conn.cursor()

# Create Database and Table
cursor.execute("CREATE DATABASE IF NOT EXISTS TODOAPP")
cursor.execute("USE TODOAPP")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_todo (
        id INT AUTO_INCREMENT PRIMARY KEY,
        task VARCHAR(50) NOT NULL,
        status ENUM('pending', 'completed') DEFAULT 'pending'
    )
""")

print("TODOAPP Initialized...\n")

# Menu Loop
while True:
    print("\n=== TODO APP MENU ===")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task = input("Enter the task: ")
        cursor.execute("INSERT INTO tb_todo (task) VALUES (%s)", (task,))
        conn.commit()
        print("Task added successfully!")

    elif choice == '2':
        cursor.execute("SELECT * FROM tb_todo")
        tasks = cursor.fetchall()
        if not tasks:
            print("No tasks found.")
        else:
            print("\n--- TASK LIST ---")
            for row in tasks:
                print(f"ID: {row[0]}, Task: {row[1]}, Status: {row[2]}")

    elif choice == '3':
        task_id = input("Enter the task ID to update status: ")
        new_status = input("Enter new status (pending/completed): ")
        if new_status not in ['pending', 'completed']:
            print("Invalid status entered.")
        else:
            cursor.execute("UPDATE tb_todo SET status=%s WHERE id=%s", (new_status, task_id))
            conn.commit()
            print("Task status updated.")

    elif choice == '4':
        task_id = input("Enter the task ID to delete: ")
        cursor.execute("DELETE FROM tb_todo WHERE id=%s", (task_id,))
        conn.commit()
        print("Task deleted.")

    elif choice == '5':
        print("Exiting TODO App. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
conn.close()
