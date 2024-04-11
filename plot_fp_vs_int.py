import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import StrMethodFormatter

costs = []
accuracies = []

# ================= All Models =======================
model = 'FP vs Int All Models'

# ================= ResNet-18 Pareto FP =======================

# FLIQS-L
cost = "9.6	19.48	32.78	50.01	68.43	118.2"
costs.append(cost)

accuracy = "60.99	66.61	70.01	71.92	73.32	74.8"
accuracies.append(accuracy)

# ================= ResNet-18 Pareto INT =======================

# FLIQS-L
cost = "9.3	19.58	33.54	49.57	70.54	120.8"
costs.append(cost)

accuracy = "60.21	66.47	69.83	71.76	73.19	74.91"
accuracies.append(accuracy)

# ================= ResNet-50 Pareto FP =======================

# FLIQS-L
cost = "21.93	44.7	76.43	115.6	165.6	297.9"
costs.append(cost)

accuracy = "72.39	75.61	76.95	78	78.24	78.81"
accuracies.append(accuracy)

# ================= ResNet-50 Pareto INT =======================

# FLIQS-L
cost = "21.03	43.55	74.49	114.8	161.5	282"
costs.append(cost)

accuracy = "72.12	75.01	76.79	77.66	78.17	78.72"
accuracies.append(accuracy)

# ================= EfficientNet Pareto FP =======================

# FLIQS-L
cost = "7.3	13.00	19.61"
costs.append(cost)

accuracy = "71.13	74.34	75.58"
accuracies.append(accuracy)

# ================= EfficientNet Pareto INT =======================

# FLIQS-L
cost = "7.42	13.32	19.85"
costs.append(cost)

accuracy = "70.01	72.96	74.62"
accuracies.append(accuracy)

# ================= MobileNetV2 Pareto FP =======================
# FLIQS-L
cost = "0.95	2.36	6.77	12.37"
costs.append(cost)

accuracy = "51.11	63.65	71.97	75.26"
accuracies.append(accuracy)

# ================= MobileNetV2 Pareto INT =======================

# FLIQS-L
cost = "1.02	2.42	7.21	12.69"
costs.append(cost)

accuracy = "52.11	63.35	71.87	74.83"
accuracies.append(accuracy)

# ================= InceptionV3 Pareto FP =======================
# FLIQS-L
cost = "3.89	15.23	32.86	56.15	124.2"
costs.append(cost)

accuracy = "60.9	70.63	74.16	75.94	77.43"
accuracies.append(accuracy)

# ================= InceptionV3 Pareto INT =======================

# FLIQS-L
cost = "4.31  15.99 33.17 59.16 119.9"
costs.append(cost)

accuracy = "60.72 70.28 73.91 75.67 77.12"
accuracies.append(accuracy)

# ================= DeiT Pareto FP =======================

# FLIQS-L
cost = "39.4	68.49	152.9	207.7	270.8"
costs.append(cost)

accuracy = "74.36	77.35	79.23	79.56	79.54"
accuracies.append(accuracy)

# ================= DeiT Pareto INT =======================

# FLIQS-L
cost = "40.45	70.57	154.5	210.4	273.2"
costs.append(cost)

accuracy = "73.9	76.88	78.89	79.16	79.28"
accuracies.append(accuracy)

labels = ['R18 FP', 'R18 INT',
          'R50 FP', 'R50 INT',
          'EFF FP', 'EFF INT',
          'MB FP', 'MB INT',
          'INC FP', 'INC INT',
          'DT FP', 'DT INT',
          ]
marker = ['o', 'o',
          'x', 'x',
          '*', '*',
          'P', 'P',
          'd', 'd',
          '^', '^'
          ]
markerColor = ['purple', 'green',
               'purple', 'green',
               'purple', 'green',
               'purple', 'green',
               'purple', 'green',
               'purple', 'green']

x_limit = [0, 4000]
y_limit = [60, 80]

# =====================================================
plt.figure(figsize=(3, 4.5))  # Add this line to set figure size
# plt.xlim(x_limit)
plt.ylim(y_limit)
plt.xscale("log")
plt.title("Integer vs. Float")
plt.xlabel('GBOPs')
plt.ylabel('Top1 Accuracy')

# Plot INT data first
for i in range(1, len(labels), 2):
    cost_arr = np.fromstring(costs[i], dtype=float, sep=' ')
    acc_arr = np.fromstring(accuracies[i], dtype=float, sep=' ')
    plt.plot(cost_arr, acc_arr, label=labels[i], marker=marker[i], color=markerColor[i], markersize=5, linestyle='None')

# Plot FP data second, so it's on top
for i in range(0, len(labels), 2):
    cost_arr = np.fromstring(costs[i], dtype=float, sep=' ')
    acc_arr = np.fromstring(accuracies[i], dtype=float, sep=' ')
    plt.plot(cost_arr, acc_arr, label=labels[i], marker=marker[i], color=markerColor[i], markersize=5, linestyle='None')
# plt.legend(loc='lower right', fontsize='small', ncol=1)
plt.subplots_adjust(left=.1, bottom=.1, right=.9, top=.9, wspace=None, hspace=None)
plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.1f}'))  # 2 decimal places
plt.grid()

plt.savefig('fp_vs_int.png', dpi=300)  # Specify the DPI for high resolution
plt.show()
