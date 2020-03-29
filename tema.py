import random
import time


#Bubble Sort
def bubbleSort(list):
    l = list.copy()
    ok = True
    while (ok == True):
        ok = False
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                ok = True
                l[i],l[i+1]=l[i+1],l[i]
    return l

#Count Sort
def countSort(list):
    l = [0] * len(list)
    max1 = max(list)+1
    contor = [0] * max1

    for i in list:
        contor[i] += 1
    cnt = 0
    for i in range(max1):
        for a in range(contor[i]):
            l[cnt] = i
            cnt += 1
    return l

#Radix Sort
def radCountSort(list, p):
    n= len(list)
    l=[0]*n
    cont=[0]*10
    for i in range (0,n):
        x=(list[i]//p)
        cont[x%10] +=1
    for i in range (1, 10):
        cont[i]+=cont[i-1]
    i=n-1
    while i>=0:
        x=(list[i]//p)
        l[cont[(x)%10]-1]=list[i]
        cont[(x)%10]-=1
        i-=1
    i=0
    for i in range (0,len(list)):
        list[i]=l[i]


def radixSort(list):
    l = list.copy()
    max1 = max(list)
    p = 1
    while max1 // p > 0:
        radCountSort(l, p)
        p *= 10
    return l

#Merge Sort

def merge(ls, l, m, r):
    a = m - l + 1
    b = r - m

    L = ls[l:m + 1]
    R = ls[m + 1:r + 1]
    i = 0
    j = 0
    c = l
    while i < a and j < b:
        if L[i] <= R[j]:
            ls[c] = L[i]
            i += 1
        else:
            ls[c] = R[j]
            j += 1
        c += 1
    while i < a:
        ls[c] = L[i]
        i += 1
        c += 1
    while j < b:
        ls[c] = R[j]
        j += 1
        c += 1


def mergeSort(list):
    ls = list.copy()
    r = len(ls) - 1
    mergeRec(ls, 0, r)
    return ls


def mergeRec(list, l, r):
    if l >= r:
        return
    m = (l + r) // 2
    mergeRec(list, l, m)
    mergeRec(list, m + 1, r)
    merge(list, l, m, r)

#Quick Sort

def part(list, a, b):
    i = a - 1
    pivot = list[b]

    for j in range(a, b):
        if list[j] <= pivot:
            i += 1
            list[i], list[j] = list[j], list[i]
    list[i + 1], list[b] = list[b], list[i + 1]
    return i + 1


def quickSort(list):
    l = list.copy()
    b = len(list) - 1
    quickRec(l, 0, b)
    return l


def quickRec(list, a, b):
    if a < b:
        p = part(list, a, b)
        quickRec(list, a, p - 1)
        quickRec(list, p + 1, b)

teste=[]

print("Introduceti numarul de teste dorite: ")
nr_teste=int(input())
print("Introduceti %s combinatii de forma [numar de valori] [valoare maxima] pentru fiecare test:" %nr_teste)
for i in range(nr_teste):
    test=input()
    teste.append(tuple(map(int, test.split())))
for i in range(len(teste)):
    print("Testul %s: " %int(i+1)  )
    print("Numar de variabile: %s" %teste[i][0] )
    print("Valoare maxima: %s" % teste[i][1])
    list= [random.randrange(0,teste[i][1],1) for _ in range(teste[i][0])]
    verif=sorted(list)
    if teste[i][0]>10000:
        print("Prea multe valori pentru Bubble Sort")
    else:
        start=time.time()
        l=bubbleSort(list)
        timp=float((time.time()-start))
        if l!=verif:
            print("Bubble Sort nu a sortat cu succes lista")
        else:
            print("Timp Bubble Sort: %s " %timp)
    if teste[i][1]>1000000:
        print("Valori prea mari pentru Count Sort")
    else:
        start=time.time()
        l=countSort(list)
        timp=float((time.time()-start))
        if l!=verif:
            print("Count Sort nu a sortat cu succes lista")
        else:
            print("Timp Count Sort: %s " %timp)
    start = time.time()
    l = radixSort(list)
    timp = float((time.time() - start))
    if l != verif:
        print("Radix Sort nu a sortat cu succes lista")
    else:
        print("Timp Radix Sort: %s " % timp)
    start = time.time()
    l = mergeSort(list)
    timp = float((time.time() - start))
    if l != verif:
        print("Merge Sort nu a sortat cu succes lista")
    else:
        print("Timp Merge Sort: %s " % timp)
    start = time.time()
    l = quickSort(list)
    timp = float((time.time() - start))
    if l != verif:
        print("Quick Sort nu a sortat cu succes lista")
    else:
        print("Timp Quick Sort: %s " % timp)

