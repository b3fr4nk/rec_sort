import random

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(n) Why and under what conditions?
    only checks each element once
    TODO: Memory usage: O(1) Why and under what conditions?
    no temp arrays/lists are created to swap/store anything"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    sorted_list = []
    while len(items1) != 0 or len(items2) != 0:
        if len(items1) == 0:
            sorted_list.append(items2.pop(0))
        elif len(items2) == 0:
            sorted_list.append(items1.pop(0))
        elif items1[0] < items2[0]:
            sorted_list.append(items1.pop(0))
        else:
            sorted_list.append(items2.pop(0))
    # while len(items1) != 0 and len(items2) != 0:
    #     if items1[0] < items2[0]
    return sorted_list

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: O(n logn) Why and under what conditions?
    every time the recursive algorithm is called there are less and less elements to sort
    TODO: Memory usage: O(n) Why and under what conditions?
    there is are temp lists created for each recursive step"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    left.sort()
    right.sort()

    output = merge(left, right)
    return output


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot. The pivot is the median value of the lowest index, the highest index, and the middle index
    from that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: O(n) Why and under what conditions?
    checking each element only once O(n) is best case
    TODO: Memory usage: O(n) Why and under what conditions?
    the list is not copied"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    
    # middle element for the median of three pivot method
    options = random.sample(range(low, high+1), 3) #add 1 to high because sample is exclusive
    if items[options[0]] > items[options[1]] and items[options[0]] < items[options[2]]:
        pivot_index = options[0]
    elif items[options[1]] > items[options[0]] and items[options[1]] < items[options[2]]:
        pivot_index = options[1]
    else:
        pivot_index = options[2]

    pivot_val = items[pivot_index]

    left = 0
    right = high
    left_swap = None
    right_swap = None
    while left < right:
        # check for the need to swap on the left hand side
        if left_swap == None:
            if items[left] > pivot_val:
                left_swap = left
            else:
                left += 1
        # check for the need to swap on the right hand side
        if right_swap is None:
            if items[right] < pivot_val:
                right_swap = right
            else:
                right -= 1
        # swap the left and the right
        if left_swap is not None and right_swap is not None:
            items[left_swap], items[right_swap] = items[right_swap], items[left_swap]
            left_swap = None
            right_swap = None
    # move the pivot index to the correct position
    items[left], items[pivot_index] = items[pivot_index], items[left]

    return (items, left) # return the partitioned array and the partition index



def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    if high is None:
        high = len(items) - 1
    if low is None:
        low = 0

    if high <= 1:
        return items
    
    items, pivot = partition(items, low, high)

    left = quick_sort(items[:pivot])
    right = quick_sort(items[pivot:])

    return merge(left, right)

# merge_sort([1, 3, 5, 2, 4, 9, -1])
print(quick_sort([1, 3, 5, 2, 4, 9, 1], 0, 6))
# print(partition([1, 3, 5, 2, 4, 9, 10], 0, 6))