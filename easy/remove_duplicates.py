

def removeDuplicates(nums: list[int]) -> int:
    """
    Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each
    unique element appears only once. The relative order of the elements should be kept the same. Then return
    the number of unique elements in `nums`.
    Consider the number of unique elements of `nums` to be `k`; to get accepted, you need to do the following
    things:
    (1) Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the
        order they were present in `nums` initially. The remaining elements of `nums` are not important as well
        as the size of `nums`.
    (2) Return `k`.

    Examples:
    >>> removeDuplicates([1,1,2])
    2
    >>> removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    5
    """
    count = 1             # nums contains at least 1 element -> count must be initialized to 1
    i = 0
    j = 1
    while j < len(nums):
        iNum = nums[i]
        jNum = nums[j]
        if iNum != jNum:
            i += 1
            nums[i] = jNum
            count += 1
        j += 1
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod(name="removeDuplicates", verbose=True)
