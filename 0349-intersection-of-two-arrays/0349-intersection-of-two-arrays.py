class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        intersection = []
        for i in nums1_set:
            if i in nums2_set:
                intersection.append(i)

        return intersection
        # seen=set(nums1)
        # res=[]
        # for n in nums2:
        #     if n in seen:
        #         res.append(n)
        #         seen.remove(n)
        # return res
    