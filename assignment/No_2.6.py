#check whether the number is in a given range

def check(num,a,b):
    if (num>=a and num<b):
        print(f"The {num} is in range {a} and {b} ")
    else:
        print(f"The {num} is not in range {a} and {b} ")


number = input("Enter a number: ")
range = input("Enter the starting range and end range(seperated be space): ")
range_list = range.split()
check(number,range_list[0],range_list[1])
