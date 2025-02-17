#Health management system

print("Welcome Health management system by Subhasree")
import datetime

def getdate():
    return datetime.datetime.now()

def log(c):
    if c==1:
        exf = int(input("Enter 1 for exercise and 2 for food\n"))
        if exf==1:
            value = input("Please type exercise here: ")
            with open("Priyagnee_ex.txt", "a") as f:
                f.write("["+str(getdate())+"] : " +value+"\n")
            print("Successfully written")

        else:
            value = input("Please type food here : ")
            with open("Priyagnee_food.txt", "a") as f:
                f.write("["+str(getdate())+"] : " +value+ "\n")
            print("Successfully written")

    elif c==2:
        exf = int(input("Enter 1 for exercise and 2 for food\n"))
        if exf==1:
            value = input("Please type exercise here: ")
            with open("Rohan_ex.txt", "a") as f:
                f.write("["+str(getdate())+"] : " +value+"\n")
            print("Successfully written")

        else:
            value = input("Please type food here : ")
            with open("Rohan_food.txt", "a") as f:
                f.write("["+str(getdate())+"] : " +value+ "\n")
            print("Successfully written")

    else:
        exf = int(input("Enter 1 for exercise and 2 for food\n"))
        if exf==1:
            value = input("Please type exercise here: ")
            with open("Goutam_ex.txt", "a") as f:
                f.write("["+str(getdate())+"] : " +value+"\n")
            print("Successfully written")

        else:
            value = input("Please type food here : ")
            with open("Goutam_food.txt", "a") as f:
                f.write("["+str(getdate())+"] : " +value+ "\n")
            print("Successfully written")

def retrive(c):
    if c==1:
        print("What to do you want to check")
        exf = int(input("Enter 1 for exercise and 2 for food\n"))
        if exf==1:
            with open("Priyagnee_ex.txt") as f:
                for i in f:
                    print(i, end="")

        else:
            with open("Priyagnee_food.txt") as f:
                for i in f:
                    print(i, end="")

    elif c == 2:
        print("What to do you want to check")
        exf = int(input("Enter 1 for exercise and 2 for food\n"))
        if exf == 1:
            with open("Rohan_ex.txt") as f:
                for i in f:
                    print(i, end="")

        else:
            with open("Rohan_food.txt") as f:
                for i in f:
                    print(i, end="")

    else:
        print("What to do you want to check")
        exf = int(input("Enter 1 for exercise and 2 for food\n"))
        if exf == 1:
            with open("Goutam_ex.txt") as f:
                for i in f:
                    print(i, end="")

        else:
            with open("Goutam_food.txt") as f:
                for i in f:
                    print(i, end="")

print("Health Management System: ")
lr = int(input("Enter 1 for Log and 2 for Retriving\n"))

if lr ==1:
    client = int(input("Enter 1 for Priyagnee, 2 for Rohan and 3 for Goutam\n"))
    log(client)

else:
    client = int(input("Enter 1 for Priyagnee, 2 for Rohan and 3 for Goutam\n"))
    retrive(client)

