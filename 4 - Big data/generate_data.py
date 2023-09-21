import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker for generating fake data
fake = Faker()

# Define the number of employees and years
num_employees = 12
num_years = 3

# Create an empty list to store employee data
employee_data = []

# Generate data for each employee
for _ in range(num_employees):
    name = fake.name()
    country = random.choice(['Poland', 'Germany', 'USA'])
    if country == 'Poland':
        salary_currency = 'PLN'
    elif country == 'Germany':
        salary_currency = 'EUR'
    else:
        salary_currency = 'USD'

    # Initialize a random base monthly salary (float) between 2000 and 10000
    monthly_salary = round(random.uniform(2500, 20000), 2)

    # Initialize an annual salary adjustment factor between 0.9 and 1.1
    annual_adjustment_factors = [random.uniform(
        0.9, 1.1) for _ in range(num_years)]

    # Generate dates for five years (12 months per year)
    start_date = datetime(2015, 1, 31)
    for year in range(num_years):
        for month in range(1, 13):
            date_of_payment = (start_date + timedelta(days=30)
                               ).strftime('%Y-%m-%d')
            # Apply the annual adjustment factor to the monthly salary
            monthly_salary *= annual_adjustment_factors[year]
            employee_data.append(
                [name, country, salary_currency, round(monthly_salary, 2), date_of_payment])
            start_date = start_date + timedelta(days=30)

# Create a DataFrame
df = pd.DataFrame(employee_data, columns=[
                  'Name', 'Country', 'Salary_Currency', 'Monthly_Salary', 'Date_Of_Payment'])

# Save the DataFrame to a CSV file
df.to_csv('salaries.csv', index=False)
