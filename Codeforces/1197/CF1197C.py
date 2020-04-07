#1197C
# Educational Round 69
# C - Array Splitting

import heapq

def solve(nums, k):
    diffs = [0] * (len(nums) - 1)
    for i in range(len(nums)-1):
        diffs[i] = -1*(nums[i+1]-nums[i])
    heapq.heapify(diffs)
    for i in range(k-1):
        heapq.heappop(diffs)
    # print(diffs)
    return sum(diffs) * -1


a = [int(x) for x in raw_input().split()]
nums = [int(x) for x in raw_input().split()]

print(solve(nums, a[1]))
