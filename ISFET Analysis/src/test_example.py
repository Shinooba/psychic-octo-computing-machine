
from ISFET_Analysis import ISFETSweepReader
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

#set directories
sweep_directory = '../data/sweep_iridiumO_240519/'
sweep_files = os.listdir(sweep_directory)

#get plot
sns.set()
fig, axes = plt.subplots()

# Lists
pH_num_list = []
int_list = []
new_handles = []
new_labels = []

#Read data from file and add to axes
for file in sweep_files:
    isr = ISFETSweepReader(sweep_directory, file)
    sweep_data = isr.get_data()
    pH_label = file.split('_')[5][:-4]
    pH_number = pH_label[2:]
    float(pH_number)
    filtered_data = isr.filter_data()
    axes.plot('V_Ref Ave. (V)', 'V_out Ave. (V)', data=filtered_data, label=pH_label)

#get legend labels
for num, file in enumerate(sweep_files):
    pH_label = file.split('_')[5][:-4]
    pH_number = pH_label[2:]
    pH_num_list.append(float(pH_number))
    int_list.append(num)

#sort in terms of pH
pH_array = np.array([pH_num_list])
pH_sort = np.argsort(pH_array)

#Get current legend titles
handles, labels = axes.get_legend_handles_labels()

#rearrange legend titles in terms of pH
for num, index in enumerate(pH_num_list):
    new_handles.append(0)
    new_labels.append(0)
    new_index = pH_sort[0,num]
    new_handles[num] = handles[new_index]
    new_labels[num] = labels[new_index]

# Set up plot with rearranged legend and axis
axes.legend(new_handles, new_labels)
axes.set_xlabel('Vref (V)')
axes.set_ylabel('Vout (V)')

# display plot
plt.show()
