# create a program in loop add some items add remove it also print 
# you want to exit the game using exit option


task=[]
while True:
    choice=input("enter the tasks(add/remove/print/exit):")
    if choice=="add":
        task.append(input("enter task items:").split(","))
        print("task added successfully!")
    elif choice=="remove":
        task="" # we did not remove all the items in string as a default method
        print("task removed successfully!")
    elif choice=="print":
        if task:
            print("todays task:")
            for i in task:
                print(i)
        else:
            print("no task")
    elif choice=="exit":
       break
    else:
        print("invalid option")