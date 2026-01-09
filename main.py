import logic as l

a = l.RomanToNumber(input("Enter 1st Roman Number: ")).to_num()
b = l.RomanToNumber(input("Enter 2nd Roman Number: ")).to_num()

operator = input("\nEnter the Operator: ")

solution = l.Calculator(a,b)

if operator == "+":
    print(solution.add())
elif operator == '-':
    print(solution.sub())
elif operator == '*':
    print(solution.mul())
else:
    print("Use only *,-,+")
