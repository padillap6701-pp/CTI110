# Pedro Padilla
# 11/10/2025
# P4HW1: List and Loop Operations
# This program asks the user for the number of scores, then uses a loop to collect that many scores, validating each one.
# It stores the valid scores in a list, then drops the lowest score, calculates the average of the remaining scores,
# and displays the lowest score, the modified list, the average, and a corresponding letter grade.

# --- Program Pseudocode ---
# 1. START Program
# 2. Ask user for the number of scores they want to enter and store it in num_scores (Input).
# 3. Initialize an empty list named 'scores_list'.
# 4. Use a FOR loop that iterates 'num_scores' times
#    For each iteration (score number i+1):
#    Use a WHILE loop for score validation
#    Prompt user to enter score #i+1
#    Convert input to a float and store in 'score'.
#    HILE score is NOT between 0 and 100
#    Print "INVALID Score entered!!!!"
#    Print "Score should be between 0 and 100"
#    Prompt user to re-enter score #i+1 and store it.
#    Once a valid score is entered, append the 'score' to 'scores_list'.
# 5. Process Data:
#    Find the 'lowest_score' in 'scores_list' using the min() function.
#    Remove the 'lowest_score' from 'scores_list'.
#    Calculate the 'sum_of_modified_scores' using the sum() function on the modified list.
#    Calculate the 'scores_average' by dividing 'sum_of_modified_scores' by the length of the modified list.
# 6. Determine Letter Grade:
#    IF scores_average >= 90:
#    - Set 'letter_grade' to 'A'.
#    ELSE IF scores_average >= 80:
#    - Set 'letter_grade' to 'B'.
#    ELE IF scores_average >= 70:
#    - Set 'letter_grade' to 'C'.
#    ELSE IF scores_average >= 60:
#    - Set 'letter_grade' to 'D'.
#    ELSE:
#    - Set 'letter_grade' to 'F'.
# 7. Display Results (Formatted):
#    Print the header "----------Results----------"
#    Print "Lowest Score :" followed by the 'lowest_score'.
#    Print "Modified List :" followed by the current 'scores_list'.
#    Print "Scores Average :" followed by 'scores_average' formatted to two decimal places.
#    Print "Grade :" followed by the 'letter_grade'.
#    Print a final separator line.
# 8. END Program


# --- Program Code ---
while True:
    try:
        num_scores = int(input("How many scores do you want to enter? "))
        if num_scores > 0:
            break
        else:
            print("Please enter a positive number of scores.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

scores_list = []
score_count = 1
for _ in range(num_scores):
    while True:
        try:
            current_score = float(input(f"Enter score #{score_count}: "))
            if 0 <= current_score <= 100:
                scores_list.append(current_score)
                break
            else:
                print("\nINVALID Score entered!!!!")
                print("Score should be between 0 and 100")
                print(f"Enter score #{score_count} again: ")
        except ValueError:
            print("\nInvalid input. Please enter a number between 0 and 100.")

    score_count += 1

if scores_list:
    lowest_score = min(scores_list)
    scores_list.remove(lowest_score)
    if scores_list:
        sum_of_modified_scores = sum(scores_list)
        scores_average = sum_of_modified_scores / len(scores_list)
    else:
        scores_average = 0.0
else:
    lowest_score = "N/A"
    scores_average = 0.0
if scores_average >= 90:
    letter_grade = 'A'
elif scores_average >= 80:
    letter_grade = 'B'
elif scores_average >= 70:
    letter_grade = 'C'
elif scores_average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

LABEL_WIDTH = 15
SEPARATOR_LENGTH = 27

print("\n" + "-" * 7 + "Results" + "-" * 7)

print(f"{'Lowest Score':<{LABEL_WIDTH}} : {lowest_score}")

print(f"{'Modified List':<{LABEL_WIDTH}} : {scores_list}")

print(f"{'Scores Average':<{LABEL_WIDTH}} : {scores_average:>.2f}")

print(f"{'Grade':<{LABEL_WIDTH}} : {letter_grade}")

print("-" * SEPARATOR_LENGTH)