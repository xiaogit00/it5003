def merge_sort(lst):
    if len(lst)<2 :
        return lst
    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    print(f"merge({left}, {right})")
    results = []
    while left and right:               # This will run N times for left & right of size N -> thus O(N)
        if left[0] < right[0]:
            results.append(left.pop(0))
        else:
            results.append(right.pop(0))
    results.extend(left)
    results.extend(right)
    print(f"result: {results}")
    return results

print(merge_sort([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]))

'''
Tracing
[4, 2, 3, 1]

merge_sort([4, 2, 3, 1])
    mid = 2
    left = merge_sort([4, 2])               ------ merge_sort([4,2]) 
    ------    ------    ------    ------    ------ [2, 4]
    right = merge_sort([3, 1])              ------ merge_sort([3,1])
    ------    ------    ------    ------    ------ [1, 3]  
    return merge(left, right)
    ------    ------    ------    ------    ------    ------    ------     merge([2, 4], [1, 3])
    ------    ------    ------    ------    ------    ------    ------     [1, 2, 3, 4]
    ------    ------    ------    ------    ------ merge_sort([4,2])
    ------    ------    ------    ------    ------ mid = 1
    ------    ------    ------    ------    ------ left = merge_sort([4]) = [4]
    ------    ------    ------    ------    ------ right = merge_sort([2]) = [2]
    ------    ------    ------    ------    ------ merge([4], [2])
    ------    ------    ------    ------    ------ results = [2, 4]
'''