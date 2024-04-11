import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import StrMethodFormatter

costs = []
accuracies = []

# ================= All Models =======================
model = 'FP All Models'
# ================= ResNet-18 Pareto =======================

# E2M1
cost = "7.78	16.80	29.23	45.08	64.35	113.1"
costs.append(cost)

accuracy = "58.17	64.18	67.96	70.43	72.08	74.22"
accuracies.append(accuracy)

# E4M3
cost = "31.13	67.19	116.90	180.3	257.4	452.5"
costs.append(cost)

accuracy = "62.06	67.57	70.56	72.66	73.75	75.43"
accuracies.append(accuracy)

# FLIQS-S
cost = "8.18	17.68	30.8	54.6	76.35	128.20"
costs.append(cost)

accuracy = "59.8	65.77	68.89	72.1	73.5	75.26"
accuracies.append(accuracy)

# FLIQS-L
cost = "9.6	19.48	32.78	50.01	68.43	118.2"
costs.append(cost)

accuracy = "60.99	66.61	70.01	71.92	73.32	74.8"
accuracies.append(accuracy)

# Float (BF16)
cost = "124.5	268.80	467.7	721.3	1030	1810"
costs.append(cost)

accuracy = "62.63	68.34	71.17	72.89	74.31	75.56"
accuracies.append(accuracy)

# ================= ResNet-50 Pareto =======================

# E2M1
cost = "16.84	37.16	65.43	101.6	145.8	257.9"
costs.append(cost)

accuracy = "70.24	73.91	75.77	76.89	77.4	78.01"
accuracies.append(accuracy)

# E4M3
cost = "67.35	148.70	261.70	406.5	583.1	1031"
costs.append(cost)

accuracy = "73.09	75.86	77.42	78.13	78.42	78.97"
accuracies.append(accuracy)

# FLIQS-S
cost = "21.72	42.87	74.28	112.7	160	279.20"
costs.append(cost)

accuracy = "72.16	75.14	76.84	77.83	78.22	78.94"
accuracies.append(accuracy)

# FLIQS-L
cost = "21.93	44.7	76.43	115.6	165.6	297.9"
costs.append(cost)

accuracy = "72.39	75.61	76.95	78	78.24	78.81"
accuracies.append(accuracy)

# Float (BF16)
cost = "269.4	594.60	1047	1626	2332	4126"
costs.append(cost)

accuracy = "73.87	76.22	77.68	78.45	78.82	79.14"
accuracies.append(accuracy)

# ================= EfficientNet Pareto =======================

# E2M1
cost = "6.16	10.97	15.88	29.21	70.25"
costs.append(cost)

accuracy = "62.45	67.49	69.14	71.22	76.12"
accuracies.append(accuracy)

# E4M3
cost = "24.65	43.89	63.50	116.8	281"
costs.append(cost)

accuracy = "72.99	75.36	76.20	78.17	79.52"
accuracies.append(accuracy)

# FLIQS-S
cost = "7.77	13.58	23.26	55.15	203.3"
costs.append(cost)

accuracy = "67.6	71.63	74.67	78.05	80.3"
accuracies.append(accuracy)

# FLIQS-L
cost = "7.3	13.00	19.61"
costs.append(cost)

accuracy = "71.13	74.34	75.58"
accuracies.append(accuracy)

# Float (BF16)
cost = "98.61	175.50	254"
costs.append(cost)

accuracy = "73.53	75.50	76.36"
accuracies.append(accuracy)

# ================= MobileNetV2 Pareto =======================

# E2M1
cost = "1.55	4.81	9.31	18.2"
costs.append(cost)

accuracy = "52.32	66.29	69.26	73.81"
accuracies.append(accuracy)


# E4M3
cost = "2.38	6.21	19.25	37.2"
costs.append(cost)

accuracy = "53.98	64.85	72.63	75.86"
accuracies.append(accuracy)

# FLIQS-S
cost = "1.22	2.69	7.35	12.6"
costs.append(cost)

accuracy = "50.76	62.58	71.14	74.34"
accuracies.append(accuracy)

# FLIQS-L
cost = "0.95	2.36	6.77	12.37"
costs.append(cost)

accuracy = "51.11	63.65	71.97	75.26"
accuracies.append(accuracy)

# Float (BF16)
cost = "9.52	24.87	77	149"
costs.append(cost)

accuracy = "55.18	65.72	73.13	76"
accuracies.append(accuracy)

