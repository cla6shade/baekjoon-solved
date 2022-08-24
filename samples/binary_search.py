def search(list, target):
    start = 0
    end = len(list) - 1
    while start <= end:
        mid = (start+end) // 2
        if list[mid] == target:
            return mid
        elif list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1