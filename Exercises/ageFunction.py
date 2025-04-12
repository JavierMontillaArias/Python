#Function

def checkDriverAge(age):
    
    if age < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif age == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
    else:
        print("Powering On. Enjoy the ride!")


#main

checkDriverAge(92)