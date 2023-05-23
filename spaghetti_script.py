import pandas as pd


data = pd.read_csv('data/aggroTV.csv')

data = data [['Aggresivität', 'Zeitdauer']]

...

data.plot.scatter(x='Aggresivität', y='Zeitdauer', z='red')
plt.show()

pass 