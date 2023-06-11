"""
Implement Greedy search algorithm for any of the following application:
I. Selection Sort
II. Minimum Spanning Tree
III. Single-Source Shortest Path Problem
IV. Job Scheduling Problem
V. Prim's Minimal Spanning Tree Algorithm
VI. Kruskal's Minimal Spanning Tree Algorithm
VII. Dijkstra's Minimal Spanning Tree Algorithm
"""
# Selection Sort

def Selection_sort(arr):
  n = len(arr)
  for i in range(n):
    min = i
    for j in range(i+1, n):
      if(arr[j] < arr[min]):
        min = j
    if(min != i):
      arr[min],arr[i] = arr[i],arr[min]
    print(arr)

arr = list(map(int, input("Enter Array Elements: ").split()))
n = len(arr)

print("Array bfore sort: ")
print(arr)
print("\nDuring Passes: ")
Selection_sort(arr)

print("\nArray after sort: ")
print(arr)
