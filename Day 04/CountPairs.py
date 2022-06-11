def getPairsCount(arr, k):
    # code here
    d = {}
    count = 0
    for i in range(len(arr)):
        diff = k - arr[i]
        
        if arr[i] not in d:
            d[arr[i]] = 1

        else:
            d[arr[i]] += 1
    return d

arr = [1, 5, 7, 1]
print(getPairsCount(arr,6))