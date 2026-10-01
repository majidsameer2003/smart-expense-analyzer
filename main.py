import csv

expenses = []

###########################################################
# csv file functions

def load_expenses_from_csv(filename):
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                expense = {
                    "category": row["category"],
                    "amount": float(row["amount"])
                }

                expenses.append(expense)

    except FileNotFoundError:
        pass

load_expenses_from_csv("expenses.csv")


def save_expenses_to_csv(filename):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['category', 'amount']

        writer = csv.DictWriter(
            csvfile,
            fieldnames=fieldnames
            )

        writer.writeheader()
        writer.writerows(expenses)

##########################################################
# featrues function

def has_expenses():
  return len(expenses) > 0


def add_expense():
  while True:
    category = input("Enter expense category ('done' to finish): ")
    if category.lower() == "done":
      print("Returning to main menu...")
      break
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            if amount <= 0:
                print("❌ Amount must be greater than 0.")
                continue
            break # Valid amount, exit inner loop
        except ValueError:
            print("❌ Invalid amount. Please enter a number.")
            continue # Ask for amount again

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses_to_csv("expenses.csv")
    print("✅ Expense added successfully!")

def view_expenses():
    print("\n========== YOUR EXPENSES ==========\n")

    if not has_expenses():
      print("No expenses recorded.")
      return

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. "
            f"{expense['category']} - "
            f"₹{expense['amount']:.2f}"
        )


def total_spending():
    print("\n========== YOUR EXPENSES ==========\n")

    if not has_expenses():
      print("No expenses recorded.")
      return
    total_amount = 0
    for expense in expenses:
        total_amount += expense['amount']

    print(f"Total Spending: ₹{total_amount:.2f}")


def average_spending():
    print("\n========== YOUR EXPENSES ==========\n")

    if not has_expenses():
      print("No expenses recorded.")
      return

    total_amount = 0
    for expense in expenses:
        total_amount += expense['amount']
    transactions = len(expenses)
    average = total_amount / transactions
    print(f"Average Spending: ₹{average:.2f}")


def largest_expense():
    print("\n========== YOUR EXPENSES ==========\n")

    if not has_expenses():
      print("No expenses recorded.")
      return

    largest_expense = expenses[0]
    for expense in expenses:
        if expense["amount"] > largest_expense["amount"]:
           largest_expense = expense
    print(
            f"Largest Expense: "
            f"{largest_expense['category']} - "
            f"₹{largest_expense['amount']:.2f}")


def category_summary():
    print(  "\n=====CATEGORY SUMMARY=====\n")
    if not has_expenses():
      print("No expenses recorded.")
      return
    total_category={}
    for expense in expenses:
      category=expense['category']
      amount=expense['amount']
      if category in total_category:
          total_category[category]+=amount
      else:
          total_category[category]=amount

    for number, (category, amount) in enumerate(total_category.items(), start=1):
        print(f"{number}.{category}- ₹{amount:.2f}")



while True:

    print("\n================================")
    print("     SMART EXPENSE ANALYZER")
    print("================================")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Average Spending")
    print("5. Largest Expense")
    print("6. Category Summary")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("You selected Add Expense.")
        add_expense()

    elif choice == "2":
        print("You selected View Expenses.")
        view_expenses()

    elif choice == "3":
        print("You selected Total Spending.")
        total_spending()

    elif choice == "4":
        print("You selected Average Spending.")
        average_spending()

    elif choice == "5":
        print("You selected Largest Expense.")
        largest_expense()

    elif choice == "6":
        print("You selected Category Summary.")
        category_summary()

    elif choice == "7":
        print("Thank you for using Smart Expense Analyzer!")
        break

    else:
        print("❌ Invalid choice. Please select 1-7.")