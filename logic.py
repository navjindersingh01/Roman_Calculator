import json

class Calculator():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
    def __str__(self):
        return f"A: {self.a}\nB: {self.b}"
    
class RomanToNumber():
    def __init__(self,a):
        self.a = list(a.upper())

        with open("roman.json",'r') as f:
            self.romans = json.load(f)
        
        with open("substraction.json","r") as f:
            self.substraction_pairs = json.load(f)
        
    def to_num(self):

        number = 0

        if len(self.a) == 1:
            number = self.romans[self.a[0]]

        elif len(self.a) == 2:
            pair = self.a[0] + self.a[1]
            if pair in self.substraction_pairs["Substraction_rule"]:
                index = self.substraction_pairs["Substraction_rule"].index(pair)
                number = self.substraction_pairs["Substituting_values"][index]
            else: 
                for i in self.a:
                    number += self.romans[i]

        else:
            for i in self.a[:-2]:
                number += self.romans[i]
            pair = self.a[-2] + self.a[-1]
            if pair in self.substraction_pairs["Substraction_rule"]:
                index = self.substraction_pairs["Substraction_rule"].index(pair)
                number += self.substraction_pairs["Substituting_values"][index]
            else:
                number += self.romans[self.a[-2]]
                number += self.romans[self.a[-1]]
        
        return number

    def __str__(self):
        return f"Roman numer is: {self.a}"
    
class NumberToRoman():
    def __init__(self,a):
        self.a = str(a)
    
        with open("substraction.json","r") as f:
                self.substraction_pairs = json.load(f)
        
        with open("roman.json",'r') as f:
            self.romans = json.load(f)
    
    def to_roman(self):
        if len(self.a) == 1:
            if int(self.a) in self.romans.values():
                return 

if __name__ == "__main__":
    roman = 'MDCCCLXXXVIIV'
    num1 = RomanToNumber(roman)
    print(num1.to_num())
    print(num1)
    