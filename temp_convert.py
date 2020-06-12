temp_calc = True

print()
print("*** Temperature Converter (Celsius to Fahrenheit) ***")
prompt = "\nPress the Enter key to continue or type 'quit'. "
prompt += "\nPress CTRL + z to halt program execution. "
while temp_calc:
    choice = input(prompt)
    if choice == 'quit':
        break
    else:
        print()
        Celsius = int(input("Enter a temperature in Celsius: "))
 
        Fahrenheit = 9.0/5.0 * Celsius + 32
 
        print("Temperature:", Celsius, "Celsius = ", Fahrenheit, " F")
        print()
        repeat = input("Would you like to convert another temperature? (y/n) ")
        if repeat == 'n':
            temp_calc = False
        print()
print()
print("Terminating program - Goodbye!")