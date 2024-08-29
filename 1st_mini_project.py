# FOR DOING RANDOM NUMBER WE CAN USE " RANDOM " MODULE WHICH HAS MANY FUNCATION
# THIS IS IN BUILT MODULE BUT WE HACE TO IMPORTE THIS
import random
Target=int(random.randint(1,100)) #THIS FUNCATION HAS POWER TO CREATE RANDOM NUBER IN GIVEN 1 TO 10M RANGE
print(Target)
# print(type(data))
while True:
    user_number=input("enter your number in between 1 to 100  or Quite (Q): -> ")
    if (user_number=='Q' or user_number=='q'):
        break
    user_number=int(user_number)
    if user_number==Target:
        print("---SUCCESS---")
        break
    elif user_number<Target:
        print("your number is smaller than target : ")
    else:
        print("your number is bigger than target : ")

print("---GAME0VER---")
