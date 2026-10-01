# Smart Expense Analyzer
A command-line Python application for recording, analyzing, and
persisting personal expenses using CSV storage.

## Features
- Add multiple expenses
- View all expenses
- Calculate total spending
- Calculate average spending
- Find the largest expense
- Generate category-wise spending summary
- Save expenses to CSV
- Load existing expenses automatically
- Input validation and error handling

## Tech Stack
- Python
- CSV
- File Handling
- Data Structures
- Exception Handling

## Project Structure
smart-expense-analyzer/
│
├── main.py
├── expenses.csv
├── README.md
├── requirements.txt
└── .gitignore


## How It Works
The application uses a Python list as the working data structure.
CSV acts as persistent storage.

expenses.csv
     ↓
load_expenses_from_csv()
     ↓
expenses
     ↓
Analysis Functions
     ↓
save_expenses_to_csv()
     ↓
expenses.csv

### Available Operations
1. Add Expense
2. View Expenses
3. Total Spending
4. Average Spending
5. Largest Expense
6. Category Summary
7. Exit

### What I Learned
- Functions and modular programming
- Lists and dictionaries
- Loops and conditional logic
- Input validation
- Exception handling
- File handling
- CSV reading and writing
- Data persistence
- Basic code refactoring
- 
### Future Improvements
- Monthly budget tracking
- Date support
- Data visualization
- Pandas-based analysis
- SQL database integration
- Automated reports