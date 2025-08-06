nums1 = [0]
m = 0
nums2 = [1]
n = 1



def merge(nums1:list[int], m:int, nums2:list[int], n:int):

    p = m + n -1 # pointer that points at the last element where we will insert i.e [1,2,3,0,0,0] p point at index 5
    p1 = m-1 # pointer that points at the last element of the nums1 i.e [1,2,3,0,0,0] p1 point at index 2
    p2 = n-1 # pointer that points at the last element of the nums2 i.e [2,5,6] p2 point at index 2

    
    while p1 >= 0 and p2 >= 0:

        if nums1[p1] > nums2[p2]: 
            nums1[p] = nums1[p1]
            p1 -= 1#move p1 to left if p1 is placed at nums1[p] position
        else:
            nums1[p] = nums2[p2]
            p2 -= 1 #move p2 to left if p2 is placed at nums1[p] position

        p -= 1 #after place at p position move p to left

    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

merge(nums1,m,nums2,n)
print(nums1)