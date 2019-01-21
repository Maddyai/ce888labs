import matplotlib
import matplotlib.pyplot as plt 
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import numpy as np

if __name__ == "__main__":
    df = pd.read_csv('./vehicles.csv')
    df = df.dropna()
    data = df.values.T[1]

    sns_distplot = sns.distplot(df.values.T[0])
    sns_distplot = sns.distplot(df.values.T[1])
    plt.legend(['Old', 'New'], loc='best')
    # sns_distplot.set(xlabel='common xlabel', ylabel='common ylabel')
    fig = sns_distplot.get_figure()
    fig.savefig("distplot_vehicles.pdf")
    fig.savefig("distplot_vehicles.png")

    sns_scatterplot = sns.scatterplot(df.columns[0], df.columns[1],data=df)
    plt.xlim(0, 35)
    plt.ylim(10, 50)
    #sns_scatterplot.axes[0, 0].set_ylim(0,)
    #sns_scatterplot.axes[0, 0].set_xlim(0, 35)
    
    fig_ = sns_scatterplot.get_figure()
    fig_.savefig("scatterplot_vehicles.pdf")
    fig_.savefig("scatterplot_vehicles.png")
