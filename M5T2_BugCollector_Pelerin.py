# CTI-110
# M5T2 - Bug Collector
# Ilona Pelerin
# October 12, 2017
#
def main():
    
    
    # initializing the accumulator to zero

    total = 0

    # set up the for loop to iterate seven times

    for day in range(1, 8):
        
    # Prompt user to input the number of bugs collected each day
    
        print('How many bugs did you collect on day', day)

    # store the number in a variable

        bugs = int(input())
        
    # Add number of bugs to the accumulator total

        total += bugs
        
    # End of loop    
    # Display tolal of bugs collect over seven days

    print('You collected a total of', total, 'bugs.')

main()
    
