def sum_of_digit(n):
    if n< 10:
        return n
    else:
        return n%10 + sum_of_digit(n/10)





def recur_factorial(n): 
         
    if n == 1:  
           
        return n  
       
    else:  
           
        return n*recur_factorial(n-1)  


def recur_summation(n):
    
    if n == 0:
        return n
    
    else:
        return n+recur_summation(n-1)


def recur_powers(n, a):
   
    if a == 1:
        return n
    
    elif a == 0:
        return 1
   
    else:
        return n*recur_powers(n, a-1)
        

def recur_fibonacci(n):
    
    if n <= 1:
        return n
    
    elif n == 0:
        return 0
    
    else:
        return (recur_fibonacci(n-1) + recur_fibonacci(n-2))


    
       
    
def main():
    
    which_math = input('What function do you want to use? \n Enter a 1 to find the sum of digits, enter A 2 to find facotrial, enter 3 to find summation, enter 4 for powers, enter 5 for fibonacci')
    
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
            
        
            
            
       
if __name__ == '__main__':
    main()
