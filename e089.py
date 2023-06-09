"""
Problem 89 - Roman numerals
"""
from myfunc import roman2int, int2roman

# 1.open and read the file (roman.txt)
file = open("p089_roman.txt")
text = file.read()
roman_numerals = text.split()
file.close()

# 2.count the characters in the text file
num_of_characters = sum([len(roman) for roman in roman_numerals])

# 3.convert each roman numeral to integer
numbers = [roman2int(roman) for roman in roman_numerals]

# 4.convert integer back to roman numeral in its minimal form
new_roman_nuerals = [int2roman(number) for number in numbers]

# 5.count the characters of roman numerals in its minimal form
num_of_characters2 = sum([len(roman) for roman in new_roman_nuerals])

# 6.subtract result (5) from result (2)
print(num_of_characters - num_of_characters2)

# # copied solution ---- one liner
# print(sum(len(s) - len(s.
#                        replace('CCCC', 'CD').
#                        replace('XXXX', 'XL').
#                        replace('IIII', 'IV').
#                        replace('DCD', 'CM').
#                        replace('LXL', 'XC').
#                        replace('VIV', 'IX')
#                        )
#           for s in open('p089_roman.txt')
#           )
#       )
