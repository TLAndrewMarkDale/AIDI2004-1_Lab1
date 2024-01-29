def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
if __name__ == "__main__":
    print("Enter integers you want sorted. Enter 'done' when you are finished.")
    arr = []
    while True:
        entry = input('Enter a number: ')
        if entry.lower() == 'done':
            break
        elif not entry.isnumeric():
            print('Please ensure you are entering an integer value.')
        else:
            arr.append(int(entry))
    print("Given list:", arr)
    print("Sorted list:", bubble_sort(arr))

