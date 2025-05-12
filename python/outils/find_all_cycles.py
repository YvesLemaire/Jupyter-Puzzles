# Algorithme de Tarjan
# implementation inspiree de https://github.com/josch/cycles_tarjan


import sys

def find_cycles(directed, max_loop, A): # A dictionaire de listes (liste d'adjacence)

    point_stack = list()
    marked = dict()
    marked_stack = list()
    cycles = list()
    Continue = True

    def backtrack(v):
    
        nonlocal Continue
        
        if Continue:
            f = False
            point_stack.append(v)
            marked[v] = True
            marked_stack.append(v)
            for w in A[v]:
                if w<s:
                    A[w] = []
                elif w==s:
                    if directed or (len(point_stack) > 2 and (point_stack[0],*reversed(point_stack[1:])) not in cycles):
                        cycles.append(tuple(point_stack))
                        if len(cycles) == max_loop:
                            Continue = False
                    f = True
                elif not marked[w]:
                    f = backtrack(w) or f
            if f:
                while marked_stack[-1] != v:
                    u = marked_stack.pop()
                    marked[u] = False
                marked_stack.pop()
                marked[v] = False
            point_stack.pop()
            return f

    for i in A:
        marked[i] = False
    
    for s in A:
        if Continue:
            backtrack(s)
            while marked_stack:
                u = marked_stack.pop()
                marked[u] = False
    
    return cycles


if __name__ == "__main__":
  
    G = [[1, 2], [2, 3], [3, 5], [3, 4], [4, 7], [7, 8], [4, 6], [6, 5], [5, 9], [9, 10], [10, 6], [10, 11], [11, 12], [12, 13], [11, 13]]
    A = {i : [] for i in range(1, 14)}
    for i, j in G:
        A[i].append(j)
        A[j].append(i)
    
    print(find_cycles(False, A))

