import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def func( x ):
    return 2*x - math.log10(x) - 7

def secant(func, a, b, n):
    x = ((a*func(b)) - (b*func(a)))/(func(b) - func(a))
    data_frame['n'].append(n)
    data_frame['a'].append(a)
    data_frame['b'].append(b)
    data_frame['x'].append(x)
    data_frame['f(a)'].append(func(a))
    data_frame['f(b)'].append(func(b))
    data_frame['f(x)'].append(func(x))
    b = str(b)
    x = str(x)
    b_begin = b.index('.')+1
    b_end = decimal+b.index('.')+1
    x_begin = x.index('.')+1
    x_end = decimal+b.index('.')+1
    if b[b_begin:b_end] != x[x_begin:x_end]:
        a = b
        b = x
        secant(func, float(a) ,float(b), n+1)
    else:
        global root
        root = float(x[0:decimal+b.index('.')+1])
    
a = 2
b = 3
decimal = int(input('Required decimal places: '))

data_frame = ({'n': [], 'a': [], 'b': [], 'x': [], 'f(a)': [], 'f(b)': [], 'f(x)': []})

secant(func, float(a), float(b), 1)

print('Required root: ', root)

df = pd.DataFrame(data_frame)

x_range = np.linspace(min(df['x']) - 1, max(df['x']) + 1, 400)
y_values = [func(x) for x in x_range]

# Plot the function and secant lines
plt.figure(figsize=(10, 6))
plt.plot(x_range, y_values, label="f(x)")
plt.scatter(root, 0, color='red', label='Secant Point', zorder=5)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.axvline(root, color='green', linestyle='--', label='Approximate Root', zorder=5)

plt.title("Secant Method Root Approximation")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()