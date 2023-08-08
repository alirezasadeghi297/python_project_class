list1=[1,2,3,'a','a','b']
list2=[1,3,'z','b',4]

def intersection(list1,list2):
    union_item1=set(list1)
    union_item2=set(list2)
    union_item1.symmetric_difference_update(union_item2)
    return(union_item1)

print(intersection(list1,list2))