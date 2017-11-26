# max_pairwise_product
# Uses python3
# Max time used: 0.16/5.00, max memory used: 28073984/536870912

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

a.sort()

print(a[n-1] * a[n-2])

# result = sorted[n-1]*sorted[n-2]

# result = 0
#
# for i in range(0, n):
#     for j in range(i+1, n):
#         if a[i]*a[j] > result:
#             result = a[i]*a[j]

# print(result)
