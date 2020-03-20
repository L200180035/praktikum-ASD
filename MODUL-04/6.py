def binSe(kumpulan, target):
    low = 0
    high = len(kumpulan) -1
    data = []
    while low <= high:
        mid = (high + low) //2
        if kumpulan[mid] == target:
            data.append(kumpulan.index(target))
            return True
        elif target < kumpulan[mid]:
            high = mid -1
        else :
            low = mid +1
    return False

list = [38, 12, 99, 137, 299]
target1 = 99
target2 = 123

print ("nilai target :", target1)
print (binSe(list, target1))

print ("\nnilai target :", target2)
print (binSe(list, target2))
