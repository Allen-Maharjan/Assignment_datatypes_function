#checking whether it is prime or not

def prime(number):
    if (number <= 1):
        print(f'{number} is not a prime number')
    elif (number==2):
        print("2 is prime number")
    else:
        for i in range (2,number):
            if (number%i) == 0:
                print(f"{number} is not a prime number")
                break
        else:
            print(f"{number} is a prime number")



number = int(input("Enter a number: "))
prime(number) if number >0 else print("Error")
