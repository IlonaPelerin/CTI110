# CTI-110
# M6T2 - Feet to Inches Converter
# Ilona Pelerin
# November 1, 2017

# Main function

def main():

    # Local variables for feet and inches.

    feet = 0.0
    inches = 0.0

    # Get user input of the number of feet.

    feet = float(input("Enter the number of feet to convert: "))
    print()
    # call and print the corresponding number of inches from the feet_to_inches function.
                 
    inches = feet_to_inches(feet)
    print (feet, "feet = ", inches, "inches")
                 
# The feet to inches function uses the parameter feet from the main function.
# Returns the converted number of inches.

def feet_to_inches(feet):
    inches = 12 * feet
    return inches

# Call the main function

main()
