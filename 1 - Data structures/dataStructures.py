from collections import OrderedDict

List = [1, 2,  3,4,4,3]
Tuple = ('Hello', 'World')
Dict = {'Name': 'Python', 1: [1, 2, 3, 4]}


dict1 = dict()
#dict1 = OrderedDict()
dict1['b'] = 1
dict1['a'] = 2
dict1['c'] = 3


# print(dict1)

# dict1.pop('a')
# print(dict1)

# dict1['a'] = 2
# print(dict1)

# set
set1 = {1, 2, 3}
#set1 = frozenset({1, 2, 3})
set2 = {3, 4, 5}

set1.add(4)

#suma
print(set1 | set2)

#czesc wspolna
print(set1 & set2)

#roznica
print(set2 - set1)

#symetryczna roznica
print(set1 ^ set2)
