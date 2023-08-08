"""
    Name: paint_job_estimator.py
    Author: Adam Frisch
    Created: 3/3/2022
    Purpose: Determine the number of labor hours, gallons of paint,
    paint charge, labor charge, and total charge for a paint job based
    on user input.

"""

# Imports
from math import ceil
import utils

# Constants
FEET_PER_GALLON = 112.0
LABOR_HOURLY = 35
HOURS_LABOR = 8

# Title
print(utils.title("Paint Job Estimator"))

# Main function
def main():
    
    wall_square_feet, price_per_gallon = get_input()

    gallons = calculate_gallons(wall_square_feet)

    labor_hours = calculate_labor_hours(wall_square_feet) 

    paint_price = calculate_paint_price(gallons, price_per_gallon)

    labor_charge = calculate_labor_charge(labor_hours) 

    total_sale = calculate_total_sale(labor_charge, paint_price) 

    display(gallons, labor_hours, paint_price, labor_charge, total_sale)

# Get user inputs
def get_input():
    wall_square_feet = int(input("Enter wall space in square feet: "))
    price_per_gallon = float(input("Enter paint price per gallon: "))
    return wall_square_feet, price_per_gallon

# Calculate gallons required, round up
def calculate_gallons(wall_square_feet):
    gallons = ceil(wall_square_feet / FEET_PER_GALLON)
    return gallons

# Calculate labor hours required, round up
def calculate_labor_hours(wall_square_feet):
    labor_hours = ceil((wall_square_feet / FEET_PER_GALLON) * HOURS_LABOR)
    return labor_hours

# Calculate the price of paint
def calculate_paint_price(gallons, price_per_gallon):
    paint_price = gallons * price_per_gallon
    return paint_price

# Calculate labor charge
def calculate_labor_charge(labor_hours):
    labor_charge = labor_hours * LABOR_HOURLY
    return labor_charge

# Calculate the total charge
def calculate_total_sale(labor_charge, paint_price):
    total_sale = labor_charge + paint_price
    return total_sale

# Display all result
def display(gallons, labor_hours, paint_price, labor_charge, total_sale):
    print(f'Gallons of paint: {gallons}')
    print(f'Hours of labor: {labor_hours}')
    print(f'Paint charges: ${paint_price:,.2f}')
    print(f'Labor charges: ${labor_charge:,.2f}')
    print(f'Total cost: ${total_sale:,.2f}')

main()
    

