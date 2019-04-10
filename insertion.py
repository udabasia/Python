list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
def insertion_sort(list1):
    length = len(list1)
    for x in range (1,length):
        check_value = list1[x]
        list_position=x
        while list_position>0 and list1[list_position-1]>check_value:
            list1[list_position]=list1[list_position-1]
            list_position-=1
        list1[list_position]=check_value
    return list1
print(insertion_sort(list1))
                
