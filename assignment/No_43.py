#removing an item from tuple

sample_tuple = ('1','2','3','4','5')
print("initial tuple: ",sample_tuple)
delete = input("Enter the item to be deleted: ")
sample_list = list(sample_tuple)
sample_list.remove(delete)
sample_tuple = tuple(sample_list)
print("final tuple: ",sample_tuple)
