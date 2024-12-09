import random


array1 = random.sample(range(100), 10)
print("zaklad:", array1)


def bubble_sort(array1):
    n = len(array1)
    for i in range(n):
        for j in range(0, n-i-1):
            if array1[j] > array1[j+1]:
                array1[j], array1[j+1] = array1[j+1], array1[j]


def selection_sort(array1):
    n = len(array1)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array1[j] < array1[min_index]:
                min_index = j
        array1[i], array1[min_index] = array1[min_index], array1[i]


def insertion_sort(array1):
    n = len(array1)
    for i in range(1, n):
        key = array1[i]
        j = i - 1
        while j >= 0 and key < array1[j]:
            array1[j + 1] = array1[j]
            j -= 1
        array1[j + 1] = key


def is_sorted(array1):
    return all(array1[i] <= array1[i + 1] for i in range(len(array1) - 1))

def bogo_sort(array1):
    while not is_sorted(array1):
        random.shuffle(array1)  


bubble_sorted_array1 = array1.copy() 
bubble_sort  (bubble_sorted_array1)
print ("serazeni  bubble sort:", bubble_sorted_array1)


selection_sorted_array1 = array1.copy()  
selection_sort(selection_sorted_array1)
print("Serazeni  selection sort:", selection_sorted_array1)

selection_sorted_array1 = array1.copy() 
selection_sort (selection_sorted_array1)
print ("Serazeni  selection sort:", selection_sorted_array1)


bogo_sorted_array1 = array1.copy()  
bogo_sort (bogo_sorted_array1)
print ("serazeni  bogo sort:", bogo_sorted_array1)