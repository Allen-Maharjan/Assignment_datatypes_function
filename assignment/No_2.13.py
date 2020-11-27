#to sort list of tuples

sample_list = [(1,2),(2,1),(3,12)]

sample_list.sort(key=lambda x:x[1])

print(sample_list)
