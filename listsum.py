def sumlist(list):
    sum=0
    for i in range(len(list)):
        sum=sum+list[i]
    return sum

list=[10,9,8,7,6]
print(list)
print("sum of list : ",sumlist(list))