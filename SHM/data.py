import numpy as np
import pandas as pd
import time

i = 0;
sg = pd.DataFrame(columns = ['time stamp', 'e1', 'e2', 'e3'])
while i<10:
    sg = sg.append({'time stamp': pd.Timestamp.now(), 'e1': np.random.rand()*100,'e2': np.random.rand()*100, 'e3': np.random.rand()*100}, ignore_index=True)
    i = i + 1
    time.sleep(1)
    print('record #', i)
    #print(sg.iloc[-1:])

sg.to_csv('/home/dnaneet/ComputationalMechanicsPlayGround/SHM/data.csv', mode='a', header=False)


