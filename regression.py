import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from scipy import stats

nyc = pd.read_csv('https://raw.githubusercontent.com/pdeitel/IntroToPython/master/examples/ch10/ave_hi_nyc_jan_1895-2018.csv')

nyc.Date = nyc.Date.floordiv(100)
nyc.columns = ['Date','Temperature','Anomaly']

linear_regression = stats.linregress(x=nyc.Date, y=nyc.Temperature)
axes = sns.regplot(x= nyc.Date, y =nyc.Temperature)

axes.set_ylim(5,80)
plt.title('Simple regression using Scipy')

plt.show()
