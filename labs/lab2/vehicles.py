import matplotlib
import matplotlib.pyplot as plt 
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import numpy as np

if __name__ == "__main__":
    df = pd.read_csv('./data/vehicles.csv')
    df = df.dropna()
    data = df.values.T[1]

    sns_distplot = sns.distplot(df.values.T[0])
    sns_distplot = sns.distplot(df.values.T[1])
    plt.legend(['Current fleet', 'New Fleet'], loc='best')
    # sns_distplot.set(xlabel='common xlabel', ylabel='common ylabel')
    fig = sns_distplot.get_figure()
    fig.savefig("./png/distplot_vehicles.png")
    fig.savefig("./pdf/distplot_vehicles.pdf")

    plt.legend()
    sns_scatterplot = sns.scatterplot(df.columns[0], df.columns[1],data=df)
    plt.xlim(0, 35)
    plt.ylim(10, 50)
    
    fig_ = sns_scatterplot.get_figure()
    fig_.savefig("./png/scatterplot_vehicles.png")
    fig_.savefig("./pdf/scatterplot_vehicles.pdf")
