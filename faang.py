#!/usr/bin/env python3

import yfinance as yf
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

def get_data():
    tickers = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']
    
    # Get data of the last 5 days for the 5 FAANG stocks
    data = yf.download(
        tickers=tickers,
        period="5d",
        interval="1h",
        group_by="ticker",
        auto_adjust=True
    )

    # Create a timestamped filename
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"data/{timestamp}.csv"

    # Save the dataset as a CSV file in the data folder
    data.to_csv(filename)

    print(f"Data saved to: {filename}")
    return data

def load_close_prices(filename):
    # Load CSV file with multi-level headers
    df_raw = pd.read_csv(filename, header=[0,1], index_col=0, parse_dates=True)
    
    # Extract only the columns with 'Close'
    close_df = df_raw.xs('Close', level=1, axis=1)
    
    return close_df

def generate_filename():
    # Generate a timestamp string in the format YYYYMMDD-HHmmss
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    
    # Create the output filename inside 'plots' folder
    return f"plots/{timestamp}.png"

def plot_data():
    # Specify the latest data file
    latest_file = "data/20251204-165637.csv"
    
    # Load only closing prices from CSV
    close_df = load_close_prices(latest_file)
    
    # Extract last date from index to use it as plot title
    title = close_df.index[-1].strftime("%Y-%m-%d")
    
    # Generate the output filename
    filename = generate_filename()
    
    # Plot all closing prices on the same figure
    ax = close_df.plot(title=f"Close Prices - {title}", xlabel="Date", ylabel="Price")
    
    # Get the figure from the axes object so we can save it
    fig = ax.get_figure()
    
    # Save the figure as a PNG file in the 'plots' folder
    fig.savefig(filename)
    
    # Print confirmation with the saved filename
    print(f"Plot saved to: {filename}")

if __name__ == "__main__":
    get_data()
    plot_data()
