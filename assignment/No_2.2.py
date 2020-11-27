#sum of all the numbers in a list

def sum_all(*args):
    print("list= ",args[0])
    sum = 0
    for i in args[0]:
        sum+= int(i)
    print("the sum of list= ",sum)



numbers = input("Enter the list of numbers: ")
numbers_list = numbers.split()
sum_all(numbers_list)
