# CTI-110
# M3HW1 - Age Classifier
# Ilona Pelerin
# September 12, 2017
#
def main():
    
    # Get the person's age. If less than a year old use a decimal.
    age = float(input("Please enter the person's age (if less than 1 year, use a decimal): "))
    
    # Print statement given the age.
    
    if   age <= 1:
         print('You are an infant')
    elif age < 13:
         print('You are a child')
    elif age < 20:
         print('You are a teenager')
    else :
         print('You are an adult')
    
main()
