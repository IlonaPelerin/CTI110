# CTI-110
# M3HW1 - Age Classifier
# Ilona Pelerin
# September 13, 2017
#
def main():
    
    packagePrice = 99
    
    # Get the quantity purchased
    print()
    quantity = int(input("Please enter the number of packages bought: "))
    print()
    # Print statement of the discount, total purchase cost, and final cost given quantity.
    
    if   quantity < 10:
         discount = quantity * (packagePrice * 0)
         totalPurchaseCost = quantity * packagePrice
         finalCost = totalPurchaseCost - discount
         print("Your total purchase cost is $", format(totalPurchaseCost,".2f"))
         print("Your discount is           -$", format(discount,".2f"))
         print("Your final cost is          $", format(finalCost,".2f"))
         
    elif quantity < 20:
         discount = quantity * (packagePrice * 0.1)
         totalPurchaseCost = quantity * packagePrice
         finalCost = totalPurchaseCost - discount
         print("Your total purchase cost is $", format(totalPurchaseCost,".2f"))
         print("Your 10% discount is       -$", format(discount,".2f"))
         print("Your final cost is          $", format(finalCost,".2f"))
         
    elif quantity < 50:
         discount = quantity * (packagePrice * 0.2)
         totalPurchaseCost = quantity * packagePrice
         finalCost = totalPurchaseCost - discount
         print("Your total purchase cost is $", format(totalPurchaseCost,".2f"))
         print("Your 20% discount is       -$", format(discount,".2f"))
         print("Your final cost is          $", format(finalCost,".2f"))
         
    elif quantity < 100:
         discount = quantity * (packagePrice * 0.3)
         totalPurchaseCost = quantity * packagePrice
         finalCost = totalPurchaseCost - discount
         print("Your total purchase cost is $", format(totalPurchaseCost,".2f"))
         print("Your 30% discount is       -$", format(discount,".2f"))
         print("Your final cost is          $", format(finalCost,".2f"))
         
    elif quantity >= 100:
         discount = quantity * (packagePrice * 0.4)
         totalPurchaseCost = quantity * packagePrice
         finalCost = totalPurchaseCost - discount
         print("Your total purchase cost is $", format(totalPurchaseCost,".2f"))
         print("Your 40% discount is       -$", format(discount, ".2f"))
         print("Your final cost is          $", format(finalCost, ".2f"))
    
main()
