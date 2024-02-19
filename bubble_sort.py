def bubble_sort(arr):
    a_len = len(arr)
    for i in range(a_len):
        for j in range(0, a_len-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        yield arr