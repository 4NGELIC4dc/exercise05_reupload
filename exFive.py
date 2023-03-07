firstSide = int(input("Enter the first side: "))
secondSide = int(input("Enter the second side: "))
thirdSide = int(input("Enter the third side: "))
if firstSide == thirdSide and secondSide == thirdSide:
    print("The triangle is an equilateral.")
else:
    print("The triangle is not an equilateral.")