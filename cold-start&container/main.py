import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scienceplots

df = pd.read_excel("data_test.xlsx", header=0)

# print(df.values)
#
# print("\n(2)第2行第3列的值：")
# print(df.values[0, 0])
# print(df.values[0, 1])
# print(df.values[0, 2])
# print(df.values[0, 3])

x_index = []
cold_start_index = []
idle_index = []
low_usage_index = []

print(df.shape)

for i in range(121):
    x_index.append(float(df.values[i, 0]))
    cold_start_index.append(int(df.values[i, 1]))
    idle_index.append(int(df.values[i, 2]))
    low_usage_index.append(int(df.values[i, 3]))


def model(p):
    if p == 'cold start':
        return cold_start_index
    if p == 'idle container':
        return idle_index
    else:
        return low_usage_index


pparam = dict(xlabel='Timeline', ylabel=r'Count (300 Functions)')
#
#
label = ['cold start', 'idle container', 'low usage container']
#
with plt.style.context(['science']):
    fig, ax = plt.subplots()
    for p in label:
        ax.plot(x_index, model(p), label=p)
    ax.legend(prop = {'size':8})
    ax.autoscale(tight=True)
    ax.set(ylim=[0, 205])
    ax.set(**pparam)
    fig.show()
    fig.savefig('figures/fig1.pdf')
    fig.savefig('figures/fig1.jpg', dpi=500)
