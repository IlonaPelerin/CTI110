# This program asks the user to input 5 test grades.
# It then displays the letter grade for each score and the final average test score.
# November 2, 2017
# CTI 110 - Test Average and Grades
# Ilona Pelerin
#

# Main function to control the flow of the program.
# It also holds the input command for the user to type the grade in.

def main():
    
    # Defining local varibles

    test1 = 0.0
    test2 = 0.0
    test3 = 0.0
    test4 = 0.0
    test5 = 0.0
    average = 0.0

    # Getting input from user

    test1 = float(input("Please enter the score for test 1: "))
    test2 = float(input("Please enter the score for test 2: "))
    test3 = float(input("Please enter the score for test 3: "))
    test4 = float(input("Please enter the score for test 4: "))
    test5 = float(input("Please enter the score for test 5: "))
    print()

    # Call the calc_average function

    average = calc_average(test1, test2, test3, test4, test5)

    # Display the test grades and averages in a table
    # calling on determine_grade function

    print('test\t\tScore\t\tletter grade')
    print('----------------------------------------------------')
    print('Test 1:\t\t', test1, '\t\t', determine_grade(test1))
    print('Test 2:\t\t', test2, '\t\t', determine_grade(test2))
    print('Test 3:\t\t', test3, '\t\t', determine_grade(test3))
    print('Test 4:\t\t', test4, '\t\t', determine_grade(test4))
    print('Test 5:\t\t', test5, '\t\t', determine_grade(test5))
    print('----------------------------------------------------')
    print ('Average score:\t', average, '\t\t', \
           determine_grade(average))

# this function accepts 5 test scores as arguments
# and returns the average of the scores.

def calc_average(score1, score2, score3, score4, score5):
    return (score1 + score2 +score3 + score4 + score5)/5.0

# This funtion accepts a test score as an argement and
# returns a letter grade for the score using the ten-point grading scale.

def determine_grade(test):
    if test >= 90:
        return "A"
    elif test >= 80:
        return "B"
    elif test >= 70:
        return "C"
    elif test >= 60:
        return "D"
    else:
        return "F"

# Call the main function

main()
    
