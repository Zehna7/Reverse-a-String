string = input("Please Enter Your Own String: ")
string2 = ('')
for i in string:
    string2 = i + string2
print("\nThe original String = ", string)
print("The Reversed String = ", string2)