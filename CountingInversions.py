import pandas as pd

# Define the path to your file
path = r"C:\Users\ahmed\Downloads\_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt"

# Function to perform merge sort and count inversions
def mergesort(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        n = len(arr)
        left, l = mergesort(arr[:n//2])
        right, r = mergesort(arr[n//2:])
        i = j = 0
        sorte = []
        inversions = 0
        
        # Merge the two halves while counting inversions
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorte.append(left[i])
                i += 1
            else:
                sorte.append(right[j])
                j += 1
                inversions += len(left) - i  # Count the remaining elements in left
        
        # Append remaining elements
        while i < len(left):
            sorte.append(left[i])
            i += 1
            
        while j < len(right):
            sorte.append(right[j])
            j += 1
            
        return sorte, inversions + l + r

# Read the data from the file
data = []
with open(path, 'r') as f:
    for line in f.readlines():
        data.append(int(line.strip()))

# Print the data (for debugging purposes)
print(data)

# Perform merge sort and count inversions
sorted_array, total_inversions = mergesort(data)

# Print the sorted array and the number of inversions
print("Sorted Array:", sorted_array)
print("Total Inversions:", total_inversions)
#Counting Inversions: When an element from the right half is appended before an element from the left half, it indicates inversions for all the remaining elements in the left half.