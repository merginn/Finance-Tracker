# Problem Statement:
Imagine you want to track your personal finances. You need a system that allows you to:

### 1. Add Transactions:
Each transaction should include:
- **type**: `"income"` or `"expense"`
- **amount**: Numeric value
- **category**: e.g., `"Food"`, `"Rent"`, `"Salary"`
- **date**: `YYYY-MM-DD` format

### 2. View Transactions:
- Retrieve all stored transactions.

### 3. Generate Financial Summary:
- Calculate and display:
  - **Total Income**
  - **Total Expenses**
  - **Balance**: `income - expenses`

### 4. Handle Missing Data Gracefully:
- Implements error handling if required fields are missing.

### 5. Save Transactions Permanently:
- Stores and retrieves transaction data using JSON files.
