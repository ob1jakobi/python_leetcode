
def containsDuplicate(nums: list[int]) -> int:
    """
    Given an integer array `nums`, return `True` if any value appears at least twice in the array, and return
    `False` if every element is distinct.

    Examples:
    >>> containsDuplicate([1,2,3,1])
    True
    >>> containsDuplicate([1,2,3,4])
    False
    >>> containsDuplicate([1,1,1,3,3,4,3,2,4,2])
    True
    """
    """ Below is a more complicated solution that's similar to the Java implementation:
    my_set = set()
    for num in nums:
        if num in my_set:
            return True
        my_set.add(num)
    return False
    """
    return len(set(nums)) != len(nums)


if __name__ == "__main__":
    import doctest
    doctest.testmod(name="containsDuplicate", verbose=True)
