
my_dict={'dave':'001','ava':'002','joe':'003'}
print(my_dict)
print(type(my_dict))
print('-----------')
new_dict=dict()
print(new_dict)
print(type(new_dict))
print('---------')
#Creating Nested Dictionaries:
emp_detaily={'Employee':{
             'dava':{
                 'id':'001','salary':2300,'designation':'python developer'},
             'ava':{
                 'id':'002','salary':3000,'designation':'java developer'},
             'joe':{
                 'id':'003','salary':5000,'designation':'scala developer'},
             'menge':{
                 'id':'004','salary':2000,'designation':'c++ developer'}}}
print(emp_detaily)
print(type(emp_detaily))
"""
Accessing Values:
 ==>The values of a dictionary can be accessed in many ways such as:
       => Using key values
       => Using functions
       => Implementing the for loop
"""
# using key values
print(my_dict['dave'])
print(my_dict.keys())
print(my_dict.values())
print(my_dict.get('dave'))
# using function implementations
print("all keys")
for key in my_dict:
    print(key)
print("all valus")
for val in my_dict.values():
    print(val)
print('all keys and values')
for key,val in my_dict.items():
    print('key : '+val,' value : '+val)
# updating dictionary
my_dict['dave']='004'
print(my_dict)
my_dict['chris']='005'
print(my_dict)

# deleting items from dictionars :
#del my_dict['dave']  #removes key-value pair of 'Dave'
#my_dict.pop('ava')   #removes the value of 'Ava'
#my_dict.popitem()    #removes the last inserted item
#print(my_dict)

import  pandas as pd
df=pd.DataFrame(emp_detaily['Employee'])
print(df)
