import pandas as pd
from time import time

time = time()

df = pd.DataFrame({'Country':['India','USA','China'],
'Population':['10000','20000','30000'],
'Time':time})

df.to_csv('pop.csv')