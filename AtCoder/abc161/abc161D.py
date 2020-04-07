# https://atcoder.jp/contests/abc161/tasks/abc161_d
# ABC 161
# D. Lunlun Number

import heapq
import sys
 
def solve(k):
    if k < 10:
        return k
    
    heap = [1,2,3,4,5,6,7,8,9]
    heapq.heapify(heap)
 
    for i in range(k-1):
        lunlun = heapq.heappop(heap)
        lastDigit = lunlun  % 10
        # print lunlun
        heapq.heappush(heap, (lunlun*10) + lastDigit)
 
        if lastDigit == 0:
            newlunlun = (lunlun * 10) + 1
            heapq.heappush(heap, newlunlun)    
        elif lastDigit == 9:
            newlunlun = (lunlun * 10) + 8
            heapq.heappush(heap, newlunlun)  
        else:
            newlunlun1 = (lunlun * 10) + lastDigit + 1
            newlunlun2 = (lunlun * 10) + lastDigit - 1
            heapq.heappush(heap, newlunlun1)
            heapq.heappush(heap, newlunlun2)
 
    return heapq.heappop(heap)
 
k = input()
# k = 100000
print(solve(int(k)))