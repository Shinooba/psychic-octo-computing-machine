import numpy as np
import pandas as pd



class ISFETSweepReader:
    def __init__(self, directory, filename):
        self.directory = directory
        self.filename = filename

    def read_data(self):
        self.data = pd.read_csv(self.directory + self.filename,
                                usecols=["V_out Ave. (V)", "V_Ref Ave. (V)"])
        vout = self.data['V_out Ave. (V)']
        vref = self.data['V_Ref Ave. (V)']
        sweep_data = (vout, vref)

        return sweep_data

    def get_data(self):
        self.data = pd.read_csv(self.directory + self.filename,
                                usecols=["V_out Ave. (V)", "V_Ref Ave. (V)"])
        return self.data

    def filter_data(self):
      #  print(self.data)
        filtered_data = self.data.rolling(window=500).mean()
      #OLD METHOD FOR CUTTING DATA BETWEEN VALUES
       # filtered_data = filtered_data[(filtered_data[['V_out Ave. (V)']] >= 1.6).all(axis=1)]
       # filtered_data = filtered_data[(filtered_data[['V_out Ave. (V)']] <= 1.9).all(axis=1)]
       # print(filtered_data)
       # for index in filtered_data
            #find difference between rows
        return filtered_data

    def print_sweep(self):
        print(self.data)



