#multiply all element of list

def mul_all(*args):
    print("list= ",args[0])
    mul = 1
    for i in args[0]:
        mul *= int(i)
    print("the multiple of list= ",mul)



numbers = input("Enter the list of numbers: ")
numbers_list = numbers.split()
mul_all(numbers_list)
