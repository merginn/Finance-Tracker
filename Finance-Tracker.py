import json
import os
from datetime import datetime

class FinanceTracker:
    def __init__(self, filename='transactions.json'):
        self.filename = filename
        self.transactions = self.load_transactions()

    def load_transactions(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as file:
            return json.load(file)

    def save_transactions(self):
        with open(self.filename, 'w') as file:
            json.dump(self.transactions, file, indent=2)

    def add_transaction(self, type, amount, category, date):
        transaction = {
            'type': type,
            'amount': float(amount),
            'category': category,
            'date': date
        }
        self.transactions.append(transaction)
        self.save_transactions()

    def retrieve_transactions(self):
        return self.load_transactions()

    def filter_transactions(self, type=None, category=None, start_date=None, end_date=None):
        transactions = self.load_transactions()
        filtered = transactions

        if type:
            filtered = [t for t in filtered if t['type'] == type]
        if category:
            filtered = [t for t in filtered if t['category'] == category]
        if start_date:
            filtered = [t for t in filtered if t['date'] >= start_date]
        if end_date:
            filtered = [t for t in filtered if t['date'] <= end_date]

        return filtered


def main():
    tracker = FinanceTracker()


    tracker.add_transaction('income', 10000, 'Salary', '2024-01-10')
    tracker.add_transaction('expense', 1000, 'Rent', '2024-01-15')
    tracker.add_transaction('expense', 300, 'Groceries', '2024-01-20')


    print("All Transactions:")
    for transaction in tracker.retrieve_transactions():
        print(transaction)


    print("\nExpense Transactions:")
    expense_transactions = tracker.filter_transactions(type='expense')
    for transaction in expense_transactions:
        print(transaction)

if __name__ == "__main__":
    main()