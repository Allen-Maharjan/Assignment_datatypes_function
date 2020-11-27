#sorting list of dictionary

sample_list = [{'name':'Allen','age':24,'location':'kathmandu'},
                {'name':'Ram','age':21,'location':'Dhulikhel'},
                {'name':'Shyam','age':25,'location':'kirtipur'}]

sample_list.sort(key= lambda x:x['age'])

print(sample_list)
