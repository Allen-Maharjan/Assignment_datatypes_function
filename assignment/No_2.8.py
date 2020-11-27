#returning new unique list

def unique_list(*sample):
    sample_list = []
    for i in sample[0]:
        if i not in sample_list:
            sample_list.append(i)
    print(f"Unique list: {sample_list}")

sample = input("Enter elements of list: ")
sample_list = sample.split()
unique_list(sample_list)
