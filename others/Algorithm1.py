import random
import math





def sample1(A):
    sum=0
    for i in range(len(A)):
        sum=sum+A[i]
    return sum

def sample2(A):
    sum=0
    for i in range(len(A)):
        for j in range(len(A)):
            sum=sum+A[i]*A[j]
    return sum

def sample3(A):
    sum=0
    for i in range(len(A)):
        for j in range(len(A)):
            random.shuffle(A)
            r=A[0:int(len(A)/2)]
            for k in range(len(r)):
                if r[k-1]>=r[k]:
                    l=r[k-1]
                elif r[k-1]<=r[k]:
                    l=r[k]
            sum=sum+l
    return sum

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

def selection(A):
    b=[]
    while A:
        m=0
        for i in range(0, len(A)):
            if A[i]>A[m]:
                m=i
        v=A.pop(m)
        b.insert(0,v)
    return b
        
def bubble(A):
    for i in range(0, len(A)):
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j]
    return A

def quick(A):
    if len(A) <2:
        return A
    bot=[]
    top=[]
    mid=[]
    n=A[random.randint(0,len(A)-1)]
    for a in A:
        if a<n:
            bot.append(a)
        elif a>n:
            top.append(a)
        else:
            mid.append(a)
    print(bot,mid,top)
    R=quick(bot)+mid+quick(top)
    return R

def binarySearch(array, value, low, high):
	if low > high:
		return False
	mid = (low+high) / 2
	if array[mid] > value:
		return binarySearch(array, value, low, mid-1)
	elif array[mid] < value:
		return binarySearch(array, value, mid+1, high)
	else:
		return mid













