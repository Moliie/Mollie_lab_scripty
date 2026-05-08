# -----------------------------------------
# Mollie - Python Lab Script
# -----------------------------------------

# -------------------------------
# Personal Greeting & Age Check
# -------------------------------

name = input("Mollie Rejano: ")
age = int(input("25: "))

print(f"\nHello, {name}!")

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# -------------------------------
# Math Operation (Rectangle Area)
# -------------------------------

print("\n--- Rectangle Area Calculator ---")
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
print(f"The area of the rectangle is: {area}")

# -------------------------------
# Favorite Item List
# -------------------------------

print("\n--- Favorite Item List ---")
items = ["Python", "Gaming", "Drawing", "Traveling"]

print("Here are some items:")
for item in items:
    print("-", item)

favorite = input("Which of these is your favorite: ")

print(f"Great choice! Your favorite item is {favorite}.")
