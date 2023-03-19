def build_heap(arr):
    swaps = []
    size = len(arr)
    for i in range(size // 2, -1, -1):
        j = i
        while True:
            k = j * 2 + 1
            if k >= size:
                break
            if k + 1 < size and arr[k + 1] < arr[k]:
                k = k + 1
            if arr[j] <= arr[k]:
                break
            swaps.append((j,k))
            arr[j], arr[k] = arr[k], arr[j]
            j = k

    return swaps


def main():
    choice = input()
    if "I" in choice:
        n = int(input())
        arr = list(map(int, input().split()))
    elif "F" in choice:
        file = input()
        with open("tests/"+file,'r') as f:
                m = int(f.readline())
                arr = list(map(int, f.readline().split()))
    swaps = build_heap(arr)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
