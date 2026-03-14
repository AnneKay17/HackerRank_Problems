def insertionSort1(n, arr):
    # Write your code here
    value = arr[-1]
    for i in range(n-2,-1,-1): #[1,2,4,5,3]
        if arr[i] > value:
            arr[i+1] = arr[i]
            for num in arr:
                print(num, end=" ")
            print()
            if i == 0:
                arr[i] = value
                for num in arr:
                    print(num, end=" ")
        else:
            arr[i+1] = value
            for num in arr:
                print(num, end=" ")
            break
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
