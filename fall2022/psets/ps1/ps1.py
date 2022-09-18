from array import array
from asyncio import base_tasks
import math
import pdb
import time
import random

"""
See below for mergeSort and countSort functions, and for a useful helper function.
In order to run your experiments, you may find the functions random.randint() and time.time() useful.

In general, for each value of n and each universe size 'U' you will want to
    1. Generate a random array of length n whose keys are in 0, ..., U - 1
    2. Run count sort, merge sort, and radix sort ~10 times each,
       averaging the runtimes of each function. 
       (If you are finding that your code is taking too long to run with 10 repitions, you should feel free to decrease that number)

To graph, you can use a library like matplotlib or simply put your data in a Google/Excel sheet.
A great resource for all your (current and future) graphing needs is the Python Graph Gallery 
"""


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])
    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits

def radixSort(universe, b, arr):
    k = math.ceil(math.log2(universe) / math.log2(b))
    n = len(arr)
    for i in range(n):
        vi = BC(arr[i][0], b, k)
        arr[i] = [arr[i][0], arr[i][1], vi]

    for j in range(k):
        for i in range(n):
            arr[i][0] = arr[i][2][j]
        arr = countSort(b, arr)

    for i in range(n):
        key = 0
        for j in range(k):
            key += arr[i][2][j] * int(math.pow(b, j))
        arr[i] = (key, (arr[i][1]))
    return arr


def run_trials(n, U):
    avg_count = []
    avg_merge = []
    avg_radix = []
    arr = []
    for i in range(n): 
      arr.append((random.randint(0, U-1), i))
    for i in range(10):
        t = time.time()
        countSort(U, arr)
        t1 = time.time()
        avg_count.append(t1-t)
        mergeSort(arr)
        t = time.time()
        avg_merge.append(t-t1)
        radixSort(U, n, arr)
        t1 = time.time()
        avg_radix.append(t1-t)
    cou = sum(avg_count) / 10
    mer = sum(avg_merge) / 10
    rad = sum(avg_radix) / 10
    #print(avg_count, avg_merge, avg_radix)
    if cou < mer and cou < rad:
        return 'c'
    if mer < cou and mer < rad:
        return 'm'
    else:
        return "r"


def run_times():
    for i in range(1,17):
        n = 2**i
        for j in range(1,21):
            U = 2**j
            fastest = run_trials(n, U)
            print(n, U, fastest)
    return 'hi'

BC(120, 10, 1)
run_times()

""" 
def radixSort(univsize, b, arr): 
  k = math.ceil(math.log(univsize)/math.log(b))
  n = len(arr)
  vprime = []
  for i in range (n):
    vprime.append(BC(arr[i][0], b, k))
  working = []
  for j in range (k):
    for i in range (n):
      if j == 0:
        working.append([vprime[i][j], arr[i][1], vprime[i]])
      else:
        working[i][0] = working[i][2][j]
    working = countSort(b, working)
  sortedArr = [] 
  for i in range(n): 
    key = 0 
    for j in range(k):
      key += working[i][2][j] * pow(b, j)
    sortedArr.append((key, working[i][1]))
  return sortedArr
"""
""" 
def radixSort(univsize, b, arr): 
  k = math.ceil(math.log(univsize)/math.log(b))
  arr_prime = []
  for i in range (len(arr)):
    arr_prime.append(list(arr[i]))
    arr_prime[i].append(BC(arr[i][0], b, k))
  for j in range (k):
    for i in range (len(arr_prime)):
      arr_prime[i][0] = arr_prime[i][2][j]
    arr_prime = countSort(b, arr_prime)
  sortedArr = [] 
  for elt in arr_prime: 
    key = 0
    pow = 1
    for dig in elt[2]:
      key += dig * pow
      pow *= b
    sortedArr.append((key,elt[1]))
  return sortedArr
  """
""" 
b = 2 
for i in range (1, 17):
  for j in range (1, 21):
    arr1 = []
    arr2 = []
    arr3 = []
    n = pow(2, i)
    U = pow(2, j)

    for k in range (n):
      x = random.randint(0, U - 1)
      arr1.append((x, k))
      arr2.append((x, k))
      arr3.append((x, k))
    
    beg_r = time.time() 
    radixSort(U, b, arr1)
    end_r = time.time()
    time_r = end_r - beg_r

    beg_r = time.time() 
    mergeSort(arr2)
    end_r = time.time()
    time_m = end_r - beg_r

    beg_r = time.time() 
    countSort(U, arr3)
    end_r = time.time()
    time_c = end_r - beg_r

    if (time_r < time_c and time_r < time_m):
      print(n, U, "r")
    elif (time_c  < time_m):
      print(n, U, "c")
    else:
      print(n, U, "m")


"""

""" 
b= 2
n = pow(2, 2)
U = pow(2, 2)
arr = []


for k in range (n):
  arr.append((random.randint(0, U - 1), k))
print(arr)
print(radixSort(U, b, arr))
"""


""" 
for i in range (1, 17):
  for j in range (1, 21):
    arr = []
    n = pow(2, i)
    U = pow(2, j)

    for k in range (n):
      arr.append((random.randint(0, U - 1), k))
    avg_m = 0
    avg_c = 0
    avg_r = 0
    for k in range (10): 
      beg_r = time.time() 
      radixSort(U, b, arr)
      end_r = time.time()
      avg_r += end_r - beg_r 

      beg_m = time.time() 
      mergeSort(arr)
      end_m = time.time()
      avg_m += end_m - beg_m 

      beg_c = time.time() 
      countSort(U, arr)
      end_c = time.time()
      avg_c += end_c - beg_c

      
    avg_m /= 10
    avg_c /= 10
    avg_r /= 10

    if (avg_r < avg_c and avg_r < avg_m):
      print(n, U, "r")
    elif (avg_c < avg_m):
      print(n, U, "c")
    else:
      print(n, U, "m")

"""
