def comp(array1, array2):
    '''function accepts 2 arrays and returns true if all elements in array1 squared are present in array2'''
    # if array1 == None and array2 == None:
    #     return True
    # elif array1 == None or array2 == None:
    #     return False
    # for i in array1:
    #     if i**2 not in array2:
    #         return False
    # for i in array2:
    #     if i**(1/2) not in array1:
    #         return False
    # return True
    array2_sort = sorted(array2)
    clean_array1 = []
    for i in array1:
        clean_array1.append(i**2)
    array1_sort = sorted(clean_array1)
    zipped = zip(array1_sort,array2_sort)
    for i,j in zipped:
        if i != j:
            return False
    return True
''' way better code, need to look at lambda expressions and try them earlier instead of all the storing to varriables
    try:
        return sorted([i**2 for i in array1]) == sorted(array2)
    except:
        return False'''