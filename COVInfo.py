#Master Loop
import sys #imports sys for sys.exit command

#def yell(text): #function body
#    quarantine = "You need to quarantine"
#    quarantine = quarantine.upper()
#good style to leave a space after funciton
#def quarantine_Status(diagnosis, exposure):
#    return
#try:
diagnosis = str(input("Have you been diagnosed with COVID-19? (Y/N) ")).upper()
print("You answered " + '"' + diagnosis + '".')
if diagnosis == "Y":
    print("You may have COVID-19 and need to quarantine. CDC recommends quarantining for 10 days after exposure or diagnosis, until you have gone more than 24 hours without a fever.")#go to section on counting days in quarantiny")
elif diagnosis == "N":
    exposure = str(input("Have you had a recent known exposure to someone showing symptoms or with a positive diagnosis of COVID-19? ")).upper()
    if exposure == "Y":
        exposure_time = int(input("When was your last known exposure? (enter the number of days): "))
        try: exposure_time < 0
        except NameError as err:
            print("ValueError: Try again inputting a positive whole number instead.")
            print("({})".format(err))
        if exposure_time <=10:
            print("You have had a recent exposure. You need to quarantine")
        elif exposure_time >10:
            print("You have not had a recent exposure. You do not need to quarantine.")
        else:
            print("You have not had a recent exposure. You do not need to quarantine.")
quarantine_info = input("Would you like more information about quarantine? (Y/N)").upper()
if quarantine_info == "Y":
    print("Please visit www.cdc.gov for mor information.") 
else:
    print("Thank you for using COVInfo! The program will now exit.")   
try:
    temperature = float(input("What is your temperature in degrees Fahrenheit?  "))
except ValueError:
    print("Please enter a decimal number.")
measurement_count = 1
while temperature >100.4:
    if measurement_count >12:
            sys.exit("You can only take your temperature 12 times in a 24 hour period. This program will now terminate.")
    temperature = float(input("You have a fever. Please wait a at least two hours and try again. Now what is your temperature?  "))
measurement_count += 1
print("Congratulations, you do not have a fever! After 24 hours with no fever, you may exit quarantine.")
# Prompt user if they want to proceed. Y/N?
#time_infected == input("When did you receive your diagnosis?(enter the number of days)"):
#If they want to proceed
should_proceed = input("Do you want to know how long is left in your quarantine? Y/N ")
if should_proceed.lower() == "y":
    days_complete = int(input("How many days have you been in quarantine? ")) #expect a ValuError
quarantine_duration = 10
quarantine_duration_remaining = quarantine_duration - days_complete
        #except NameError:
print("There are {} days remaining in your quarantine.".format(quarantine_duration_remaining))#output how many days are left in the user's quarantine
#else:
    #print("Thank you for using COVinfo.")
#diagnosis = False
#symptoms = input("Do you have any COVID symptoms?")
#symptoms = True
#not diagnosis and not symptoms

#"hot dogs" != "sandwiches"  evaluates to True



#23 // 3  integer division
#23 % 4 #this will give you the remainder 