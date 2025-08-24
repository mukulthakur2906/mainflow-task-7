def merge_count_split_inv(arr, temp, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_count_split_inv(arr, temp, left, mid)
        inv_count += merge_count_split_inv(arr, temp, mid + 1, right)
        inv_count += merge(arr, temp, left, mid, right)
    return inv_count

def merge(arr, temp, left, mid, right):
    i, j, k = left, mid + 1, left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += (mid - i + 1)  # Count inversions
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]
    return inv_count

def count_inversions(arr):
    return merge_count_split_inv(arr, [0]*len(arr), 0, len(arr)-1)

# Example
arr = [1, 20, 6, 4, 5]
print("Inversion Count:", count_inversions(arr))
