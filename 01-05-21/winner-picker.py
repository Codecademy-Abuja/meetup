#This is a basic Python program that helps you pick a winner from a "n" list of attendees or users though random selection.
#From Codecademy Abuja Meetup

import random

#collect input from the user and store in a variable
name = input("Enter your name: \n")

print(f"Welcome {name}!")

print("I am built to help you select a winner through random process")

proceed = input("To proceed, hit 'Enter': \n")

#the number of attendees to be provided via input function
length_of_list = input("Enter total number of attendees: \n")

#convert input to int
length_of_list = int(length_of_list)

#random selection
random_winner = random.randint(1, length_of_list)

print("loading.....")
print("loading.........")
print("loading...........")

print(f"The winner is user - {random_winner}")