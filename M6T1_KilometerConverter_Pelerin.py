# CTI-110
# M6T1 - Bug Collector
# Ilona Pelerin
# October 31, 2017

# Global constant for converting kilometers to miles

Kilometer_to_Miles = 0.6214

def main():

    # Local variable for main function to hold the distance in kilometer.

    kilometerDistance = 0.0

    # Get input from the user for distance in kilometer.

    kilometerDistance = float(input("Enter the distance in Kilometer: "))
    print()

    # Calling the calculateMiles function to print the miles.

    show_miles(kilometerDistance)

# The show_miles function has kilometer as an argument.

def show_miles(kilometer):

    # Local variable for the claculateMiles function.

    miles = 0.0

    miles = kilometer * Kilometer_to_Miles

    # Print the converted kilometer in miles.  End of show_miles function

    print ("The distance of", format(kilometer, '.2f'), "Kilometer is", format(miles, '.2f'), "miles")

# Call the main function.

main()
