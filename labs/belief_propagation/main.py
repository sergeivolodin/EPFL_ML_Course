import numpy as np
# number of variables in a factor graph
n_vars = 10

# number of factors in a factor graph
n_funcs = 5

# some function examples
f0 = lambda x : x[0]
f1 = lambda x : x[1]
f2 = lambda x : x[2]
f3 = lambda x : x[3]
f4 = lambda x : x[4]

# list of all functions
funcs = [f0, f1, f2, f3, f4]

# list of argument numbers required for each functions
deps = [[0,1], [1], [2], [0,3], [4]]

def get_siblings(node):
    if node[0] == 'f':
        f_n = int(node[1:])
        return ['x' + str(i) for i in deps[f_n]]
    elif node[0] == 'x':
        x_n = int(node[1:])
        return ['f' + str(i) for i, x in enumerate(deps) if x_n in x]

# sanity check
assert(len(deps) == n_funcs)
assert(len(funcs) == n_funcs)

# list of all nodes
nodes = ['f' + str(i) for i in range(n_funcs)] + ['x' + str(i) for i in range(n_vars)]

# sanity check
assert(len(nodes) == n_vars + n_funcs)

# array with all of the messages
messages = [[None] * len(nodes)] * len(nodes)

print(get_siblings('x0'))
