ls = [9,8,7,6,5,4,3,2,1]

def sort(ls):
    length = len(ls)
    for x in range (1,length):
        check_value = ls[x]
        list_position = x
        while list_position>0 and ls[list_position-1]>check_value:
            ls[list_position] = ls[list_position-1]
            list_position-=1
        ls[list_position] = check_value
    return ls
print(sort(ls))
