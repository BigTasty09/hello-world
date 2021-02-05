Exercise 1
print ("Jose Perez")
print ("St Roberts CHS")
print ("8101 Leslie St, Thornhill, ON")
print ("Thornhill Ontario L3T 7P4")
print ("Canada")

Exercise 2
usertext = input("What is your name?")
print ("Hello", usertext )

Exercise 3
length = float(input("what is the length of the room?"))
width = float(input("What is the width of the room?"))
area = length*width 
print("The area is", area)

Exercise 5
less_deposit = 0.10
more_deposit = 0.25

less = int(input("How many 1 litre or less containers do you have? "))
more = int(input("How many larger than 1 litre containers do you have? "))

refund = less * less_deposit + more * more_deposit 

print("Your total refund is $%.2f." % refund)
