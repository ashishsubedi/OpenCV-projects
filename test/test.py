list1 = ['Alpha', 'Beta', 'Gamma', 'Sigma']
list2 = ['one', 'two', 'three', 'six']
tup = (list1,list2)
print(tup)

res = zip(list1,list2)

val = zip(*tup)

for i in res:
    print(i)

for i in val:
    print(i)
