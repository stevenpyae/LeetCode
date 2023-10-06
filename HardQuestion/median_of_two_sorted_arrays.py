def merge_arrays(nums1, nums2, m, n, merged_array):
    i = 0
    j = 0
    k = 0

    # Put everything from first array nums1
    while (i < m):
        merged_array[k] = nums1[i]
        i += 1
        k += 1

    # put everything from second array nums2
    while (j < n):
        merged_array[k] = nums2[j]
        j += 1
        k += 1

    # sort the combined array
    merged_array.sort()


def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    m = len(nums1)
    n = len(nums2)

    print("m is : {}".format(m))
    print("n is : {}".format(n))

    ##get the merged array
    # create the final array with size M+N
    merged_array = [0 for i in range(m + n)]
    merge_arrays(nums1, nums2, m, n, merged_array)

    if len(merged_array) % 2 == 0:
        # even

        # Get the half + half-1 and divide by two
        return (merged_array[int(len(merged_array)/2)] + merged_array[int((len(merged_array)/2)) - 1]) / 2.0

    else:
        # odd get the middle one
        return merged_array[int(len(merged_array) / 2)]


if __name__ == "__main__":
    nums1 = [1,3]
    nums2 = [2]
    print(findMedianSortedArrays(nums1,nums2))