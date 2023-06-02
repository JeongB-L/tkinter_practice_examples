class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # pointer to last of nums1
        last = m + n - 1 #this is equal to len(nums1) - 1
        # 오른쪽에서 왼쪽으로 merge(switching) 시작; m, n을 포인터로 사용
        m, n = m - 1, n - 1
        while m + 1> 0 and n + 1> 0:
            if nums1[m] > nums2[n]:
                nums1[last] = nums1[m]
                m -= 1
            else:
                nums1[last] = nums2[n]
                n -= 1
            last -= 1
        # 이제 nums1에 nums2에서 남은 element들을 모두 왼쪽에 추가
        while n > 0:
            nums1[last] = nums2[n]
            n , last = n - 1, last - 1