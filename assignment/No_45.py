#to find index of an item

sample_tuple = ('1','2','3','4','5')
print('sample_tuple= ',sample_tuple)
sample_list = list(sample_tuple)
find = input("Enter the element to find: ")
print("The element is in ",sample_list.index(find))
