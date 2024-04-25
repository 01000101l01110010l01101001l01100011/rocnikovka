import random
first_numbers = []
for i in range(10):
    first_numbers.append(random.randrange(0, 10))

numbers = []
[numbers.append(x) for x in first_numbers if x not in numbers]

def sort(numbers:list):
    pivot = random.choice(numbers)
    index = 0
    for i, number in enumerate(numbers):
        if number > pivot:
            continue
        elif number < pivot:
            index += 1
            if i == index:
                continue
            elif i > index:
                print("Numbers before:", numbers)
                numbers[i] = numbers[index]
                numbers[index] = number
                print(numbers)
        elif number == pivot:
            index += 1
            if i == index:
                pass
            elif i > index:
                numbers[i] = numbers[index]
                numbers[index] = numbers[i]
            break
    numbers1 = numbers[:pivot]
    numbers2 = numbers[pivot: +1]
    

def main(numbers:list):
    numbers, pivot = sort(numbers)
    numbers1 = numbers[:pivot]
    numbers2 = numbers[pivot: +1]

    print(numbers)
    print(pivot)
    print(numbers1)
    print(numbers2)

def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x < arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x >= arr[0]])

print(numbers)
print(qsort(numbers))