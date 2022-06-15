def merge(arr,start,end):

    mid = start + (end-start)//2

    len1 = mid - start + 1
    len2 = end - mid

    arr1 = []
    arr2 = []

    k = 0
    for i in range(len1):
        arr1.append(arr[k])
        k+=1

    l = mid+1
    for j in range(len2):
        arr2.append(arr[l])
        l+=1

    i = 0
    j = 0
    idx = start
    # print("Hello")

    while i < len1 and j < len2:
        if arr1[i] < arr2[j]:
            arr[idx] = arr1[i]
            i+=1
            idx += 1

        else:
            arr[idx] = arr2[j]
            j+=1
            idx+=1

    while i < len1:
        arr[idx] = arr1[i]
        i+=1
        idx+=1

    while j < len2:
        arr[idx] = arr2[j]
        j+=1
        idx+=1

    



def mergeSort(arr,start,end):
    if start >= end:
        return

    mid = start + (end-start)//2

    mergeSort(arr,start,mid)
    mergeSort(arr,mid+1,end)

    merge(arr,start,end)


arr = [1, 2, 2, 3, 1, 3, 4, 6, 4]
mergeSort(arr,0,len(arr)-1)
print(arr)