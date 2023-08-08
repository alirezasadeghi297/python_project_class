list1=['a','a','b','c',2,2,2]
# print(max(list1))
union_item=set(list1)
item_count={}
for item in union_item:
    item_count.update({item:list1.count(item)})
max_item=max(item_count,key=item_count.get)
print(max_item)
