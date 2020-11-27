#printing the even numbers:

def even(*number):
    output = []
    for i in number[0]:
        if int(i) % 2 == 0:
            output.append(int(i))
    print("Result= ",output)



sample = input("Enter the elements of list: ")
sample_list = sample.split()
even(sample_list)
