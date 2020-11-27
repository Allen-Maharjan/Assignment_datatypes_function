#filter a list of integer

sample_list = [1,2,3,4,5,6,7,8,9,10]

result = list(filter(lambda x : (x%2)==0,sample_list))

print(result)
