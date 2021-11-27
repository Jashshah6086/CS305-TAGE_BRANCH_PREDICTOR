import matplotlib.pyplot as plt
from numpy.core.fromnumeric import mean


modes = ['bimodal', 'hashed_perceptron', 'tage-l']
trace_ids = range(1, 6)

dct = dict()

for mode in modes:
    dct[mode] = []
    for i in trace_ids:
        f = open(f'{mode}/server_00{i}.champsimtrace.xz-{mode}-no-no-no-no-lru-1core.txt')
        for line in f.readlines():
            if 'Branch Prediction Accuracy' in line:
                acc = float(line.split()[5][:-1])
                dct[mode].append(acc)
                
                
colors = dict(zip(modes, ['red', 'black', 'blue', 'green']))

plt.xlabel('Server trace ID')
plt.ylabel('Branch Prediction Accuracy (%)')
plt.xticks(range(1, 6), [1, 2, 3, 4, 9])
for mode in reversed(modes):
    plt.plot(trace_ids, dct[mode], label=mode, marker='o', color=colors[mode])

for mode in reversed(modes):
    m = mean(dct[mode])
    plt.axhline(y = m, linestyle='dashed', color=colors[mode])
    plt.text(4.57, m + 0.1, '%.5f' % m, color=colors[mode])


plt.legend()
plt.savefig('result.png')
plt.show()