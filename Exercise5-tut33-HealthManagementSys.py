#Health management system
'''
suppose you are giving diet plan to your clienets may be for nutritions and weight loose and may be for spinal problem and muscle problem and you design
the diet for them and also you design exercise for them
'''
# '''
# 3 clients= Harry, Rohan, Hamad = for these people we have to manage the diet like what are they eating and they are doing exercise or not
# so you have to create 3 file for their foods for 3 people and 3 more files for their exercises so total 6 files you have to create
# ->write a function that when executes takes as input the client name
# ->create like press 1 for rohan and 2 for harry and 3 for Hamad
# ->now ask the user like what to want to check for suppose for 1 that means for Rohan i.e exercise or diet
# ->suppose 1 for exercise and 2 for diet and user entered 2 for Rohan means the diet
# ->then the diet will be printed
# ->then all these things like diet will be printed to the file
# function= use this funtion
# def getdate():
#     import datetime
#     return datetime.datetime.now()
#
# print tnito the file like this
# [timestamp] khana like chiken and roti and print a new line character
# ex= for exercise we can write
# [timestamp] cable crossover
#
# create one more funtion to retirve exercise or the food
# -> first ask 2 types of qs like
# do you want to lock or retrive
# and at the end it should display a message like perfect you locked it correctly
# '''

import datetime

def getdate():
    return datetime.datetime.now()

def log(c):
    if c==1:
        exf = int(input("Enter 1 for exercise and 2 for food\n"))
        if exf==1:
            value = input("Please type exercise here: ")
            with open("Harry_ex.txt", "a") as f:
                f.write("["+str(getdate())+"] : " +value+"\n")
            print("Successfully written")

        else:
            value = input("Please type food here : ")
            with open("Harry_food.txt", "a") as f:
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
            with open("Hamad_ex.txt", "a") as f:
                f.write("["+str(getdate())+"] : " +value+"\n")
            print("Successfully written")

        else:
            value = input("Please type food here : ")
            with open("Hamad_food.txt", "a") as f:
                f.write("["+str(getdate())+"] : " +value+ "\n")
            print("Successfully written")

def retrive(c):
    if c==1:
        print("What to do you want to check")
        exf = int(input("Enter 1 for exercise and 2 for food\n"))
        if exf==1:
            with open("Harry_ex.txt") as f:
                for i in f:
                    print(i, end="")

        else:
            with open("Harry_food.txt") as f:
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
            with open("Hamad_ex.txt") as f:
                for i in f:
                    print(i, end="")

        else:
            with open("Hamad_food.txt") as f:
                for i in f:
                    print(i, end="")

print("Health Management System: ")
lr = int(input("Enter 1 for Log and 2 for Retriving\n"))

if lr ==1:
    client = int(input("Enter 1 for Harry, 2 for Rohan and 3 for Hammad\n"))
    log(client)

else:
    client = int(input("Enter 1 for Harry, 2 for Rohan and 3 for Hammad\n"))
    retrive(client)

