def display() :
    print('\n\t"To-Do List"\nOptions available: ')
    print('''\t1.Add a task
        2.Remove a task
        3.View all tasks
        4.Mark task as completed
        5.View completed tasks
        6.Search task
        7.Clear all tasks
        8.Exit''')


def add_task(tasks):
    task = input('Enter a task : ')
    if task not in tasks:
        tasks.append(task)
        print(f'Task - "{task}" is added to the list of tasks.')
    else:
        print(f'Task - "{task}" is already in the list of tasks.')


def view_task(tasks):
    if len(tasks) != 0:
        print('List of tasks: ')
        for i in range(len(tasks)):
            print(f'{i+1}. {tasks[i]}')
    else:
        print('No Tasks Found.')


def remove_task(tasks):
    view_task(tasks)
    try:
        task_index = int(input('Enter task number to be removed: '))
        if 0 < task_index <= len(tasks) :
            print(f'Task - "{tasks.pop(task_index-1)}" is removed from the list of tasks.')
        else:
            print('Invalid task number...')
    except ValueError:
        print('Enter a valid number...')


def mark_completed(tasks, completed_tasks):
    view_task(tasks)
    try:
        task_index = int(input('Enter task number to be marked as completed: '))
        if 0 < task_index <= len(tasks) :
            completed_tasks.append(tasks[task_index-1])
            print(f'Task - "{tasks[task_index-1]}" marked as completed.')
        else:
            print('Invalid task number...')
    except ValueError:
        print('Enter a valid number...')


def view_completed(completed_tasks):
    if len(completed_tasks) != 0:
        print('List of tasks: ')
        for i in range(len(completed_tasks)):
            print(f'{i+1}. {completed_tasks[i]}')
    else:
        print('No Completed Tasks Found.')


def search_task(tasks):
    key = input('Enter keyword to search for: ')
    found_tasks = [i for i in tasks if key.lower() in i.lower()]
    if len(found_tasks) != 0:
        print('List of tasks: ')
        for i in range(len(found_tasks)):
            print(f'{i+1}. {found_tasks[i]}')
    else:
        print('No such tasks found.')


def clear_all(tasks):
    sure = input('Are you sure you want to clear all tasks? (y/n): ')
    if sure.lower() == 'y':
        tasks.clear()
        print('All tasks have been cleared.')
    elif sure.lower() == 'n':
        print('Cancelled "clear" operation.')
    else:
        print('Wrong input given.')


def main():
    tasks = []
    completed_tasks = []

    while True:
        display()
        try:
            choice = int(input('Choose an option(0-8): '))
            match choice:
                case 1:
                    add_task(tasks)
                case 2:
                    remove_task(tasks)
                case 3:
                    view_task(tasks)
                case 4:
                    mark_completed(tasks, completed_tasks)
                case 5:
                    view_completed(completed_tasks)
                case 6:
                    search_task(tasks)
                case 7:
                    clear_all(tasks)
                case 8:
                    print('Exiting...')
                    break
                case _ :
                    print('Invalid choice...')
        except ValueError:
            print('Enter a valid number...')


if __name__ == "__main__" :
    main()

