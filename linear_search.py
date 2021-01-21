def linear_search(item,collections):

    for index_position in  range(len(collections)):
        if collections[index_position] == item:
            return index_position,"item found"
        return -1,"item not found"
print(linear_search(12,[31,2,4,6,8,10,12,1,2,4,3,5,6,7,787,65]))

 