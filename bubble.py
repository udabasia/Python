list_1 = [5,9,7,3,2,1]
def bubble(list_1):
    length = len(list_1)-1
    for x in range(length):
        for y in range(0,length):
            if list_1[y]>list_1[y+1]:
                temp = list_1[y]
                list_1[y]=list_1[y+1]
                list_1[y+1]=temp
    return list_1
print(bubble(list_1))
