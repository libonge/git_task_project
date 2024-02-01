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