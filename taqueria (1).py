menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        item = input("Item: ").title()
        if item in menu:
            total += menu[item]
            print("Total: $", end="")
            print("{:.2f}".format(total))
        else:
            print(f"{item} is not in the menu. Please choose a valid item.")
    except EOFError:
        print("\nExiting the program.")
        break
print()
