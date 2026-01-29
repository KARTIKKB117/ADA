# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1

#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1

#         arr[j + 1] = key

#     return arr


# nums = [5, 2, 9, 1, 5, 6]
# print(insertion_sort(nums))

l = [1,2,3,4,8]
print(l)
n = len(l)
for i in range (1,n):
    j=i-1
    v=l[i]
    while j>=0 and l[j]>v:
        l[j+1]=l[j]
        j=j-1
    l[j+1]=v
print(l)
        