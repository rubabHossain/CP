# https://codeforces.com/contest/25/problem/A
# CF Beta Round 25
# A. IQ Test

n = int(input())
nums = [0] * n

inp = str(raw_input()).split(" ")


for i in range(n):
    nums[i] = int(inp[i])


t = 0
for i in range(3):
    t += (nums[i] % 2)

majority_rem = 0 if t < 2 else 1

for i in range(n):
    if nums[i] %2 != majority_rem:
        print(i+1)
