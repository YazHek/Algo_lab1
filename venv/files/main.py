from models.puzzle import Puzzle
import time


def merge(A, B):
    global merge_swap_count
    global merge_compare_count
    i1 = i2 = 0
    out = []
    while i1 < len(A) and i2 < len(B):
        merge_compare_count += 1
        if A[i1].warranty >= B[i2].warranty:
            out.append(A[i1])
            i1 += 1
            merge_swap_count += 1
        else:
            out.append(B[i2])
            i2 += 1
            merge_swap_count += 1
    out += A[i1:] + B[i2:]
    merge_swap_count += len(A) - i1 + len(B) - i2
    return out


def merge_sort(A):
    if len(A) <= 1:
        return A
    mid = int(len(A) / 2)
    return merge(merge_sort(A[:mid]), merge_sort(A[mid:]))


def selection_sort(A):
    global selection_swap_count
    global selection_compare_count
    for i in range(len(A)):
        min_i = i
        for j in range(i + 1, len(A)):
            selection_compare_count += 1
            if A[j].howmuch_elements >= A[min_i].howmuch_elements:
                min_i = j
        A[i], A[min_i] = A[min_i], A[i]
        selection_swap_count += 1


arr = []

with open('input.txt', 'r') as input:
    fields = input.read().split(',')
    i = 0
    howmuch_elements = 0
    warranty = ""
    material = ""
    type_level = ""
    for field in fields:
        i += 1
        if (i % 4 == 1):
            howmuch_elements = int(field)
        if (i % 4 == 2):
            warranty = str(field)
        if (i % 4 == 3):
            material = str(field)
        if (i % 4 == 4):
            type_level = str(field)
        if (i % 4 == 0):
            arr.append(Puzzle(howmuch_elements, warranty, material, field))

selection_begin = time.time()
selection_compare_count = 0
selection_swap_count = 0
selection_sort(arr)
selection_finish = time.time()

with open('output.txt', 'a+') as output:
    output.write('SELECTION SORT\n')
    output.write('Time: ' + str(selection_finish - selection_begin) + '\n')
    output.write('Compares: ' + str(selection_compare_count) + '\n')
    output.write('Swaps: ' + str(selection_swap_count) + '\n')
    output.write('Elements:\n')
    for a in arr:
        output.write(str(a))
        if a.material.find('\n') == -1:
            output.write('\n')

merge_begin = time.time()
merge_compare_count = 0
merge_swap_count = 0
arr = merge_sort(arr)
merge_finish = time.time()

with open('output.txt', 'a+') as output:
    output.write('MERGE SORT\n')
    output.write('Time: ' + str(merge_finish - merge_begin) + '\n')
    output.write('Compares: ' + str(merge_compare_count) + '\n')
    output.write('Swaps: ' + str(merge_swap_count) + '\n')
    output.write('Elements:\n')
    for a in arr:
        output.write(str(a))
        if a.warranty.find('\n') == -1:
            output.write('\n')
