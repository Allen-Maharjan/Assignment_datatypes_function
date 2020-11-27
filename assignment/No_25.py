#checking the dictionary in a list is empty or not
def check_sample(sample_list):
    for i in sample_list:
        if i:
            return True
        else:
            return False

sample_list = [{},{},{}]
sample_list1 = [{1,2}, {} ,{} ]
print(f'{sample_list}= ',check_sample(sample_list))
print(f'{sample_list1}= ',check_sample(sample_list1))
