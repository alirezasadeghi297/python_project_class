
def is_primitive(number):
    if number%2!=0:
        for i in range(3,int(number**0.5+1),2):
            if number%i==0:
                return False
        return True
    else:
        return False
def primitive_sum(number):
    list1=[]
    sum_primitive=0
    if number>2:
        for num in range(3,number,2):
            if is_primitive(num):
                list1.append(num)
                sum_primitive+=num
            else:
                continue
        sum_primitive+=2
        list1.insert(0,2)
        return (list1,sum_primitive)
    elif number==2:
        return number
    else:
        return (f'the {number} is not in the range')
print(primitive_sum(18))




