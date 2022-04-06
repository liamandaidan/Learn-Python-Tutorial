#The goal of this project is to input N and retrieve a sum of the digits recursivly.
#this is a newbie version to show how its done
import sys

print("Please enter an integer to find the value of N: ")
#step 1 read user input from console cast type to int
n = int(input())

def calc(n):
    """
    This will be our calculate function
    """
    #Step 2 work out 1 digit case
    if len(str(n)) == 1:
        return n
    else:
        #We need to add up the sum of the compnents and return it to calc(n)
        #convert integers to list
        nums = [int(x) for x in str(n)]
        sum = 0
        for x in nums:
            sum += x
            sys.stdout.write(str(x)+" + ")
        print("= "+str(sum))
        return calc(sum)


#Output
print(calc(n))