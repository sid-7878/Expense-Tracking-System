import mysql.connector
from contextlib import contextmanager
from setup_logging import setup_logger


logger = setup_logger('db')

@contextmanager
def get_db_cursor(commit = False):
    connection = mysql.connector.connect(
        host= "localhost",
        user = 'root',
        password = 'root' ,
        database = 'expense_manager'

    )

    if connection.is_connected() :
        print("connection is succesfull")
    else :
        print("connection failed")

    cursor = connection.cursor(dictionary= True)
    yield cursor

    if commit :
        connection.commit()

    cursor.close()
    connection.close()

def fetch_all_records ():
    with get_db_cursor() as cursor :
        cursor.execute('SELECT * FROM expense_manager.expenses;')
        expenses =cursor.fetchall()
        for expense in expenses :
            print(expense)



def fetch_expenses_for_date(expense_date) :
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute('SELECT * FROM expense_manager.expenses WHERE expense_date = %s',
                       (expense_date,))
        expenses = cursor.fetchall()
        return expenses


def insert_expense(expense_date, amount, category, notes) :
    logger.info(f"insert_expense called with date: {expense_date}, amount: {amount}, category: {category}, notes: {notes}")
    with get_db_cursor(commit = True) as cursor :
        cursor.execute(
            "INSERT INTO expenses(expense_date, amount, category, notes) VALUES(%s, %s, %s,%s)",
            (expense_date, amount, category, notes))


def delete_expense_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with {expense_date}")
    with get_db_cursor(commit = True) as cursor :
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s",
                       (expense_date,) )

def fetch_expense_summary(start_date , end_date):
    logger.info(f"fetch_expense_summary called with start: {start_date} end: {end_date}")
    with get_db_cursor(commit = True) as cursor :
        cursor.execute('''SELECT category , SUM(amount) as total 
                       FROM expenses WHERE expense_date BETWEEN %s and %s 
                       GROUP BY category''',
                       (start_date,end_date))
        data = cursor.fetchall()
        return data

def fetch_monthly_expense_summary():
    logger.info(f"fetch_expense_summary_by_months")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT month(expense_date) as expense_month, 
               monthname(expense_date) as month_name,
               sum(amount) as total FROM expenses
               GROUP BY expense_month, month_name;
            '''
        )
        data = cursor.fetchall()
        return data


if __name__ == "__main__" :
    pass