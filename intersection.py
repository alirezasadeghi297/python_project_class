'''
code1
unique items:
'''
list1=[1,2,3,'a','a','ali',3,'alireza']
list2=[1,3,'z',4,3,'c','alireza','alireza']

def intersection(list1,list2):
    union_item1=set(list1)
    union_item2=set(list2)
    union_item1.symmetric_difference_update(union_item2)
    return(union_item1)

# print(intersection(list1,list2))

'''
code2
repeated items
'''
def intersection3(list1,list2):
    temp_list=list1.copy()
    for item in temp_list:
        if item in list2:
            list1.remove(item)
            list2.remove(item)
    return list1+list2
print(intersection3(list1,list2))
