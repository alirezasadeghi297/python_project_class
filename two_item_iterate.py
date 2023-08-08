list1=['a','a','b','c','c',2,2,3,3,3,3,5,5,5]
union_item=set(list1)
result=[]
for item in union_item:
    if list1.count(item)==2:
        result.append(item)

print(result)