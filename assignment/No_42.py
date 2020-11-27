#converting list into tuple

sample = input("Enter the element to be in list: ")
sample_list = sample.split()
sample_tuple = tuple(sample_list)
print(f'list = {sample_list}')
print(f'tuple = {sample_tuple}')
