# Can you write a program that is able to tell if a integer number is even or odd?

number = 5
stringOutput = ""
# number is a variable you can change to test inputs

#HINT the % modulus operator leaves a remainder that you can work with ;)
if number%2 == 0:
    stringOutput = "Even"
else:
    stringOutput = "Odd"

print(stringOutput)