#calculating factorial of a number

def factorial(num):
    output = 1
    if num<0:
        print('Error')
    elif(num == 0):
        print("The factorial of 0 is 1.")
    else:
        for i in range(1,num+1):
            output *= i
    print(f"The factorial of {num} is {output}")

number= int(input("Enter a number= "))
factorial(number)
