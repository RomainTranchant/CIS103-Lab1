# Lab 1: Getting Started with Python
# CIS 103: : Introduction to Programming
# Instructor: MD Ali
# Student Name: Romain Tranchant
# Date: 08/26/2024

# This script prints a personalized greeting message and demonstrates
# the use of variables and basic data types.

# The script interacts with the user by first asking for their name and age, then
# calculates the year the user was born by subtracting their age from the
# current year (2024)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
# Get the user's name (string) and age (integer)

current_year = 2024
birth_year = current_year - age
# Calculate the year the user was born

print(f"Hello, {name}! You were born in {birth_year}.")
# Print a personalized greeting message
# The f prefix enables the use of expressions inside curly braces {} within a string .
# Python evaluates these expressions and replaces the name and age of the user's name
# and age with their input values.

