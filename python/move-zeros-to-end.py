# Moving zeros to the end
def move_zeros(array):
    count = array.count(0)
    while 0 in array:
        array.remove(0)
    for i in range(count):
        array.append(0)
    return(array)


# move_zeros([1, 0, 1, 2, 0, 1, 3])




