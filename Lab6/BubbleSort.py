#pseudo code for the bubble sort algorithm

#BUBBLESORT(A)

#step-1.  for i= 1 to A.length-1
#step-2.      for j= A.length downto i+1
#step-3.          if A[j]< A[j-1]
#step-4.              exchange A[j] with A[j-1]

#implementing the bubble sort algorithm

A =[]
for v in range(0, 5):
    A.append(int(input('Enter a number : ')))
print (A)

def bubbleSort(A):
    n = len(A)
    for i in range(1,n):
        for j in range(1,n-i+1):
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]

bubbleSort(A)
print('Sorted Array : ')
print(A)
