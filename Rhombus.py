rows = int(input("Enter the number of rows for the Rhombus: "))
print("Rhombus:")

if rows == 1:
    print("1")
elif rows == 2:
    print(" 1")
    print("121")
    print(" 1")
elif rows == 3:
    print("  1")
    print(" 121")
    print("12321")
    print(" 121")
    print("  1")
elif rows == 4:
    print("   1")
    print("  121")
    print(" 12321")
    print("1234321")
    print(" 12321")
    print("  121")
    print("   1")
elif rows == 5:
    print("    1")
    print("   121")
    print("  12321")
    print(" 1234321")
    print("123454321")
    print(" 1234321")
    print("  12321")
    print("   121")
    print("    1")
else:
    print("Please enter a number between 1 and 5 for the number of rows.")  

