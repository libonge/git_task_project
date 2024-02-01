validation_of_age
## Requests the user to enter their name
name = input("What is your name ? ")

# Validates the age input
while True:
    age = input("Enter your age : ")
    if age.isdigit() and 0 <= int(age) <= 150:
        break
    else:
        print("Invalid age! , Please enter a numerical value between 0 and 150.")

user_input = input(" Say something : ")
 
print (f'{name} said that " {user_input}. " ')

#Requests the the user to enter their name
name = input("what is your name ? ")
age = input("enter age ")

#Requests  the user to enter their thoughts
thoughts = input("what are your thinking of ? ")

#Print the user's name and thoughts
print(f"{name} is thinking of {thoughts} and is {age} years old.")

