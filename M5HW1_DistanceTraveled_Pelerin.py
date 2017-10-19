# CTI-110
# M5HW1 - Distance Traveled
# Ilona Pelerin
# October 19, 2017

#
def main():
    
    
    # declaring and initializing the variables to zero.

    distance = 0
    speed = 0.0
    time = 0.0

    # Prompt user to input the speed and store it in speed variable.
    
    speed = float(input('Enter the speed at which you are driving in mph: '))

    # Prompt user to input the time traveled and convert to int for full hour

    time = int(float(input('Enter the number of hours driven: ')))
        
    # Display the distance traveled for each hour in a table.

    print ('Hours \t Distance Traveled')
    print ('__________________________')
        
    # For loop to iterate as many times as there are hours
                      
    for hour in range(1, time + 1):
            distance = hour * speed
            print (hour, '\t' , distance)

                      
main()
