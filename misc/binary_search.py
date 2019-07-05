#lst = [12, 23, 45, 56, 1, 34, 22, 10, 8]
#n = 12

def main():
    length = int(input("Enter the length of the list: "))
    print("Enter the items:")
    lst = [int(input()) for i in range(length)]
    n = int(input("Enter the key to search: "))
    return search(lst,n)

def search(lst, n):
    ls = lst.sort()
    print(f"Sorted List: {lst}")
    lower = 0
    upper = len(lst) - 1
    
    while lower <= upper:
        mid = (lower + upper) // 2
        if lst[mid] == n:
            print(f"Found:{n} at position: {mid + 1}")
            return 0
        elif lst[mid] < n:
            lower = mid + 1
        else:
            upper = mid - 1
    print("Not Found")

if __name__ == '__main__':
    main()