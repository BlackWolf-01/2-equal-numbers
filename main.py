#Program to check if user input numbers are equal without using any comparison operator
def checkifsame(Number1,Number2):
    #Use XOR operator as a^a is always 0
    if((Number1^Number2)!=0):
        print('Numbers are not equal')
    else :
        print('Both numbers are equal')
#Taking input 
Number1=int(input('Enter first number to compare'))         
Number2=int(input('Enter second number to compare'))
checkifsame(Number1,Number2)     