'''
Created on Oct 26, 2021

@author: jtortorella23
'''


output = ''

def sum_of_digit(n):
''' 
Description of function:
This function finds the sum of the digits of a number. 

Input parameters:
takes 1 number, n (int)

returns:
int

example:
n = 33
output is 6 
'''


    if n< 10:
        return n
    else:
        return n%10 + sum_of_digit(n/10)





def recur_factorial(n): 
''' 
Description of function:
This function finds the factorial of a number

Input parameters:
takes 1 number, n (int)

returns:
int

example:
n = 5
output is 120
'''
    if n == 1:  
           
        return n  
       
    else:  
           
        return n*recur_factorial(n-1)  


def recur_summation(n):
''' 
Description of function:
This function finds the summation of a number

Input parameters:
takes 1 number, n (int)

returns:
int

example:
n = 4
output is 10
'''
    if n == 0:
        return n
    
    else:
        return n+recur_summation(n-1)


def recur_powers(n, a):
''' 
Description of function:
This function puts a base number to an exponent

Input parameters:
takes 2 numbers, n (int), a (int)

returns:
int

example:
n = 3
a = 2
output is 9
'''   
    if a == 1:
        return n
    
    elif a == 0:
        return 1
   
    else:
        return n*recur_powers(n, a-1)
        

def recur_fibonacci(n):
''' 
Description of function:
This function finds the nth term in the fibonacci sequence

Input parameters:
takes 1 number, n (int)

returns:
int

example:
n = 5
output is 3
'''
    if n <= 1:
        return n
    
    elif n == 0:
        return 0
    
    else:
        return (recur_fibonacci(n-1) + recur_fibonacci(n-2))


def recur_GCD(x, y):
''' 
Description of function:
This function finds the sum of the digits of a number. 

Input parameters:
takes 1 number, n (int)

returns:
int

example:
n = 33
output is 6 
''' 
    if y <= x and x % y == 0: 
        
        return y
    
    else:
        return recur_GCD(y, x % y)

def recur_product(a,b):

    """
               Summary and Description of Function:
               Finds the product of two numbers

               Parameters:
               a (int): The first number inputted by the user
               b (int): The second number inputted by the user

               Returns:
               a (int): The first number multiplied by the second
        """

    if b > 0:
        return a + recur_product(a,b-1)

    elif b == 0:
        return 0
       
def recur_sum_in_range(x, y):
    if x == y : 
        return y 
    
    else :
        return y + recur_sum_in_range(x, (y-1))
    
    
def reverse(the_list):
    
    temp = ""
    if len(the_list) == 0:
        return 
    
    else :
        pos = len(the_list) - 1
        
        token = the_list.pop(pos)
        temp = temp + token
    
        print(temp, end='')
        
        return reverse(the_list)
    
def product_of_digit(n):

    """
           Summary and Description of Function:
           Finds the product of the digits of a number

           Parameters:
           n (int): The number inputted by the user

           Returns:
           n (int): The number multiplied in the function
    """
    if n < 10:
        return n
    else:
        return n % 10 * product_of_digit(n // 10)


def main():
    
    which_math = input('What function do you want to use? \n Enter a 1 to find the sum of digits, \n enter A 2 to find facotrial, \n enter 3 to find summation, \n enter 4 for powers, \n enter 5 for fibonacci, \n enter 6 to find the greatest common divisor \n enter 7 to find your compound interest balance. \n enter 8 for product of two numbers \n Enter 9 for the sum of numbers in a range. \n enter 10 to reverse the digits of a number')
    
    which_math = int(which_math)
    
    if which_math ==1: 
        
        # Read number  SUM OF DIGITS
        number = int(input("Enter number to find the sum of its digits: "))
    
    # Function call
        digit_sum = sum_of_digit(number)
        
        # Display output
        print("Sum of digit of number %d is %d." % (number,digit_sum))
    
    
    
    
    elif which_math == 2: 
    
        # take input from the user  for factorial
        numfact = int(input('What number would you like to take the factorial of?'))
        
        # check is the number is negative  
        if numfact < 0:  
            print('Factorials do not exist for negative numbers. Please insert a positive integer.')  
        
        # for recursion depth
        elif numfact > 997:
            print('This program only calculates the factorials up to 997. Please enter less than or equal to 997.')
           
        elif numfact == 0:  
            print('The factorial of 0 is 1')  
           
        # finds the factorial  
        else:  
            print('The factorial of',numfact,'is',recur_factorial(numfact))
    
    
    elif which_math == 3:
    
        #SUMMATION
        summation_number = int(input('What number would you like to find the summation of?'))
        
        if summation_number < 0:
            print('Summations do not exist for negative numbers. Please insert a positive integer')
            
        elif summation_number == 0:
            print('The summation of 0 is 0')
            
        #recursion depth
        elif summation_number > 997:
            print('This program only works for numbers less than 998. Please insert a new number for summation.')
            
        #finds summation    
        else:
            print('The summation of', summation_number, 'is', recur_summation(summation_number))
            
    
    elif which_math == 4:     
        
        #POWERS 
        base_Number= int(input('What number would you like to be the base? Please enter a positive integer'))
        
        if base_Number < 0:
            print('This program does not exist for negative numbers. Please insert a positive integer')
            
        elif base_Number == 0:
            print('0 raised to any power is 0')
            
        power_number = int(input('What number do you want to raise the base to? (what exponent)'))
        
        if power_number < 0:
            print('This program does not exist for negative numbers. Please insert a positive integer')
        
        elif power_number == 0:
            print('Your number,', base_Number, 'to the ', power_number, 'power is 1')
            
        else:
            print('Your number,', base_Number, 'to the ', power_number, 'power is', recur_powers(base_Number, power_number))

    
    elif which_math == 5:
        fib_number = input('What term of the fibonacci sequence would you like to find?')
        
        fib_number= int(fib_number)
        
        if fib_number == 0:
            print('0 is the 0th term of sequence')
            
        elif fib_number == 1:
            print('1 is 1st term of sequence')
            
        else: 
            print('the', fib_number,' term is',  recur_fibonacci(fib_number), 'in the fibonacci sequence.')
            
            
            
    elif which_math == 6:
        x = input('What is the first number?')
        
        x= int(x)
        
        y = input('What is the second number?')
        
        y = int(y)
        
        print('The greatest common divisor for your two numbers is ',recur_GCD(x, y))
        
    elif which_math == 7:
       
        principle = input('What is your principle amount?')
        principle= int(principle)
        
        rate = input('What is the rate?')
        rate = int(rate)
        
        time = input('How many years?')
        time = int(time)
        
        print('Your compound interest balance is', recur_compound_interest_balance(principle, rate, time))
        

    elif which_math == 8:

        a = input("What is the first number?")
        a = int(a)

        b = input("What is the first number?")
        b = int(b)

        print(recur_product(a,b))
            
            
    elif which_math == 9:
        x= input('What number do you want to start on?')
        x = int(x)
        
        y = input('What number would you like to end on?')
        y = int(y)
        
        if x <0:
            print('This program is only for positive numbers')
            
        elif y <0:
            print('This program is only for positive numbers')
            
        else: 
            print('The sum of numbers in your range of', x, '-', y, 'is', recur_sum_in_range(x, y))
            
    elif which_math == 10:
        num = input('What number would you like to reverse?')
        print("Your number reversed is:")
        reverse(list(num))
   
        
        
       

            
        
if __name__ == '__main__':
    main()
