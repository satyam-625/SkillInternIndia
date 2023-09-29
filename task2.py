import os
import json

# Define the data file path
DATA_FILE = "budget_data.json"

# Check is there data file is here or not if not then vreate it
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

# Load budget from the file
def load_budget_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save budget data to the file
def save_budget_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Function to add an expense
def add_expense(date, category, amount):
    budget_data = load_budget_data()
    budget_data.append({"date": date, "category": category, "amount": amount})
    save_budget_data(budget_data)

# Function to calculate total expenses
def calculate_total_expenses():
    budget_data = load_budget_data()
    total_expenses = sum(item["amount"] for item in budget_data)
    return total_expenses

# Main menu
def main():
    while True:
        print("Budget Tracker")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category: ")
            amount = float(input("Enter the amount: "))
            add_expense(date, category, amount)
            print("Expense added successfully!")
        elif choice == "2":
            total_expenses = calculate_total_expenses()
            print(f"Total Expenses: ${total_expenses:.2f}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()