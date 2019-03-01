nums1 = input('Enter comma separated numbers: ')
nums2 = input('Enter more comma separated numbers: ')

nums1_set = set(item for item in nums1.split(', '))
nums2_set = set(item for item in nums2.split(', '))

common = [int(item) for item in nums1_set.intersection(nums2_set)]
common.sort()
common = [str(item) for item in common]

sep = ','
print(sep.join(common))