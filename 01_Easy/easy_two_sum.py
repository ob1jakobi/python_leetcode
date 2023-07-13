

def two_sum(nums: list[int], target: int) -> list[int]:
    my_map = dict()
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in my_map:
            return [i, my_map.get(complement)]
        my_map[num] = i
    return list()


if __name__ == "__main__":
    nums1 = [2, 7, 11, 15]
    nums2 = [3, 2, 4]
    nums3 = [3, 3]

    target1 = 9
    target2 = 6
    target3 = 6

    all_nums = [nums1, nums2, nums3]
    all_targets = [9, 6]

    for ns in all_nums:
        for t in all_targets:
            print(f"nums: {ns},\ttarget: {t},\ttwo_sum: {two_sum(ns, t)}\n")
