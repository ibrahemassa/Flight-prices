import requests
import add_user

print("Welcome to Ibrahem's flight club.\nWe find the best flight deals")
first_name = input("What's your first name?\n")
last_name = input("What's your last name?\n")
while True:
    email = input("What's your eamil?\n")
    confirmation = input("Type your email again please\n")
    if email != confirmation:
        print("Unmatching emails!")
    else:
        break

print("Congrats, your are in the club!")

add_user.post_new_row(first_name, last_name, email)