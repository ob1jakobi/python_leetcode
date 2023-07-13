
def rotate(nums: list[int], k: int) -> None:
    """
    Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is a non-negative int.

    Examples:
    >>> my_list = [1, 2, 3, 4, 5, 6, 7]
    >>> rotate(my_list, 3)
    >>> my_list
    [5, 6, 7, 1, 2, 3, 4]
    >>> my_list = [-1, -100, 3, 99]
    >>> rotate(my_list, 2)
    >>> my_list
    [3, 99, -1, -100]
    """
    n = len(nums)
    rotated_nums = [0] * n
    for i in range(n):
        insert_index = (i + k) % n
        num = nums[i]
        rotated_nums[insert_index] = num
    for i in range(n):
        nums[i] = rotated_nums[i]


if __name__ == "__main__":
    import doctest
    doctest.testmod(name="rotate", verbose=True)

