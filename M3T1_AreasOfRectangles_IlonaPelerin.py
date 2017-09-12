#CTI-110
#M3T1 - Areas if Rectangles
#Ilona Pelerin
#September 12, 2017
#
#Prompt to get the length of the first rectangle
lengthRectangle1 = float(input("Enter the lengths of the first rectangle: "))
#Prompt to get the width of the first rectangle
widthRectangle1 = float(input("Enter the width of the first rectangle: "))
#create a line space
print(" ")
#Prompt to get the length of the second rectangle
lengthRectangle2 = float(input("Enter the lengths of the second rectangle: "))
#Prompt to get the width of the second rectangle
widthRectangle2 = float(input("Enter the width of the second rectangle: "))
#
#Calculate the area of the first rectangle
areaRectangle1 = lengthRectangle1 * widthRectangle1
#Calculate the area of the second rectangle
areaRectangle2 = lengthRectangle2 * widthRectangle2
#create a line space
print(" ")
#Print appropriate response given the different sizes of the areas
if areaRectangle1 > areaRectangle2:
    print("The first area is: ", format(areaRectangle1,".2f"))
    print("The second area is: ", format(areaRectangle2,".2f"))
    print(" ")
    print("The first rectangle has the larger area")
elif areaRectangle1 < areaRectangle2:
    print("The first area is: ", format(areaRectangle1,".2f"))
    print("The second area is: ", format(areaRectangle2,".2f"))
    print(" ")
    print("The second rectangle has the larger area")
else:
    print("Both rectangles have equal area of: ", format(areaRectangle1,".2f"))
