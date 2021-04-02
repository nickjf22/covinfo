"""COVInfo Application
Created: 2021
Author: Nicholas Johnson
"""

import sys #imports sys for sys.exit() command
# Project Requirement 3: Read data from an external CSV file, and use that data in your application
cdc_file = open("cdc_info.txt", encoding="utf-8") # imports latest CDC data used to determine temperature and quarantine duration fields
data = cdc_file.read() #read the file
cdc_file.close() #closes it out of memory

# Project Requirement 1: "Master Loop" console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program
# Project Requirement 1: "Master Loop" console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program
def show_help():
    print("Welcome to the COVInfo help section.")
    print("""
"DONE" to quit.
"HELP" for this help.
"SHOW" to see your current log.
Enter a temperature to add it to your temperature log.
Or "CONT" to continue to the main program.
""")
temperature_log = []
def add_temperature(temp):#Create a function named add_temperature that declares a paramater named item
    #add the temperature to the list
    temperature_log.append(temp)
    # Notify user taht the item was added, and state the number of items in the list currently
    print("Temperature successfully added! You logs has {} entries in it.".format(len(temperature_log)))

# Define a function named show_log that prints all the entries in the log
def show_log():
    print("Here's your temperature log:")
    for temp in temperature_log:
        print(temp)

show_help()
while True:
        new_item = input("> ").upper()
        if new_item.upper() == "DONE":
            sys.exit() #causes the loop to immediately end, (could make it so the program flow jumps to the code after the loop.)
        elif new_item.upper() == "HELP":
            show_help()
            continue #puts back to 'while true' immediately; causes the loop to start the next iteration (ending the current one, but not the loop itself).
        # Enable the SHOW command to show the list.
        elif new_item.upper() == "SHOW":
            show_log()
            continue
        elif new_item.upper() == "CONT":
            break
        # Call add_temperature with new_temperature as an argument
        add_temperature(new_item)


quarantine_duration = 10
measurement_count = 1

print("Have you recently been diagnosed with COVID-19?")
diagnosis = str(input("Enter (Y/N) ")).upper()
print("You answered " + '"' + diagnosis + '".')
while diagnosis != "Y": #will evaluate until their condition evaluates as false
    if diagnosis == "N":
        exposure = str(input("Have you had a recent known exposure to someone showing symptoms or with a positive diagnosis of COVID-19? (Y/N) ")).upper() #gets stuck in a repeat loop now
        if exposure == "N":
            print("You have not had a recent diagnosis or recent exposure, so you do not need to quarantine or isolate. The program will now quit.")
            sys.exit()
        elif exposure == "Y":
            exposure_time = int(input("When was your last known exposure? (enter the number of days): "))
            try: exposure_time < 0
            except NameError as err:
                print("NameError: Try again inputting a positive whole number instead.")
                print("({})".format(err))
            except ValueError as err:
                print("ValueError: Try again inputting a positive whole number instead.")
                print("({})".format(err))
            if exposure_time <=10:
                print("You need to monitor yourself for symptoms for {} more days per the most recent CDC guidlines. Please visit www.cdc.gov for more information.".format(quarantine_duration - exposure_time))
                quarantine_info = input("Would you like more information about quarantine or isolation? (Y/N): ").upper()
                if quarantine_info == "Y":
                    print("Please visit www.cdc.gov for more information. The program will now exit.")
                    sys.exit()
                elif quarantine_info != "Y" or "N":
                    print("Invalid input, please enter (Y/N): ")
                    quarantine_info = input("Would you like more information about quarantine or isolation? (Y/N): ").upper()
                elif quarantine_info == "N":
                    print("Thank you for using COVInfo! The program will now exit.")
                    sys.exit()
                else:
                    print("Thank you for using COVInfo! The program will now exit.")
                    sys.exit()
            elif exposure_time >10:
                print("You have not had a recent exposure. You do not need to quarantine. The program will now quit.")
            sys.exit()
    elif diagnosis != "Y" or "N":
        diagnosis = input("Invalid answer. Try again...\nEnter Y/N ") #how do I get this to break the loop if they enter a correct answer?
if diagnosis == "Y":
    while True:
        time_infected = input("When did you receive your diagnosis? (enter the number of days): ")
        try:
            #temperature = int(temperature)
            time_infected = int(time_infected)
        except ValueError:
            print("Invalid input. Please enter a decimal number.")
            continue
        else:
            break
    #while true:
        try:
            time_infected < 0
        except ValueError:
            print("Invalid input. Please enter a positive whole number.")
            continue
    else: time_infected < 10
    symptomatic = input("Are you showing symptoms? (Y/N) ").upper()
if symptomatic == "Y":
    print('You have COVID-19 and need to isolate. CDC recommends isolating for {} days after symptoms first appear and you have gone at least 24 hours without fever-reducing medication, and symptoms have improved.  If you live with others, stay in a specific "sick room" or area and away from other people or animals, including pets. Use a separate bathroom, if available.'.format(quarantine_duration))#go to section on counting days in quarantiny")
while True:
    print("CDC Guidance says a temperature of", data, " degrees F or higher constitutes a fever.")
    temperature = float(input("What is your temperature in degrees Fahrenheit?: "))
    try:
        temperature = int(temperature)
    except ValueError:
        print("Invalid input. Please enter a decimal number.")
        continue
    else:
        break
while temperature >100.4:
    if measurement_count >12:
        sys.exit("You can only take your temperature 12 times in a 24 hour period.\n This program will now terminate.") #new line character
    temperature = float(input("You have a fever. Please wait a at least two hours and try again. Now what is your temperature?  "))
    if temperature <= 100.4:
        print("Congratulations, you do not have a fever! After 24 hours with no fever-reducing medication, you may exit quarantine.")
    elif symptomatic != "Y":
        print("""Stay home until after 10 days have passed since your positive test. If you live with others, stay in a specific "sick room" or area and away from other people or animals, including pets. Use a separate bathroom, if available.""")
    elif time_infected >=10:
        print("You do not need to quarantine. The program will now exit.")
        sys.exit()
else:
    #try: 
    quarantine_info = input("Would you like more information about quarantine or isolation? (Y/N)").upper()
    if quarantine_info == "Y":
        print("Please visit www.cdc.gov for more information. The program will now exit.")
        sys.exit()
    elif quarantine_info != "Y":
        print("Invalid input, please enter (Y/N): ")
    else:
        print("Thank you for using COVInfo! The program will now exit.")
        sys.exit()
measurement_count += 1
proceed = input("Do you want to continue? (Y/N) ").upper() # Prompt user if they want to proceed. Y/N?
if proceed == "Y": #If they want to proceed
    how_long_left = input("Do you want to know how long is left in your quarantine? Y/N ").upper()
    if how_long_left == "Y":
        days_complete = int(input("How many days have you been in quarantine? ")) #expect a ValuError
        quarantine_duration_remaining = quarantine_duration - days_complete
        print(f"There are {quarantine_duration_remaining} days remaining in your quarantine.") #output how many days are left in the user's quarantine
    elif how_long_left != "Y":
        print("Okay, thank you for using COVInfo! The program will now exit.")
        sys.exit()
else: print("Okay, thank you for using COVInfo! The program will now exit.")
print("Here is your log of temperatures: ")
show_log()
sys.exit()


# Project Requirement 2: Create a list, populate it with several values, retrieve at least one value, and use it in your program
