# CTI-110
# M5HW2 - Running Total
# Ilona Pelerin
# October 19, 2017

#
def main():
    
    
    # declaring and initializing the variables.

    number = 1.0
    runningTotal = 0.0

    # setting up the while loop to add numbers until a negative one is entered.

    while number >= 0:
        number = float(input('Enter a positive number: '))

    # Check the number is positive so it does not change the value of the running total.
    
        if number >= 0:
            runningTotal = runningTotal + number
            print()
            
    # Display the running total using proper formating to round to 2 decimal places.

    print()
    print ('Total = ' , format(runningTotal, '.2f'))
    
        
main()
