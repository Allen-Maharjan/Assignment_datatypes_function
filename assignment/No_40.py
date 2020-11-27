#adding element to tuple

sample_tuple = (1,2,3,4)
sample_list = list(sample_tuple)
print(f'initial tuple = {sample_tuple}')
add = input("Enter the element to be added: ")
sample_list.append(add)
sample_tuple = tuple(sample_list)
print(f'final tuple = {sample_tuple}')
