import math
import time
from KnapsackDP import knapsack_DP

c = 0
def knapSack(mW,w,v,n):
    # counter how many time recursive function is called.
    global c
    c += 1
    
    if(mW == 0 or n == 0):
        return [0,[]]
        
    if(w[n-1] > mW):
        return knapSack(mW,w,v,n-1)
        
    set1 = knapSack(mW-w[n-1],w,v,n-1)
    set2 = knapSack(mW,w,v,n-1)
    
    if(set1[0]+v[n-1] > set2[0]):
        set1[1].append(n-1)
        set1[0] += v[n-1]
        return set1
    else:
        return set2

for i in range(5):
    val = [160, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    
    t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
    
    print("Here is the time for Backtracking programming:")

    start = time.perf_counter()
    knapSack(W,wt,val,n)
    end = time.perf_counter()

    print("Knapsack Max & list:",knapSack(W, wt, val, n))
    print("Total Recursive Steps:" ,c)
    print("Time consumed for Knapsack of Backtracking Algorithim: ",end - start)
    
    print("Here is the time for Dynamic programming:")

    start = time.perf_counter()
    knapsack_DP(wt, val, W, n)
    end = time.perf_counter()
    
    print("Knapsack of Dynamic programming:", knapsack_DP(wt, val, W, n))
    print("Time consumed for Knapsack of Dynamic Algorithim: ",end - start)
