#to do list app manager
import datetime
def task():
    tasks = []
    print("----Welcome to the task management app!----")
    total_tasks = int(input("Enter number of tasks you want to add in your app:"))
    for i in range(1,total_tasks+1):
        task = input(f"Enter task{i}")
        tasks.append(task)
    print("date and time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("today`s taks are:",tasks)
    while True:
        "1. add"
        "2. remove(mark done)"
        "3. update"
        "4. sort"
        "5. delete"
        "6. view"
        "7. exit"
        functions = int(input("Enterthe functions you want to add in!"))
        if functions ==1:
            add = input("Enter the task you want to add!")
            tasks.append(add)
            print(f"the {add} has added!")
        elif functions ==2:
            remove_t = input("Enter the task you want to remove:")
            if remove_t in tasks:
                tasks.remove(remove_t)
                print(f"the {remove_t} has removed!")
        elif functions ==3:
            update_t= input("Enter the task you want to update:")
            if update_t in tasks:
                new = input("Enter new task you want to update")
                ind = tasks.index(update_t)
                tasks[ind] = new
                
                print(f"the {update_t} has updated!")
            else:
                print("invaild")
        elif functions ==4:
            tasks.sort()
            print(f"the {tasks} has sorted!")
        elif functions ==5:
            del_t= input("Enter the task you want to delete:")
            if del_t in tasks:
                ind = tasks.index(del_t)
                del tasks[ind]
                print(f"the {del_t} has deleted!")
            else:
                print("invaild!")
        elif functions ==6:
            print(f"the total tasks- {tasks}")
        elif functions ==7:
            break
        else:
            print("invaild choice!")
    return tasks

print(task())