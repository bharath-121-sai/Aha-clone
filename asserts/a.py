def merge(arr1, arr2):
    n, m = len(arr1), len(arr2)
    i, j, k = n - 1, m - 1, n + m - 1
    arr1.extend([0] * m)
    
    while i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1
    
    while j >= 0:
        arr1[k] = arr2[j]
        j -= 1
        k -= 1
    
    return arr1

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
print(merge(arr1, arr2))