# ================= InceptionV3 Pareto =======================

# E2M1
cost = "3.04	12.07	27.08	48.08	108"
costs.append(cost)

accuracy = "54.14	67.8	72.09	74.55	76.35"
accuracies.append(accuracy)

# E4M3
cost = "12.17	48.28	108.3	192.3	432"
costs.append(cost)

accuracy = "62.65	71.5	74.49	75.94	77.39"
accuracies.append(accuracy)

# FLIQS-S
cost = "3.66	13.46	29.16	51.65	111.4"
costs.append(cost)

accuracy = "58.78	69.5	73.43	75.28	77.03"
accuracies.append(accuracy)

# FLIQS-L
cost = "3.89	15.23	32.86	56.15	124.2"
costs.append(cost)

accuracy = "60.9	70.63	74.16	75.94	77.43"
accuracies.append(accuracy)

# Float (BF16)
cost = "48.69	193.1	433.3	769.2	1728"
costs.append(cost)

accuracy = "63.65	72.1	75.24	76.26	77.55"
accuracies.append(accuracy)

# ================= DeiT Pareto =======================

# E2M1
cost = "38.42	67.96	152.1	206.8	269.8"
costs.append(cost)

accuracy = "73.88	76.35	80.1	79.04	79.49"
accuracies.append(accuracy)

# E4M3
cost = "153.5	271.5	608.1	826.6	1079"
costs.append(cost)

accuracy = "76.96	78.85	79.13	79.9	79.17"
accuracies.append(accuracy)

# FLIQS-S
cost = "38.42	70.74	156.3	211.7	275.4"
costs.append(cost)

accuracy = "73.95	77.52	79.24	79.56	79.27"
accuracies.append(accuracy)

# FLIQS-L
cost = "39.4	68.49	152.9	207.7	270.8"
costs.append(cost)

accuracy = "74.36	77.35	78.89	79.56	79.54"
accuracies.append(accuracy)

labels = ['R18 E2M1', 'R18 E4M3', 'R18 FLIQS-S', 'R18 FLIQS-L', 'R18 BF16',
          'R50 E2M1', 'R50 E4M3', 'R50 FLIQS-S', 'R50 FLIQS-L', 'R50 BF16',
          'EFF E2M1', 'EFF E4M3', 'EFF FLIQS-S', 'EFF FLIQS-L', 'EFF BF16',
          'MB E2M1', 'MB E4M3', 'MB FLIQS-S', 'MB FLIQS-L', 'MB BF16',
          'INC E2M1', 'INC E4M3', 'INC FLIQS-S', 'INC FLIQS-L', 'INC BF16',
          'DT E2M1', 'DT E4M3', 'DT FLIQS-S', 'DT FLIQS-L'
          ]
marker = ['o', 'o', 'o', 'o', 'o',
          'x', 'x', 'x', 'x', 'x',
          '*', '*', '*', '*', '*',
          'P', 'P', 'P', 'P', 'P',
          'd', 'd', 'd', 'd', 'd',
          '^', '^', '^', '^'
          ]
markerColor = ['steelblue', 'orange', 'green', 'red', 'black',
               'steelblue', 'orange', 'green', 'red', 'black',
               'steelblue', 'orange', 'green', 'red', 'black',
               'steelblue', 'orange', 'green', 'red', 'black',
               'steelblue', 'orange', 'green', 'red', 'black',
               'steelblue', 'orange', 'green', 'red', 'black',
               ]

x_limit = [0, 4000]
y_limit = [60, 80]

# =====================================================
plt.figure(figsize=(4.5, 6.75))
# plt.xlim(x_limit)
plt.ylim(y_limit)
plt.xscale("log")
plt.title("Float Models")
plt.xlabel('GBOPs')
plt.ylabel('Top1 Accuracy')
for i in range(len(labels)):
    cost_arr = np.fromstring(costs[i], dtype=float, sep=' ')
    acc_arr = np.fromstring(accuracies[i], dtype=float, sep=' ')
    plt.plot(cost_arr, acc_arr, label=labels[i], marker=marker[i], color=markerColor[i], markersize=5, linestyle='None')
plt.subplots_adjust(left=.1, bottom=.1, right=.9, top=.9, wspace=None, hspace=None)
plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.1f}'))
plt.grid()
plt.savefig('fp_models', dpi=300)
plt.show()
