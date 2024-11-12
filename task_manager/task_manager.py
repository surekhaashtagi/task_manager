import json
import os
import argparse
from datetime import datetime

TASKS_FILE = 'tasks.json'

# Initialize the task list
def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description, due_date):
    """Add a task to the task list."""
    tasks = load_tasks()
    task = {
        'id': len(tasks) + 1,
        'description': description,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {description} (Due: {due_date})")

def view_tasks():
    """Display all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "Done" if task['completed'] else "Pending"
        print(f"ID: {task['id']} - {task['description']} (Due: {task['due_date']}) - Status: {status}")

def delete_task(task_id):
    """Delete a task by its ID."""
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f"Task with ID {task_id} has been deleted.")

def mark_complete(task_id):
    """Mark a task as completed."""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            save_tasks(tasks)
            print(f"Task ID {task_id} marked as completed.")
            return
    print(f"Task with ID {task_id} not found.")

def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    
    # Define subcommands
    subparsers = parser.add_subparsers(dest="command")
    
    # Subcommand to add a task
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", help="Description of the task")
    parser_add.add_argument("due_date", help="Due date of the task (YYYY-MM-DD)")
    
    # Subcommand to view tasks
    parser_view = subparsers.add_parser("view", help="View all tasks")
    
    # Subcommand to delete a task
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("task_id", type=int, help="ID of the task to delete")
    
    # Subcommand to mark a task as completed
    parser_complete = subparsers.add_parser("complete", help="Mark a task as completed")
    parser_complete.add_argument("task_id", type=int, help="ID of the task to mark as completed")
    
    args = parser.parse_args()
    
    # Execute command based on user input
    if args.command == "add":
        add_task(args.description, args.due_date)
    elif args.command == "view":
        view_tasks()
    elif args.command == "delete":
        delete_task(args.task_id)
    elif args.command == "complete":
        mark_complete(args.task_id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
