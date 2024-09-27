import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('epa-sea-level.csv')

def draw_plot():
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label="Data Points")

    slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_all = pd.Series(range(1880, 2051))
    y_all = slope_all * x_all + intercept_all
    ax.plot(x_all, y_all, label='Best Fit Line (All Data)', color='red')

    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, _, _, _ = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_2000 = pd.Series(range(2000, 2051))
    y_2000 = slope_2000 * x_2000 + intercept_2000
    ax.plot(x_2000, y_2000, label='Best Fit Line (From 2000)', color='green')

    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    plt.savefig('sea_level_plot.png')
    return plt.gca()