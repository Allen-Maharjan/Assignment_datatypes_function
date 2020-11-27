#replace last element in a list

sample = input("Enter the value of 1st list: ")
sample_list = sample.split()
sample1 = input("Enter the value of 2nd list: ")
sample1_list = sample1.split()
output = sample_list[0:-1]+sample1_list
print(output)
