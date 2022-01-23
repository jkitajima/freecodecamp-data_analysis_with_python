"""
Medical Data Visualizer

The dataset values were collected during medical examinations.
The rows in the dataset represent patients and the columns represent
information like body measurements, results from various
blood tests, and lifestyle choices.
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('medical_data_visualizer/medical_examination.csv')

data['overweight'] = data.loc[:, 'weight'] / ((data.loc[:, 'height'] / 100) ** 2)
data.loc[data['overweight'] > 25, 'overweight'] = 1
data.loc[data['overweight'] != 1, 'overweight'] = 0
data['overweight'] = data['overweight'].astype('int8')

data.loc[data['cholesterol'] == 1, 'cholesterol'] = 0
data.loc[data['cholesterol'] != 0, 'cholesterol'] = 1
data.loc[data['gluc'] == 1, 'gluc'] = 0
data.loc[data['gluc'] != 0, 'gluc'] = 1
data[['cholesterol', 'gluc']] = data[['cholesterol', 'gluc']].astype('int8')
data[['cardio', 'smoke',
      'alco', 'active']] = data[['cardio', 'smoke', 'alco', 'active']].astype('int8')


def draw_cat_plot() -> object:
    df_cat = pd.melt(data,
                     id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke',
                                 'alco', 'active', 'overweight'])
    
    fig = sns.catplot(data=df_cat, x='variable', hue='value', col='cardio', kind='count',
                    order=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    fig.set_ylabels('total')
    fig.savefig('catplot.png')
    
    return fig


def draw_heat_map() -> object:
    df_heat = data.drop(data.loc[data['ap_lo'] > data['ap_hi'], ['ap_lo', 'ap_hi']].index)
    
    df_heat = df_heat.drop(
        df_heat.loc[data['height'] < df_heat['height'].quantile(0.025), 'height'].index)
    
    df_heat = df_heat.drop(
        df_heat.loc[data['height'] > df_heat['height'].quantile(0.975), 'height'].index)
    
    df_heat = df_heat.drop(
        df_heat.loc[data['weight'] < data['weight'].quantile(0.025), 'weight'].index)
    
    df_heat = df_heat.drop(
        df_heat.loc[data['weight'] > data['weight'].quantile(0.975), 'weight'].index)
    
    corr = round(df_heat.corr(), 1)
    mask = np.triu(np.ones_like(corr, dtype='bool'))
    f, ax = plt.subplots(figsize=(11, 9))
    hmap = sns.heatmap(corr, mask=mask, square=True, annot=True)
    fig = hmap.get_figure()
    fig.savefig('heatmap.png')
    
    return fig
