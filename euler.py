import math
def primefactor(num):
    factors = []
    for i in range(1, int(math.sqrt(num))+ 1):
        if num % i ==0:
            factors.append(i)
            if i != num //i:
                factors.append(num//i)
    return factors

def isprime(num):
    if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1,2)):
        return True
    else:
        return False
    
def ispalindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

def partition(list,low,high):
    i = low - 1
    pivot = list[high]
    for j in range (low,high):
        if list[j] <= pivot:
            i = i+1
            list[i],list[j] = list[j],list[i]
    list[i+1],list[high] = list[high],list[i+1]
    return(i+1)

def removeduplicates(list1):
    list1 = set(list1)
    list1 = list(list1)
    return list1 

def quicksort(list,low,high):
    if low < high:
        pi = partition(list,low,high)
        quicksort(list,low,pi-1)
        quicksort(list,pi+1,high)
    return(list)
'''
euler q3
num = 600851475143
list = primefactor(num)
primelist = []
flag = False
for i in range(0,len(list)):
    nnum = list[i]
    flag = isprime(nnum)
    if flag == True:
        primelist.append(nnum)
    else:
        pass


print(primelist)
'''

liste = []
for i in range (100,999):
    for j in range(100,999):
        num = str(i*j)
        flag = ispalindrome(num)
        if flag == True:
            liste.append(num)
        else:
            pass

liste = removeduplicates(liste)

liste = quicksort(liste,0,len(liste)-1)
print(liste)