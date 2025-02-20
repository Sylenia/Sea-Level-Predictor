import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 5))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original data')

    # Create first line of best fit for all data
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_levels_extended = result.slope * years_extended + result.intercept
    plt.plot(years_extended, sea_levels_extended, color='orange', label='Best fit line (1880-2050)')

    # Create second line of best fit for data from 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    result_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent_extended = pd.Series(range(2000, 2051))
    sea_levels_recent = result_recent.slope * years_recent_extended + result_recent.intercept
    plt.plot(years_recent_extended, sea_levels_recent, color='green', label='Best fit line (2000-2050)')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()
