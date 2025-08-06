nums = [4, 1, 2, 5, 3]


def insertionSort(nums):
    for current in range(1, len(nums)):

        curr = nums[current]
        previous = current - 1

        """ old code
        while previous < len(nums) and previous > -1:

            if curr <= nums[previous]:
                nums[previous+1] = nums[previous]
                previous -= 1
            else:
                nums[previous+1] = curr
                break

        -while previous < len(nums) and previous > -1 , from this we remove first check condition as its always true
        then we add another condtion as nums[prev]> curr, this removes the inside if
        -and we get ride of else block and place it outside of it , as once nums[previous]
          condtion is broken the loop ends ,and we assign it ,
        -it also get rid of if previous == -1: block as it will be checked
            and we place nums[previous+1] = curr as , prev will be smaller than curr (while condtion broken)

        """

        # updated code
        while previous >= 0 and nums[previous] > curr:
            nums[previous+1] = nums[previous]
            previous -= 1

        nums[previous+1] = curr


insertionSort(nums)
print(nums)
