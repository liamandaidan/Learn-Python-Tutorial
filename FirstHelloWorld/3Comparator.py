# Declare vars
conditionA = True
conditionB = False
print("condtionA is:")
print(conditionA)
print("condtionB is:")
print(conditionB)

# we can compare boolean types with:
# ==, !=, >, >=, <, <=
# equal to, not equal to, greater than, greater or equal to, less than, less or equal to
print("Does conditionA==conditionB?")
print(conditionA == conditionB)
# output: False. ConditionA Equal to ConditionB. Therefore with our inputs is False.
print("Does conditionA!=conditionB")
print(conditionA != conditionB)
# output: True. ConditionA does not equal ConditionB. Therefore with our inputs is True

# we can compare other things as well! It will still however return a boolean value of T/F
num1 = 1
num2 = 2

print("Is num1 < num2?")
print(num1 < num2)

print("Is num1 >= num2?")
print(num1 < num2)

# Finally we can use an IF statement to dictate the flow of our code
print("If Statement. Is num1 less than num2?")
# keep in mind python will indent code to show it belongs to a block...
# one tab or 4 spaces.
if num1 < num2:
    print("num1 is less than num2!")
else:
    #else is the default case that triggers when a condition is not found.
    print("num2 is less than num1")
print()
#One last format of IF contains elif
print("elif Example")
if num1 == num2:
    print('Num1 equals num2')
elif num1 >= num2:
    #known as ELSE IF
    print('Num1 greater than or equal num2')
elif num1 == 10:
    print('num1 equals to 10')
elif num1 + num2 == 3:
    # This condition is the only one that will trigger
    print('num1+num2 = 3')
else:
    print('num1 does not trigger any other condition.')

