#Internet source / insperation: https://www.programiz.com/dsa/insertion-sort

#To sort a[left...right] into ascending order:
#1. For r = left+1, ..., right, repeat:
#1.1. Let val = a[r].
#1.2. Insert val into its correct sorted position in a[left...r].
#2. Terminate.

# Test Vars: a = [4,3,4,5,2,3,4,6,8,9,10]  # O(1)

# Test Vars: 
a = ["fox", "cow", "pig", "cat", "rat", "lion", "tiger", "goat", "dog"]  # O(1)
# Test Vars: a = [23, 56, 7, 44, 768, 90, 107, 22, 45, 66, 99, 1, 12]  # O(1)

arr = a[:]  # O(1)

for l in range(0, len(arr) - 1):  # O(n)
    p = l  # O(n)
    for i in range(l+1, len(arr)):  # O(n^2)
        if arr[i] < arr[p]:  # O(1)
            p = i  # O(1)

    if p != l:  # O(1)
        temp = arr[p]  # O(1)
        for j in range(p, l, -1):  # O(n^3)
            arr[j] = arr[j-1]  # O(1)
        arr[l] = temp  # O(1)

print(arr)  # O(1)