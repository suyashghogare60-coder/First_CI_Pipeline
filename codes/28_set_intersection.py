def set_intersection(first, second):
    return first.intersection(second)


if __name__ == "__main__":
    first = set(map(int, input("Enter first set elements: ").split()))
    second = set(map(int, input("Enter second set elements: ").split()))

    print("Intersection:", set_intersection(first, second))