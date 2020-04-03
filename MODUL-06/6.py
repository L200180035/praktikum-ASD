def quickSort(S):
    quicksorthelp(S, 0, len(S))

def quicksorthelp(S, low, high):
    result = 0
    if low < high:
        pivot_location, result = Partition(S, low, high)
        result += quicksorthelp(S, low, pivot_location)
        result += quicksorthelp(S, pivot_location + 1, high)
    return result

def Partition(S, low, high):
    result = 0
    pivot, pidx = median_of_three(S, low, high)
    S[low], S[pidx] = S[pidx], S[low]
    i = low + 1
    for j in range(low + 1, high, 1):
        result += 1
        if S[j] < pivot:
            S[i], S[j] = S[j], S[i]
            i += 1
    S[low], S[i - 1] = S[i - 1], S[low]
    return i - 1, result

def median_of_three(S, low, high):
    mid = (low + high - 1) // 2
    a = S[low]
    b = S[mid]
    c = S[high - 1]
    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, high - 1
    if b <= c <= a:
        return c, high - 1
    return a, low

listin = [11, 7, 9, 4, 90, 23, 2, 14, 67, 170]

quickSort(listin)
print(listin)
