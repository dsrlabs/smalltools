# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name
print()
print("*** Distance Converter (km to mi) ***")
print()
prompt = "\nPress the Enter key to continue or type 'quit'. "
prompt += "\nPress CTRL + z to halt program execution. "

name = input("What us your name? ")
print()
print("Hi " + name + "!")
calculator = True

while calculator:
    choice = input(prompt)
    if choice == 'quit' or choice == 'QUIT':
        break
    else:
       
        print()
        distance_km = input('Enter distance in km: ')
        distance_mi = float(distance_km)/1.609
        print(f'{distance_km} km is equivalent to {round(distance_mi,1)} miles.')
        print()
        repeat = input("Would you like to calculate another MOI? (y/n) ")
        if repeat == 'n':
            calculator = False
            
# Indicates program termination
print()     
print("Terminating Program - Goodbye, " + name + "!")
import datetime
import time
now_date = datetime.date.today()
now_now = time.strftime("%H:%M %p")
print(f"Date: {now_date}\nTime: {now_now}")
print()