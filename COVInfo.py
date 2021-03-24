#Master Loop
import sys #imports sys for sys.exit() command
quarantine_duration = 10
measurement_count = 1

print("Have you been diagnosed with COVID-19?")
diagnosis = str(input("Enter (Y/N) ")).upper()
print("You answered " + '"' + diagnosis + '".')
while diagnosis != "Y":
    if diagnosis == "N":
        exposure = str(input("Have you had a recent known exposure to someone showing symptoms or with a positive diagnosis of COVID-19? (Y/N) ")).upper() #gets stuck in a repeat loop now
    elif diagnosis != 'Y' or 'N':
        diagnosis = input("Invalid answer. Try again...\nEnter Y/N ") #how do I get this to break the loop if they enter a correct answer?
if diagnosis == "Y":
    try:
        time_infected = int(input("When did you receive your diagnosis? (enter the number of days): ")) #coerce this into an integer
    except ValueError:
            print ("Please enter a whole number.")
    while time_infected <0:
        print("Please enter a positive integer.")
        time_infected = int(input("When did you receive your diagnosis? (enter the number of days): "))#make this a loop until they put in the right type of information. currently crashes if NameError
        if time_infected <10:
                symptomatic = input("Are you showing symptoms? (Y/N) ").upper()
                if symptomatic == "Y":
                    print('You have COVID-19 and need to isolate. CDC recommends isolating for 10 days after symptoms first appear and you have gone at least 24 hours without fever-reducing medication, and symptoms have improved.  If you live with others, stay in a specific "sick room" or area and away from other people or animals, including pets. Use a separate bathroom, if available.')#go to section on counting days in quarantiny")
                    try:
                        temperature = float(input("What is your temperature in degrees Fahrenheit?  "))
                    except ValueError:
                        print("Please enter a decimal number.")
                    while temperature >100.4:
                        if measurement_count >12:
                            sys.exit("You can only take your temperature 12 times in a 24 hour period. This program will now terminate.")
                        temperature = float(input("You have a fever. Please wait a at least two hours and try again. Now what is your temperature?  "))
                if temperature <= 100.4:
                    print("Congratulations, you do not have a fever! After 24 hours with no fever-reducing medication, you may exit quarantine.")
                elif symptomatic != "Y":
                    print("""Stay home until after 10 days have passed since your positive test. If you live with others, stay in a specific "sick room" or area and away from other people or animals, including pets. Use a separate bathroom, if available.""")
        if time_infected >=10:
            print("You do not need to quarantine. The program will now exit.")
            sys.exit()
            if exposure == "Y":
                exposure_time = int(input("When was your last known exposure? (enter the number of days): ")).upper()
                try: exposure_time < 0
                except NameError as err:
                    print("NameError: Try again inputting a positive whole number instead.")
                    print("({})".format(err))
                except ValueError as err:
                    print("ValueError: Try again inputting a positive whole number instead.")
                    print("({})".format(err))
                if exposure_time <=10:
                    print("You have had a recent exposure. You need to quarantine")
                    quarantine_info = input("Would you like more information about quarantine or isolation? (Y/N)").upper()
                elif exposure_time >10:
                    print("You have not had a recent exposure. You do not need to quarantine.")
else:
    print("Please enter (Y/N)")
    diagnosis = str(input("Have you been diagnosed with COVID-19? (Y/N) ")).upper()
try: quarantine_info == "Y"
except NameError:
#    print("Please visit www.cdc.gov for mor information.")
#if quarantine_info != "Y":
#    sys.exit
#else:
    print("Thank you for using COVInfo! The program will now exit.")
    sys.exit()
measurement_count += 1
proceed = input("Do you want to continue? (Y/N) ").upper() # Prompt user if they want to proceed. Y/N?
if proceed == "Y": #If they want to proceed
    how_long_left = input("Do you want to know how long is left in your quarantine? Y/N ").upper()
    if how_long_left == "Y":
        days_complete = int(input("How many days have you been in quarantine? ")) #expect a ValuError
        quarantine_duration_remaining = quarantine_duration - days_complete
    elif how_long_left != "Y":
        print("Okay, thank you for using COVInfo! The program will now exit.")
        sys.exit()
        print(f"There are {quarantine_duration_remaining} days remaining in your quarantine.") #output how many days are left in the user's quarantine
else: print("Okay, thank you for using COVInfo! The program will now exit.")
sys.exit()
#try:
#    except NameError as err:
#    print("NameError: Try again inputting a positive whole number instead.")
#    print("({})".format(err))

#diagnosis = False
#symptoms = input("Do you have any COVID symptoms?")
#symptoms = True
#not diagnosis and not symptoms

#"hot dogs" != "sandwiches"  evaluates to True
#23 // 3  integer division
#23 % 4 #this will give you the remainder
#diagnosis = str(input("Have you been diagnosed with COVID-19? (Y/N) ")).upper() #How do I make this question loop until the user puts in the right value, instead of just repeating it a second time?
temperature_log = float([])#Temperature Log list
temperature_log.append(temperature)
temp_check = input("Would you like to know how many times you have recorded your temperature? (Y/N) ")
if temp_check == "Y":
    print("You have recorded your temperature {} times.").format(len(temperature_log))