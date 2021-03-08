diagnosis = input("Have you been diagnosed with COVID? (type 'yes' or 'no') ")
print("You answered", diagnosis)
if diagnosis == "yes":
    print("You have COVID")
else:
    print("You do not have Covid:")

#diagnosis = False
#symptoms = input("Do you have any COVID symptoms?")
#symptoms = True
#not diagnosis and not symptoms

exposure = input("When was your last known exposure? (enter the number of days)")
print("It has been", exposure, " days since your last exposure.")
if exposure == <10:
    print("You have had a recent exposure.")
    print("You need to quarantine")