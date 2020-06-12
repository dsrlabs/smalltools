# Moment of Inertia Calculator Version 1
# This program calculates the Moment of Inertia of a single stage model rocket.
# Numerical input validation code is not used in this program.

print()
print('-'*54)
print("Moment of Inertia (MOI) Calculator")
print("Created in MS Excel by Ryan S. Wescott")
print ("Ported to Python by Doug Ramsay, DSR Labs © 2020")
print('-'*54)
prompt = "\nPress the Enter key to continue or type 'quit'. "
prompt += "\nPress CTRL + z to halt program execution. "

# Set a flag to indicate MOI calculation is active
calculator = True

# Execute an indefinate iteration while loop to run or exit the program.
while calculator:
    choice = input(prompt)
    if choice == 'quit' or choice == 'QUIT':
        break
    else:
        print()
        rocketname = input("Rocket Name = ? ")
        dstrings = float(input("Distance between strings (cm) ? " ))
        mass = float(input("Rocket mass (g) = ? "))
        tperiods = float(input("10 periods (sec) = ? " ))
        strlen = float(input("Length of string (cm) = ? " ))
        g = 9.80665
# Unit conversion code
        dstrings_conv = dstrings/100
        mass_conv = mass/1000
        tperiods_conv = tperiods/10
        strlen_conv = strlen/100
        num = dstrings_conv*dstrings_conv*mass_conv*g*tperiods_conv*tperiods_conv
        den = 16*3.14159*strlen_conv
        moi = num/den
        print()
        print('-'*54)
        print("Rocket Name: " + rocketname.title())
        print(f"The Moment of Inertia is {moi:3f} kg/m2 ")
        print('-'*54)
        repeat = input("Would you like to calculate another MOI? (y/n) ")
        print('-'*54)
        if repeat == 'n':
            calculator = False
            
# Indicates program termination
print()     
print("Terminating Program")
import datetime
import time
now_date = datetime.date.today()
now_now = time.strftime("%H:%M %p")
print(f"Date: {now_date}\nTime: {now_now}")
print()