#set of all subset
#design and implement python program to find a subset of a given set S ={s1,s2,s3..,sn}of n positive integers whose sum is equal to a given positive integer d

# s = list(map(int , input("Enter the numbers:").split()))
# subsets = [ [] ]

# for i in s:
#     subsets += [j + [i]for j in subsets]

# for k in subsets:
#     print(k)

# d=int(input("Enter the num:"))
# if sum(k) == d:
#     print(k)


def sumset(subsets):
    d = int(input("Enter sum to find:"))
    sum = []
    for j in subsets:
        if sum(j) == d:
            sum.append(j)
    if not sum:
        print("No such Subset Found.")
    else:
        print(sum)

if __name__ == "__main__":
    s = list(map(int,input("Enter the Number:").split()))
    subsets = [[]]
    for i in s:
        subsets += [ j + [i] for j in subsets]
    print(subsets)
    sumset(subsets)