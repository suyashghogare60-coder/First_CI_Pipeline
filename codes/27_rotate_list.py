def rotate_list(items, k):
    if len(items) == 0:
        return []

    k = k % len(items)

    if k == 0:
        return items.copy()

    return items[-k:] + items[:-k]


if __name__ == "__main__":
    items = list(map(int, input("Enter numbers separated by spaces: ").split()))
    k = int(input("Enter k: "))

    print("Rotated list:", rotate_list(items, k))