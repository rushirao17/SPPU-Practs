#With Selection Sort
def selection_sort_greedy(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [64, 25, 12, 22, 11]
print("Sorted array is:", selection_sort_greedy(arr))





#With Dijkstra's Minimal Spanning Tree Algorithm
from typing import List, Tuple
import heapq

def dijkstra(n: int, edges: List[Tuple[int, int, int]], start: int) -> List[int]:
    distances = [float('inf') for _ in range(n)]
    distances[start] = 0  # distance to start vertex is 0
    heap = [(0, start)]
    while heap:
        dist, u = heapq.heappop(heap)
        if dist > distances[u]:  # if the distance is larger than the recorded distance, skip
            continue
        for v, w in edges[u]:
            if distances[v] > dist + w:  # if the distance to v through u is smaller
                distances[v] = dist + w  # update the distance to v
                heapq.heappush(heap, (distances[v], v))
    return distances





#With Kruskal's Minimal Spanning Tree/Minimum Spanning Tree
from typing import List, Tuple

def kruskal(n: int, edges: List[Tuple[int, int, int]]) -> int:
    edges.sort(key=lambda x: x[2])  # sort the edges by their weights in ascending order
    parent = [i for i in range(n)]  # initially, each vertex is in its own set
    total_weight = 0
    for u, v, w in edges:
        if find(u, parent) != find(v, parent):  # if u and v are in different sets
            total_weight += w  # add the weight of this edge to the total weight
            union(u, v, parent)  # merge the sets containing u and v
    return total_weight

def find(u: int, parent: List[int]) -> int:
    if parent[u] == u:
        return u
    parent[u] = find(parent[u], parent)
    return parent[u]

def union(u: int, v: int, parent: List[int]) -> None:
    root1 = find(u, parent)
    root2 = find(v, parent)
    parent[root1] = root2
