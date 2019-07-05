# spilt the unsorted list
# compare each of the elements and group them 
# repeat step 2 until whole list is merged and sorted

list1 = [1, 45, 6, 90, 8, 24]

def main():
    length = int(input("Enter the length of the list: "))
    print("Enter the items:")
    list1 = [int(input()) for i in range(length)]
    print("Sorted List:", merge_sort(list1))

def merge_sort(list1):
    if len(list1) > 1: # base case
        mid = len(list1) // 2
        right = list1[mid:]
        left = list1[:mid]
        merge_sort(left)
        merge_sort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list1[k] = left[i]
                i += 1
                k += 1
            else:
                list1[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            list1[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list1[k] = right[j]
            j += 1
            k += 1
    return list1

if __name__ == '__main__':
    main()
