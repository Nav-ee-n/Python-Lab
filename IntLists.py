list1=[1,2,3,4,5]
print('List 1 : ',list1)
list2=[5,10,15,20,25]
print('List 2 : ',list2)

if(len(list1)==len(list2)):
    print('Lists are same length')
else:
    print('Lists are of different length')

sum1=0
for i in range(0,len(list1)):
    sum1=sum1+list1[i]
sum2=0
for i in range(0,len(list2)):
    sum2=sum2+list2[i]

if(sum1==sum2):
    print('Lists sums to same value')
else:
    print('Lists sums to different value')

common=set(list1).intersection(list2)
if common:
    print("There is a common value")
else:
    print("There are no common values")
