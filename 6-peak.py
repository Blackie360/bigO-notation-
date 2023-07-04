def find_peak(nums):
    if not nums:
        return None

    start = 0
    end = len(nums) - 1

    while start < end:
        mid = (start + end) // 2

        if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
            return nums[mid]

        if nums[mid] < nums[mid + 1]:
            start = mid + 1
        else:
            end = mid - 1

    if start == end:
        return nums[start]

    return None


def main():
    # Test cases
    test_cases = [
        [1, 2, 3, 4, 5, 6, 5, 4, 3],
        [5, 10, 20, 15, 12],
        [10, 8, 6, 4, 2],
        [1, 3, 5, 7, 9],
        [7, 6, 5, 4, 3, 2, 1],
    ]

    complexity = "O(log n)"

    with open("6-peak.txt", "w") as f:
        f.write(f"The time complexity of the algorithm is: {complexity}\n")

    for i, nums in enumerate(test_cases):
        peak = find_peak(nums)
        if peak is not None:
            print(f"Peak of test case {i + 1}: {peak}")
        else:
            print(f"No peak found for test case {i + 1}")


if __name__ == "__main__":
    main()
