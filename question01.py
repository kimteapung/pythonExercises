##Question 1
##Level 1
##
##Question:
##Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
##between 2000 and 3200 (both included).
##The numbers obtained should be printed in a comma-separated sequence on a single line.
##
##Hints: 
##Consider use range(#begin, #end) method

numbers = ""
for number in range(2000, 3201):
    if number%7 == 0 and number%5 != 0:
        numbers += str(number)+","
print numbers
