#CTI-110
#M2HW2 - Tip Tax Total
#Ilona Pelerin
#August 29, 2017
#
#Promp to get the cost of the meal at a restaurant.
foodCost = float(input("Enter the cost of the meal: "))
#Calculate the tip amount for the meal cost and print.
tipAmount = foodCost * .18
print("Tip amound: $", format(tipAmount, ".2f"))
#Calculate the sales tax for the meat cost and print.
salesTax = foodCost * .07
print("Sales Tax: $", format(salesTax, ".2f"))
#Calculate the total cost of the meal and print.
totalCost = foodCost + tipAmount + salesTax
print("Total cost: $", format(totalCost, ".2f"))
#Print retaurant standart salutation.
print("Chez Ilona appreciates your patronage.")
print("Hope the see you soon!")
