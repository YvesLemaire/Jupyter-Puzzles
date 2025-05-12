# Algorithme de Tarjan
# implementation inspiree de https://github.com/josch/cycles_tarjan


import sys

def find_cycles(A): # A dictionaire de listes (liste d'adjacence)

    point_stack = list()
    marked = dict()
    marked_stack = list()

    def backtrack(v):
        f = False
        point_stack.append(v)
        marked[v] = True
        marked_stack.append(v)
        for w in A[v]:
            if w<s:
                A[w] = []
            elif w==s:
                yield tuple(point_stack)
                f = True
            elif not marked[w]:
                it = backtrack(w)
                for x in it:
                    yield x
                f = it or f
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
        for cycle in backtrack(s):
            yield cycle
        while marked_stack:
            u = marked_stack.pop()
            marked[u] = False
