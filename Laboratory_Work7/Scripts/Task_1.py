import numpy as np
import time
import random

count = 1000000
lowBound = -1000
upBound = 1000


npmass1 = np.random.randint(lowBound, upBound, count)
npmass2 = np.random.randint(lowBound, upBound, count)

rand_list1=[]
rand_list2=[]
for i in range(count):
    rand_list1.append(random.randint(lowBound,upBound))
for i in range(count):
    rand_list2.append(random.randint(lowBound,upBound))

#measured time with numpy
tStartNp = time.perf_counter()
npComposition = np.multiply(npmass1, npmass2)
allTimeNp = time.perf_counter() - tStartNp

#measured time with a list
tStartList = time.perf_counter()
listComposition = []
for i in range(count):
    listComposition.append(rand_list1[i]*rand_list2[i])
allTimeList = time.perf_counter() - tStartList

print("Время затрченое на поэлементное умножения массива с библиотекой Numpy: ", allTimeNp)
print("Время затрченое на поэлементное умножения массива без библиотекой Numpy: ", allTimeList)


