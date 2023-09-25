import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def func( x ):
    return math.pow(x, 3) - 4*x - 9

def false(a, b, n):
    global root
    x = ((a*func(b)) - (b*func(a)))/(func(b) - func(a))
    
    data_frame['n'].append(n)
    data_frame['a'].append(a)
    data_frame['b'].append(b)
    data_frame['x'].append(x)
    data_frame['f(a)'].append(func(a))
    data_frame['f(b)'].append(func(b))
    data_frame['f(x)'].append(func(x))
    
    a = str(a)
    b = str(b)
    x = str(x)
    
    b_begin = b.index('.')+1
    b_end = decimal+b.index('.')+1
    
    a_begin = a.index('.')+1
    a_end = decimal+a.index('.')+1
    
    x_begin = x.index('.')+1
    x_end = decimal+b.index('.')+1
    
    if func(float(x)) > 0:
        if b[b_begin:b_end] != x[x_begin:x_end]:
            b = x
            false(float(a) ,float(b), n+1)
        else:
            root = float(x[0:decimal+b.index('.')+1])
    else:
        if a[a_begin:a_end] != x[x_begin:x_end]:
            a = x
            false(float(a) ,float(b), n+1)
        else:
            root = float(x[0:decimal+a.index('.')+1])
    
def graph():
    x_range = np.linspace(min(df['x']) - 1, max(df['x']) + 1, 400)
    y_values = [func(x) for x in x_range]

    # Plot the function and secant lines
    plt.figure(figsize=(10, 6))
    plt.plot(x_range, y_values, label="f(x)")
    plt.scatter(root, 0, color='red', label='False Position Point', zorder=5)

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.axvline(root, color='green', linestyle='--', label='Root', zorder=5)

    plt.title("False Position Method Root Approximation")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()
    
a = 2
b = 3
decimal = int(input('Required decimal places: '))

data_frame = ({'n': [], 'a': [], 'b': [], 'x': [], 'f(a)': [], 'f(b)': [], 'f(x)': []})

false(float(a), float(b), 1)

print('Required root: ', root)

df = pd.DataFrame(data_frame)

graph()