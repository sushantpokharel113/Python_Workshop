print("\nQno.5 \n")
print("10 builtin functions in Python are : \n")

# pow()
print("1. Pow : Returns the power of a given number")
print(f"5 ^ 2 = {pow(5,2)}")

# ascii()
print("\n2. Ascii : Returns the character for any given value")
print(f"# = {ascii(65)}")

#str()
print("\n3. str : Converts and returns any data type into string")
print("Sum of 2 + 2 is" + str(4))

#int()
print("\n 4. int : Converts and returns any data data type into integer")
print(f"Int of 5.0 is {int(5.0)}")

#float()
print("\n 5. float : Converts and returns any data data type into floating point number")
print(f"Int of 11 is {float(11)}")

#ord
print("\n6. ord : Returns ascii value corresponding to any character")
print("Character represented by 65 is Ascii is {}".format(ord('A')))

#len
print("\n7. len : Returns the length of string or list or any sequence")
print("The length of 'MONTY PYTHON is {}".format(len("MONTY PYTHON")))

#complex()
print("\n8. complex : Returns the given numbers in complez form i.e in terms of j")
print(f"Complex form os 2 and 3 is {complex(2,3)}")

#abs()
print("\n9. abs : Returns the absolute value of given number")
print(f"Absolute value of -10 is {abs(10)}")

#divmod()
print("\n10. divmod() : Returns the quotient and remainder for any given numbers")
print(f"Quotient and remainder for 10/3 is {divmod(10,3)}")
