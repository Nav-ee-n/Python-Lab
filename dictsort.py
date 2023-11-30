import operator

d={1:5,2:10,2:15,3:20,4:25,5:30}

print('Original Dictionary : ',d)

sorted_d=sorted(d.items(),key=operator.itemgetter(1))
print('Dictionary in ascending order by key:',sorted_d)

sorted_d=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by key:',sorted_d)

