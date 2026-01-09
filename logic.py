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
        
        with open("unit_numbers.json") as f:
            self.unit_romans = json.load(f)
        
    def add_vinculum(self,string):
        return "".join([char + '\u0305' for char in string])
    
    def to_roman_helper(self,number):
        roman_number = str()
        roman_list = []


        if 1 <= (number // 100) < 3:
            count = number // 100
            for _ in range(count):
                roman_list.append("C")
        
        elif 1 <= (number // 10) < 4:
            count = number // 10
            for _ in range(count):
                roman_list.append("X")
        

        roman_number = ''.join(roman_list)

        return roman_number
    
    def to_roman(self):
        length = len(self.a)
        num_list = list(self.a)
        places_list = []
        roman_list = []

        if length == 1:
            return self.unit_romans[self.a]
        
        for i in num_list:
            places_list.append(int(i) * (10**(length-1)))
            length -= 1
        
        for i in places_list:
            if len(str(i)) >=3 and i//1000:
                if 1 < i // 1000 < 4: 
                    for i in range(i//1000):
                        roman_list.append("M")
                else:
                    a = i//1000
                    roman_list.append(self.add_vinculum(self.unit_romans[str(a)]))
            elif len(str(i)) == 3 and i//500:
                if i // 500:
                    remainder = i - 500
                    if remainder // 100 < 4:
                        roman_numeral_remainder = self.to_roman_helper(remainder)
                        roman_list.append("D"+roman_numeral_remainder)
                    else: 
                        roman_list.append("CM")

            elif len(str(i)) == 3 and i//100:
                if i // 100:
                    remainder = i - 100
                    if remainder // 100 < 3:
                        roman_numeral_remainder = self.to_roman_helper(remainder)
                        roman_list.append("C" + roman_numeral_remainder)
                    else: 
                        roman_list.append("CD")

            elif len(str(i)) == 2: 
                if i // 50 :
                    remainder = i - 50
                    if remainder // 10  < 4:
                        roman_numeral_remainder = self.to_roman_helper(remainder)
                        roman_list.append("L" + roman_numeral_remainder)
                    else:
                        roman_list.append("XC")
                else:
                    remainder = i - 10
                    if remainder // 10  < 3:
                        roman_numeral_remainder = self.to_roman_helper(remainder)
                        roman_list.append("X" + roman_numeral_remainder)
                    else:
                        roman_list.append("XL")
            
            elif len(str(i)) ==1 and i != 0:
                roman_list.append(self.unit_romans[str(i)])
        
        roman_number = ''.join(roman_list)
        
        return roman_number


            
            

if __name__ == "__main__":
    roman = 3888
    num1 = NumberToRoman(roman) # CCCLXXXVIII
    print(num1.to_roman())

    