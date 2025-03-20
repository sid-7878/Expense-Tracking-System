# Expense Management System

The Expense Tracking System is a software solution developed to streamline and simplify the process of expense management for individuals and businesses. This project aims to provide users with an efficient and organized approach to expense management, improving accuracy and offering valuable insights into expenditure patterns.


## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sid-7878/expense-management-system.git
   cd expense-management-system
   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server.server:app --reload
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```
   
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Demo Video](#demo-video)
- [Contributing](#contributing)
- [License](#license)


## Features

- Add expenses with detailed descriptions and amounts
- Automatically capture the date and time of each expense
- Display all expenses
- Calculate total expenses incurred
- User-friendly interface
- Data visualization for expense analysis

## Usage

1. **Launch the Application:**  
   - Start the server and access the web interface at:  
     ```
     http://localhost:8000
     ```

2. **Add a New Expense:**  
   - Navigate to the **Add Expense** section.  
   - Fill in the form with details like description, amount, category, and date.  
   - Click **Submit** to save the expense.  

   ![Add Expense](app_frontend.png)

3. **View Expenses:**  
   - Go to the **View Expenses** section to see the list of all recorded expenses.  
   - Use filters to sort expenses by date, category, or amount.  

   ![View Expenses](assets/images/view_expenses.png)

4. **Analyze Spending:**  
   - Visit the **Analytics** section.  
   - View visual representations of your spending patterns using charts and graphs.  

   ![Analytics Dashboard](assets/images/analytics_dashboard.png)

---

✅ **Instructions:**
- Replace the placeholder image paths (e.g., `assets/images/add_expense.png`) with the actual file paths of your screenshots.
- Make sure the screenshots are uploaded to your GitHub repository.

This section provides a clean and detailed explanation of how to use your project along with relevant screenshots. 🚀








