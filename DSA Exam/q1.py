def count_occurrences(arr, target):
    count = 0
    for i in arr:
        if i == target:
            count += 1
    return count

def main():
    arr = []
    for num in input("Enter numbers: ").split():
        arr.append(int(num))

    target = int(input("what is your target number? "))

    occurrence = count_occurrences(arr, target)

    if occurrence > 0:
        print("number of occurrence = ", occurrence)
    else:
        print(target, " is not present")

main()
