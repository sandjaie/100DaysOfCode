# Swap the items by comparing adjacent items

#nums = [9, 7, 2, 4, 8, 1]

def main():
    length = int(input("Enter the length of the list: "))
    print("Enter the items:")
    nums = [int(input()) for i in range(length)]
    return bubble(nums)

def bubble_uno(nums): #not optimised
    for j in range(len(nums) -1):
        for i in range(len(nums) -1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                print(nums)
            else:
                print(nums)
    return 0

def bubble(nums):
    for j in range(len(nums)-1, 0, -1):
        for i in range(j):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                print(nums)
            else:
                print(nums)
    return 0

#bubble(nums)
#bubble_uno(nums)

if __name__ == '__main__':
    main()
