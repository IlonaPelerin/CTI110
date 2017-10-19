# CTI-110
# M5HW3 - Factorial
# Ilona Pelerin
# October 19, 2017

#
def main():
    
    
    # Declaring and initializing the variables.

    number = 0

    # Get a valid positive number from user and setting up the while loop.

    while number <= 0:
        number = int(input('Enter a positive integer: '))

        print()

    # Initializing the accumulator varial for calculating the factorial.
        factorial = 1
     
        for factor in range(1, number + 1):
            factorial *= factor
            
    # Display the factorial of the number

    print ('the factorial of' , number, 'is', factorial)
    
        
main()
