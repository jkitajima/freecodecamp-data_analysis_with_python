"""
Time Series Visualizer

For this project you will visualize time series data using a
line chart, bar chart, and box plots. You will use
Pandas, Matplotlib, and Seaborn to visualize a dataset containing the
number of page views each day on the freeCodeCamp.org forum
from 2016-05-09 to 2019-12-03. The data visualizations will help you
understand the patterns in visits and identify
yearly and monthly growth.
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


df = pd.read_csv('time_series_visualizer/fcc-forum-pageviews.csv',
                 index_col=0,
                 parse_dates=True)

mask = (df['value'] > df['value'].quantile(0.975)) | (df['value'] < df['value'].quantile(0.025))
df = df.drop(df.loc[mask].index)


def draw_line_plot() -> object:
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(df.index, df['value'])
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    fig.savefig('line_plot.png')
    plt.show()
    
    return fig

draw_line_plot()


def draw_bar_plot() -> object:
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.strftime('%Y')
    df_bar['month'] = df_bar.index.strftime('%m')
    
    years = df_bar.groupby('year')
    month_names = ['01', '02', '03',
                   '04', '05', '06',
                   '07', '08', '09',
                   '10', '11', '12']
    months = {month: [] for month in month_names}
    labels = []
    
    for k, _ in years:
        k = int(k)
        labels.append(k)
    
    labels = np.array(labels, dtype='int')
    years_and_months = df_bar.groupby(['year', 'month']) 
    first_month = df_bar.index[0].strftime('%m')
    first_month_num = int(first_month)
    
    if first_month_num != 1:
        for e in months:
            if not e == first_month:
                months[e].append(0)
            else:
                break
    
    for k, v in years_and_months:
        months[k[1]].append(v['value'].mean())
        
    x = np.arange(len(labels))
    width = 0.05
    
    fig, ax = plt.subplots(figsize=(12, 12))
    b1 = ax.bar(x - (11 * width/2), months['01'], width, label='January')
    b2 = ax.bar(x - (9 * width/2), months['02'], width, label='February')
    b3 = ax.bar(x - (7 * width/2), months['03'], width, label='March')
    b4 = ax.bar(x - (5 * width/2), months['04'], width, label='April')
    b5 = ax.bar(x - (3 * width/2), months['05'], width, label='May')
    b6 = ax.bar(x - (1 * width/2), months['06'], width, label='June')
    b7 = ax.bar(x + (1 * width/2), months['07'], width, label='July')
    b8 = ax.bar(x + (3 * width/2), months['08'], width, label='August')
    b9 = ax.bar(x + (5 * width/2), months['09'], width, label='September')
    b10 = ax.bar(x + (7 * width/2), months['10'], width, label='October')
    b11 = ax.bar(x + (9 * width/2), months['11'], width, label='November')
    b12 = ax.bar(x + (11 * width/2), months['12'], width, label='December')
    
    ax.legend(['January', 'February', 'March',
              'April', 'May', 'June',
              'July', 'August', 'September',
              'October', 'November', 'December'], title='Months')
    ax.set_ylabel('Average Page Views')
    ax.set_xlabel('Years')
    ax.set_xticks(x, labels)
    fig.savefig('bar_plot.png')
    plt.show()
    
    return fig

draw_bar_plot()


def draw_box_plot() -> object:
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 9))
    ax1 = sns.boxplot(ax=ax1, x=df_box['year'], y=df_box['value'])
    ax2 = sns.boxplot(ax=ax2, x=df_box['month'], y=df_box['value'], order=['Jan', 'Feb', 'Mar',
                                                                     'Apr', 'May', 'Jun',
                                                                     'Jul', 'Sep', 'Aug',
                                                                     'Oct', 'Nov', 'Dec'])
    
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax2.set_title('Month-wise Box Plot (Seasonality)')

    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    
    fig.savefig('box_plot.png')
    plt.show()
    
    return fig

draw_box_plot()
