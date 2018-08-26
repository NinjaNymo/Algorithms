
def insertionSort(instance):
    for j in range(1, len(instance)):
        key  = instance[j]
        i = j - 1
        while i >= 0 and instance [i] > key:
            instance[i + 1] = instance[i]
            i = i - 1
        instance[i + 1] = key
    return instance

print(insertionSort([3,2,1]))