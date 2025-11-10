# Pedro Padilla
# 11/10/2025
# P4HW2 - Multi-Employee Salary Calculator
# This program uses a loop to process salary calculations for multiple employees, including overtime pay at 1.5 times the normal rate.
# It accumulates and displays the total number of employees processed, total overtime pay, total regular pay, and total gross pay.

# --- Program Pseudocode ---
# 1. START Program
#
# 2. Initialize Accumulators and Constants:
# SET REGULAR_HOURS_THRESHOLD = 40.0
# SET OVERTIME_MULTIPLIER = 1.5
# SET total_employees = 0
# SET total_overtime_pay = 0.0
# SET total_regular_pay = 0.0
# SET total_gross_pay = 0.0
#
# 3. Start Loop:
# Prompt user to enter employee's name or "Done" to terminate and store in employee_name.
# WHILE employee_name IS NOT "Done":
#
#    4. Get Input for current employee:
#    Prompt user to enter hours worked and store in hours_worked.
#    Prompt user to enter pay rate and store in pay_rate.
#
#    5. Calculate Pay for current employee:
#    SET overtime_hours = 0.0
#    SET overtime_pay = 0.0
#
#    IF hours_worked > REGULAR_HOURS_THRESHOLD THEN
#       SET regular_hours = REGULAR_HOURS_THRESHOLD
#       CALCULATE overtime_hours = hours_worked - REGULAR_HOURS_THRESHOLD
#       CALCULATE overtime_rate = pay_rate * OVERTIME_MULTIPLIER
#       CALCULATE overtime_pay = overtime_hours * overtime_rate
#    ELSE
#       SET regular_hours = hours_worked
#
#    CALCULATE regular_pay = regular_hours * pay_rate
#    CALCULATE gross_pay = regular_pay + overtime_pay
#
#    6. Update Accumulators:
#    INCREMENT total_employees by 1
#    ADD overtime_pay to total_overtime_pay
#    ADD regular_pay to total_regular_pay
#    ADD gross_pay to total_gross_pay
#
#    7. Display Current Employee Results:
#    Print Employee name.
#    Print table header.
#    Print current employee's hours_worked, pay_rate, overtime_hours, overtime_pay, regular_pay, and gross_pay.
#
#    8. Prompt for Next Employee:
#    Prompt user to enter next employee's name or "Done" to terminate and store in employee_name.
#
# 9. Loop Ends when "Done" is entered.
#
# 10. Display Final Totals:
# Print "Total number of employees entered:" followed by total_employees.
# Print "Total amount paid for overtime:" followed by total_overtime_pay.
# Print "Total amount paid for regular hours:" followed by total_regular_pay.
# Print "Total amount paid in gross:" followed by total_gross_pay.
#
# 11. END Program

# --- Program Code ---

REGULAR_HOURS_THRESHOLD = 40.0
OVERTIME_MULTIPLIER = 1.5
COL_WIDTH = 12
SEPARATOR_LINE = "-" * (COL_WIDTH * 6)

total_employees = 0
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0

print("Welcome to the Multi-Employee Payroll Calculator!")
print(SEPARATOR_LINE)

employee_name = input('Enter employee\'s name or "Done" to terminate: ')

while employee_name.lower() != "done":
    
    while True:
        try:
            hours_worked = float(input(f"How many hours did {employee_name} work? "))
            pay_rate = float(input(f"What is {employee_name}\'s pay rate? "))
            break
        except ValueError:
            print("\nError: Hours worked and pay rate must be numbers. Please re-enter.\n")
    
    overtime_hours = 0.0
    overtime_pay = 0.0

    if hours_worked > REGULAR_HOURS_THRESHOLD:
        regular_hours = REGULAR_HOURS_THRESHOLD
        overtime_hours = hours_worked - REGULAR_HOURS_THRESHOLD
        overtime_rate = pay_rate * OVERTIME_MULTIPLIER
        overtime_pay = overtime_hours * overtime_rate
    else:
        regular_hours = hours_worked

    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    print(f"\nEmployee name: {employee_name}\n")
    print(f"{'Hours Worked':<{COL_WIDTH}}{'Pay Rate':<{COL_WIDTH}}{'OverTime':<{COL_WIDTH}}{'Overtime Pay':<{COL_WIDTH}}{'RegHour Pay':<{COL_WIDTH}}{'Gross Pay':<{COL_WIDTH}}")
    print("-" * (COL_WIDTH * 6))

    output_row = f"{hours_worked:<{COL_WIDTH}.1f}"
    output_row += f"{pay_rate:<{COL_WIDTH}.2f}"
    output_row += f"{overtime_hours:<{COL_WIDTH}.1f}"
    output_row += f"${overtime_pay:<{COL_WIDTH-1}.2f}"
    output_row += f"${regular_pay:<{COL_WIDTH-1}.2f}"
    output_row += f"${gross_pay:<{COL_WIDTH-1}.2f}"

    print(output_row)
    print("\n" + SEPARATOR_LINE)
    employee_name = input('Enter employee\'s name or "Done" to terminate: ')
print("\n" + "-" * 20 + " Final Totals " + "-" * 20)
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
print("-" * 54)