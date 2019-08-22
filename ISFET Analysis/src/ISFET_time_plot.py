from tkinter import Tk
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector
import seaborn as sns
import pandas as pd
import os
import numpy as np

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
plot_filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

#get plot
sns.set()
fig, axes = plt.subplots()

#get data
data = pd.read_csv(plot_filename)
print(data)
data.rename(columns={'Unnamed: 0':'Time'}, inplace=True)
print(data.iloc[:,0])



axes.plot('Time','V_out Ave. (V)', data=data)

# display plot
plt.show()





