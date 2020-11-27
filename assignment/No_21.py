#sorting in increaing order in tuple

sample_list = [(2,5), (1,2),(4,4),(2,3),(2,1)]
print("Sample List: ",sample_list)
#temp = []
# for i in range(0,len(sample_list)):
#     for j in range(i,len(sample_list)):
#         if (sample_list[i][1]>sample_list[j][1]):
#             temp.append(sample_list[i] )
#             sample_list[i] = sample_list[j]
#             sample_list[j] = temp[0]
#             temp.remove(sample_list[j])

sample_list.sort(key=lambda x :x[1])
print("final result= ",sample_list)
