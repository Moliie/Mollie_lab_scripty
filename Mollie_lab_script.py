# ---------------------------------------------------------
# Author: Mollie Rejano
# Class: Python Basics
# Date: May 8, 2026
# Assignment: Lab Script (Greeting, Math, List)
# ---------------------------------------------------------

# =========================================================
# 1. PERSONAL GREETING & AGE CHECK
# =========================================================

name = input("Mollie Rejano: ")
age = int(input("25: "))

print(f"\nHello, {name}!")

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# =========================================================
# 2. MATH OPERATION (Rectangle Area Calculator)
# =========================================================

print("\n--- Rectangle Area Calculator ---")
length = float(input("20px: "))
width = float(input("45px: "))

area = length * width
print(f"The area of the rectangle is: {area}")

# =========================================================
# 3. FAVORITE ITEM LIST
# =========================================================

print("\n--- Favorite Item List ---")
items = ["Learning", "Animation", "Art/Drawing", "History"]

print("Here are some items:")
for item in items:
    print("-", item)

favorite = input("Animation: ")

print(f"Great choice! Your favorite item is {favorite}.")
