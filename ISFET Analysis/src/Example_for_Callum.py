
from src.EIS_Reader import EISPlotter, EISReader
from src.EC_Lab_CVReader import CV_Plotter, CVReader
import os
import matplotlib.pyplot as plt
import numpy as np

#55m Sputtered ITO on Xylene Diluted PDMS 5/2/18 annealed for 3 hours in O2
#Hypespectral measurements from 810nm to 940nm
#Electrochemistry performed used 1mM MB in 100mM PB ph 7.2 and 100umM MB 100mM PB pH 7.2

import scipy.stats as sts


eis_directory = '../Data/EIS'
cv_directory = '../Data/CV'


working_directory = os.getcwd()

fig, eis_mag = plt.subplots()
eis_phase = eis_mag.twinx()
eis_filenames = os.listdir(eis_directory)
eis_reader = EISReader(os.path.join(eis_directory,eis_filenames[0]),set_cycle=2)

eis_mag.loglog(eis_reader.eis.frequency, eis_reader.eis.magnitude)
eis_phase.semilogx(eis_reader.eis.frequency, eis_reader.eis.phase)
eis_mag.set_xlabel('Frequency (Hz)')
eis_mag.set_ylabel('|Z| ($\Omega$)')
eis_phase.set_ylabel('$\\angle$ ($\degree$)')
eis_mag.legend(['Some Legend Name'])


fig, cv_plot = plt.subplots()
cv_files = os.listdir(cv_directory)
for file in cv_files:
    cv_reader = CVReader(os.path.join(cv_directory,file))
    cv_plot.plot(cv_reader.voltage, cv_reader.current)
cv_plot.set_xlabel('Voltage')
cv_plot.set_ylabel('Current')

eis_plotter = EISPlotter(eis_directory, legends=['100 $\mu$M PB', '1mM PB'])
uM_100_cv_plotter = CV_Plotter(cv_directory)



plt.show()