#find intersection between two arrays

sample = [1,2,3,4,5,6]
sample1 = [4,5,6,7]
result = list(filter(lambda i : i in sample,sample1))
print (result,"is the intersection.")
