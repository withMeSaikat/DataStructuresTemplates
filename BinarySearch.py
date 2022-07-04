def bsLB(arr, val, l, r):
    print("Called bsLB(arr, {}, {}, {})".format(val, l, r))
    if l >= r:
        return l
        
    mid = (l + r) // 2
    if arr[mid] < val:
        return bsLB(arr, val, mid + 1, r)
    else:
        return bsLB(arr, val, l, mid)

def bsUB(arr, val, l, r):
    print("Called bsUB(arr, {}, {}, {})".format(val, l, r))
    if l >= r:
        return l
    
    mid = (r + l) // 2
    if arr[mid] > val:
        return bsUB(arr, val, l, mid)
    else:
        return bsUB(arr, val, mid + 1, r)

arr = [-5, -2, 0, 2, 2, 4, 7, 9, 22, 23, 24, 25, 100, 102, 103]
t = int(input())
while(t > 0):
    a = int(input())
    res = bsLB(arr, a, 0, len(arr))
    res2 = bsUB(arr, a, 0, len(arr))
    print("LOWER BOUND ---> Searched value:", a, " Found on index:", res, " Value:", arr[res])
    print("UPPER BOUND ---> Searched value:", a, " Found on index:", res2, " Value:", arr[res2])
    t -= 1
    