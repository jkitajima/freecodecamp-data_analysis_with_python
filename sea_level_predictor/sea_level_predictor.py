"""
Sea Level Predictor

Anaylize a dataset of the global average sea level change since 1880.
Use the data to predict the sea level change through year 2050.
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot() -> object:
    data = pd.read_csv('sea_level_predictor/epa-sea-level.csv')
    
    fig, ax = plt.subplots(figsize=(7,7))
    ax.scatter(x=data['Year'], y=data['CSIRO Adjusted Sea Level'])
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    linreg = linregress(x=data['Year'], y=data['CSIRO Adjusted Sea Level'])
    last_year = data['Year'].iloc[data['Year'].last_valid_index()] + 1
    final_year = 2050
    years = [year for year in data['Year']]
    
    while final_year >= last_year:
        years.append(last_year)        
        last_year += 1
    
    years = pd.Series(years)
    best_fit = linreg.slope*years + linreg.intercept
    ax.plot(years, best_fit, 'r')
    
    recent_data = data.drop(data.loc[data['Year'] < 2000].index)
    rd_linreg = linregress(x=recent_data['Year'],
                           y=recent_data['CSIRO Adjusted Sea Level'])
    recent_years = [year for year in recent_data['Year']]
    final_year = 2050
    last_year = recent_data['Year'].iloc[-1] + 1
    
    while final_year >= last_year:
        recent_years.append(last_year)
        last_year += 1

    recent_years = pd.Series(recent_years)
    rd_best_fit = rd_linreg.slope*recent_years + rd_linreg.intercept
    ax.plot(recent_years, rd_best_fit, 'b')
    plt.savefig('sea_level_plot.png')
    plt.show()
    
    return plt.gca()

draw_plot()
