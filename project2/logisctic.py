a={1,3,4,5,6,7,87}

a.add(22)
print(a)
a.update({23,5,32,42})
print(a)

a.remove(32)
print(a)

b={20}
b.discard(2)
print(b)

print(a.union(b))
s=[55,456,456,144,145,1044,55,145,456,55]
from collections import Counter
cnt=Counter(s)
print(cnt)
print(cnt.most_common(1))