#fucntion to calculate tpper case and lower

def calc(sample):
    count1,count2 = 0,0
    for i in sample:
        if i.isupper():
            count1 += 1
        elif i.islower():
            count2 += 1
        else:
            continue
    print(f'Sample String = {sample}\nNo.of Upper case character: {count1}\nNo.of lower case charater: {count2}')


sample = input("Enter a sentence: ")
calc(sample)
