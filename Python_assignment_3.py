# import random

# # ---------------------------------------------------------
# # Part 1: Number Guessing Game (while loop with else/break/continue)
# # ---------------------------------------------------------
# secret_number = random.randint(1, 10)
# attempts = 3

# while attempts > 0:
#     guess = int(input("Guess the number (between 1 and 10): "))

#     # Out of range: inform the user and skip the rest of the loop
#     if guess < 1 or guess > 10:
#         print("Your guess is out of range. Please guess a number between 1 and 10.")
#         continue

#     attempts -= 1  # only valid guesses use up an attempt

#     if guess > secret_number:
#         print("Too high. Try again.")
#     elif guess < secret_number:
#         print("Too low. Try again.")
#     else:
#         print("Congratulations! You guessed the correct number.")
#         break
# else:
#     # Runs only if the loop ended without break
#     print("Better luck next time!")
#     print("The correct number was:", secret_number)


# ---------------------------------------------------------
# Part 2: Multiplication Table Generator (for loop)
# ---------------------------------------------------------
# num = int(input("Enter the number for which you want the multiplication table: "))

# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")


# ---------------------------------------------------------
# Part 3: BMI Calculator (function)
# ---------------------------------------------------------
def calculate_bmi(weight, height):
    return weight / (height ** 2)


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")