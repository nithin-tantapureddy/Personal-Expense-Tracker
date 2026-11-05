import csv
import os
from collections import defaultdict
import matplotlib.pyplot as plt

FILENAME = "expenses.csv"

expenses = []

def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append({
                    "amount": float(row["amount"]),
                    "category": row["category"],
                    "date": row["date"]
                })

def save_expenses():
    with open(FILENAME, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["amount", "category", "date"]
        )

        writer.writeheader()

        for expense in expenses:
            writer.writerow(expense)

def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")

        expenses.append({
            "amount": amount,
            "category": category,
            "date": date
        })

        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount entered.")

def view_expenses():

    if not expenses:
        print("No expenses found.")
        return

    print("\nExpense List")
    print("-" * 40)

    for expense in expenses:
        print(
            expense["date"],
            expense["category"],
            f"₹{expense['amount']}"
        )

def generate_report():

    if not expenses:
        print("No data available.")
        return

    total = sum(exp["amount"] for exp in expenses)

    print("\nTotal Spending:", total)

    category_total = defaultdict(float)

    for exp in expenses:
        category_total[exp["category"]] += exp["amount"]

    print("\nCategory Wise Spending")

    for category, amount in category_total.items():
        print(category, ":", amount)

    highest = max(expenses, key=lambda x: x["amount"])

    print("\nHighest Expense")
    print(highest)

def visualize_expenses():

    if not expenses:
        print("No data available.")
        return

    category_total = defaultdict(float)

    for exp in expenses:
        category_total[exp["category"]] += exp["amount"]

    categories = list(category_total.keys())
    amounts = list(category_total.values())

    plt.figure(figsize=(8,5))
    plt.bar(categories, amounts)
    plt.title("Expense Distribution")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()

def menu():

    load_expenses()

    while True:

        print("\n====== Personal Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Generate Report")
        print("4. Visualize Expenses")
        print("5. Save and Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            generate_report()

        elif choice == "4":
            visualize_expenses()

        elif choice == "5":
            save_expenses()
            print("Data saved successfully!")
            break

        else:
            print("Invalid Choice")

menu()
