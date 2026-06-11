num = int(input("\nEnter a integer: "))

while num < 1 or num > 3999:
    print("Please enter a integer between 1 and 3999.")
    num = int(input("Enter a integer: "))

class RomanNumeral:
    def __init__(self, value):
        self.value = value    

    def to_roman(self):
        arabic = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        roman = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        
        answer = ""

        while self.value > 0:
            for i in range(len(arabic)):
                if self.value >= arabic[i]:
                    answer += roman[i]
                    self.value -= arabic[i]
                    break
        return answer
    
roman_numeral = RomanNumeral(num)
print(f"The Roman numeral for {num} is: {roman_numeral.to_roman()}\n")
