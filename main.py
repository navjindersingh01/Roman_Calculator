import logic as l

a = l.RomanToNumber(input("Enter 1st Roman Number: ")).to_num()
b = l.RomanToNumber(input("Enter 2nd Roman Number: ")).to_num()

operator = input("\nEnter the Operator: ")
solution = l.Calculator(a,b)





if operator == "+":
    result = solution.add()
elif operator == '-':
    result = solution.sub()
elif operator == '*':
    result = solution.mul()
else:
    print("Use only *,-,+")

converter = l.NumberToRoman(result)

print(f"Result: {converter.to_roman()}")
