'''
We call the process of changing an instance from memory to be stored or transferred called serialization
After serialization, you can write the serialized content(instance) to disk or transfer it to other
machine through the network. In turn, rereading the instance from a serialized content into memory is 
called deserialization 
'''
#pickle  module
import pickle
# d = dict(name='Bob', age=20, score=88)
# print(pickle.dumps(d))#Serialize any object into a byte
'''
output:
b'\x80\x04\x95$\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x03Bob\x94\x8c\x03age\x94K\x14\x8c\x05score\x94KXu.'
'''

# with open('E:\python_tutorial\sourceCode\dump.txt', 'wb') as f:
#     pickle.dump(d, f)

#deserialization

# with open('E:\python_tutorial\sourceCode\dump.txt', 'rb') as f:
#     print(pickle.load(f))

#json serialization
import json
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))





