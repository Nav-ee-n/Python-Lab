color1=input('Enter colors of first list : ').split(',')
print("List 1 : ",color1)

color2=input('Enter colors of second list : ').split(',')
print("List 2 : ",color2)

result=list(set(color1).difference(color2))
print('Colors in list 1 but not in list 2 : ',result)