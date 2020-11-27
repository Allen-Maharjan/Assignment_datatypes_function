#getting square and cube of every

sample_list = [1,2,3,4,5,6,7]
result = list(map(lambda x : x**2,sample_list))
result1 = list(map(lambda x:x**3,sample_list))
print("The square is :",result)
print("The cube is: ",result1)
