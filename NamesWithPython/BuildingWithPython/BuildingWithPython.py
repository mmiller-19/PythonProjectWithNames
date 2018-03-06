##Name input in Python

##First Name input
firstName = input("What is your first name? ")
print("")
print("Your first name is " + firstName)
print("")

##Last Name input
lastName = input("What is your last name? ")
print("")
print("Your last name is " + lastName)

print("")
##Full Name
print("Your full name is " + firstName + " " + lastName)

##Full Name for counting 
fullName = firstName + lastName
print("")

print("The number of letters in your first name is: " + str(len(firstName)))
print("")
print("The number of letters in your last name is: " + str(len(lastName)))
print("")
print("The number of letters in your full name is: " + str(len(fullName)))