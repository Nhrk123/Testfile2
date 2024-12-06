# A Python program that interacts with the user and performs calculations

# Function to calculate the year the user will turn 100
def year_turns_100(current_age):
    current_year = 2024  # You can dynamically get the current year using datetime, but we'll keep it simple
    years_left = 100 - current_age
    year_100 = current_year + years_left
    return year_100

# Ask for the user's name and age
name = input("What's your name? ")
age = int(input(f"Hello, {name}! How old are you? "))

# Check if the age is a valid number
if age < 0:
    print("Please enter a valid age.")
else:
    # Calculate and print the year they will turn 100
    year_100 = year_turns_100(age)
    print(f"{name}, you will turn 100 years old in the year {year_100}.")
