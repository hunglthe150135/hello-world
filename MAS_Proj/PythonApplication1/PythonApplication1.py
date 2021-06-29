import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import numpy as np
import seaborn as sns


data = pd.read_csv('/content/sample_data/SYB63_327_202009_International Migrants and Refugees.csv')
data.drop(columns=['Unnamed: 1'])
data.describe()

pp = sns.pairplot(data, size=1.8, aspect=1.8,
                  plot_kws=dict(edgecolor="k", linewidth=0.5),
                  diag_kind="kde", diag_kws=dict(shade=True))

fig = pp.fig 
fig.subplots_adjust(top=0.93, wspace=0.3)
t = fig.suptitle('Attributes Pairwise Plots', fontsize=14)
plt.savefig('graph.png')
