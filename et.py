import csv
import os

FILE_NAME = "expenses.csv"

# Initialize CSV file if not exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense(date, category, amount, description):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("✅ Expense added successfully!")

def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def total_expenses():
    total = 0
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            total += float(row[2])
    print(f"💰 Total Expenses: {total}")

# Menu
while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category (Food, Travel, etc.): ")
        amount = input("Enter amount: ")
        description = input("Enter description: ")
        add_expense(date, category, amount, description)

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        print("Exiting... Bye! 👋")
        break

    else:
        print("❌ Invalid choice! Try again.")
