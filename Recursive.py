'''
Created on Oct 26, 2021

@author: jtortorella23
'''


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
   
    if n == 1:
        return a
   
    else:
        return a*recur_powers(n-1, a)
        
   
   
    
def main():



    # take input from the user  for factorial
    numfact = int(input('What number would you like to take the factorial of?'))  \
    
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
        


       
if __name__ == '__main__':
    main()