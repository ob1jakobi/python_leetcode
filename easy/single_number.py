
def single_number(nums: list[int]) -> int:
    """
    Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.
    You must implement a solution with a linear runtime complexity and use only constant extra space.

    Example:
    >>> single_number([2,2,1])
    1
    >>> single_number([4,1,2,1,2])
    4
    >>> single_number([1])
    1
    """
    result = 0
    for num in nums:
        result ^= num
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(name="single_number", verbose=True)
