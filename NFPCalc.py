# Nike Fuel Points Calculator Version 1
# This program calculates the number of NikeFuel points (NFP) converted from Apple Watch active calories.
# NFP value is a rough estimate
# Numerical input validation code is not used in this program.

print()
print('-'*27)
print("Nike Fuel Points Calculator")
print("DSR Labs © 2020")
print('-'*27)
prompt = "\nPress the Enter key to continue or type 'quit'. "
print()
print("This program converts total number of")
print("Apple Watch active cals to NikeFuel points (NFP)")

# Set a flag to indicate MOI calculation is active
calculator = True

# Execute an indefinate iteration while loop to run or exit the program.
while calculator:
    choice = input(prompt)
    if choice == 'quit' or choice == 'QUIT':
        break
    else:
        print()
        aw_cals = input("Total Apple Watch Active Calories = ? ")
# Conversion equations
        nfpn = int(aw_cals)*3.84
        nfpd = 0.892
        a = nfpn/nfpd
        nfp = round(a)
        print(f"Equivalent NFP: {nfp} ")
        print()
        repeat = input("Would you like to ctry again? (y/n) ")
        if repeat == 'n':
            calculator = False         
# Indicates program termination
print()     
print("Remember: Life Is A Sport! Goodbye!")
import datetime
import time
now_date = datetime.date.today()
now_now = time.strftime("%H:%M %p")
print(f"Date: {now_date}\nTime: {now_now}")
print()