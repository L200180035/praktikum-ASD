def mengurutkan(A,B):
    C = A+B
    n = len(C)
    for i in range(1,n):
        nilai=C[i]
        pos=i
        while pos > 0 and nilai < C[pos-1]:
            C[pos]=c[pos-1]
            pos=pos-1
        C[pos] = nilai
    return C
A = [21,23,25,27,29]
B = [31,33,35,37]
