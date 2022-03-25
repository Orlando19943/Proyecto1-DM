import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as sp

deaths = pd.read_csv('final.csv')
Desechos = ['Ignorado', 9, 999, 9999, '9', '99', '999', '9999']
deaths = deaths.drop(['ID', 'Areag', 'Mupocu', 'Mupreg', 'Mnadif', 'Pnadif', 'caudef.descrip', 'Dnadif', 'Nacdif'], axis = 1)
variables = deaths.columns.values

print(variables)


print(deaths.shape)

for i in Desechos:
	for a in variables:
		deaths = deaths[deaths[a] != i]

print(deaths.shape)

for i in variables:
	try:
		print(i)
		deaths[i] = pd.to_numeric(deaths[i])
	except:
		print('nsdkfnd')