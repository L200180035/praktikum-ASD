#latihan halaman 47
def swap(A,p,q):
    tmp=A[p]
    A[p]=A[q]
    A[q]=tmp

#latihan halaman 48
def cariPosisiTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil=dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i] < A[posisiTerkecil]:
            posisiTerkecil=i
    return posisiTerkecil

#latihan halaman 50
def bubbleSort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                swap(a,j,j+1)

#latihan halaman 52
def selectionSort(a):
    n=len(a)
    for i in range(n-1):
        indexKecil=cariPosisiTerkecil(a,i,n)
        if indexKecil != i:
            swap(a,i,indexKecil)

#latihan halaman 53
def insertionSort(A):
    n=len(A)
    for i in range(1,n):
        nilai=A[i]
        pos=i
        while pos > 0 and nilai < A[pos-1]:
            A[pos]= A[pos-1]
            pos=pos-1
        A[pos] = nilai
