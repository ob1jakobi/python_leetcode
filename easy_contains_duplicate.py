"""
Python implementation of leetcode problem to test whether a list contains duplicate
entries.
"""

def contains_duplicate(nums: list[int]) -> bool:
    """
    Creates a set of the nums arg and compares the size of the set to the size
    of the arg as a list; if the sizes are the same, then there are no duplicates,
    but if the sizes are different, then there are duplicates in the list.
    """
    return len(set(nums)) != len(nums)


if __name__ == "__main__":
    nums1 = [1, 2, 3, 1]
    nums2 = [1, 2, 3, 4]
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 1]
    nums4 = [1]
    
    print(f"Test 1: nums1 is {nums1}")
    print(contains_duplicate(nums1))
    print(f"\nTest2: nums2 is {nums2}")
    print(contains_duplicate(nums2))
    print(f"\nTest3: nums3 is {nums3}")
    print(contains_duplicate(nums3))
    print(f"\nTest4: nums4 is {nums4}")

