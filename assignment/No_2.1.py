#python function to find the max of three numbers
def max_num(*args):
    largest = int(args[0][0])
    for i in args[0]:
        if largest < int(i):
            largest = int(i)
    print(largest)


numbers = input("Enter three numbers: ")
numbers_list = numbers.split()
max_num(numbers_list)
