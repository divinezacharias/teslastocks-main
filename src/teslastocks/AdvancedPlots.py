import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas.plotting as pd_plot

class AdvancedPlots:
    """
    Generates advanced visualizations like seasonal plot, lagsplot and generate autocorrelation value as well for Tesla stock data.
    """
    def __init__(self, dataframe):
        assert isinstance(dataframe, pd.DataFrame), "Input should be a Pandas DataFrame"
        #This assertion checks whether the dataframe is a pandas dataframe or not
        self.tesla = dataframe

    def seasonal_plot(self):
        """
        Creates a seasonal plot of Tesla's closing prices. Seasonal plot in time series analysis provide insights on
        seasons of every year in a parallel fashion. This helps to identify month wise trends on every year.

        """
        assert "Month" in self.tesla.columns and "Year_Num" in self.tesla.columns, "Data must be preprocessed first"
        #This assertion checks whether the dataframe is void of missing and duplicate values

        plt.figure(figsize=(13, 7))
        colors = plt.cm.rainbow(np.linspace(0, 1, self.tesla["Year_Num"].nunique()))
        #loop through every year and displays a different colour line for each year.
        for (year, color) in zip(self.tesla["Year_Num"].unique(), colors):
            subset = self.tesla[self.tesla["Year_Num"] == year]
            plt.plot(subset["Month"], subset["closing_price"], label=year, color=color)
        #labelling x and y axes
        plt.xlabel("Month")
        plt.ylabel("Closing Price")
        plt.title("Seasonal Plot of Tesla Closing Prices")
        plt.xticks(range(1, 13), ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
        plt.legend(title="Year", loc="upper left")
        plt.show()

    def lag_plot(self, lag=1, num_plots=10):
        """
        Generates lag plots which shows the similarity between past values and present value.

        Parameters used:
        lag (int): The lag value for the first plot. Default value here is 1.
        num_plots (int): The number of lag plots to generate (default value here is 10). The plots will be for
        lags from `lag` to `lag+num_plots-1`.
        """
        assert "closing_price" in self.tesla.columns, "DataFrame must contain 'closing_price' column"

        # Create subplots with 2 rows and 5 columns (for up to 10 lag plots)
        rows = 2
        cols = 5
        fig, axes = plt.subplots(rows, cols, figsize=(20, 7))

        # Flatten axes array for easier iteration
        axes = axes.flatten()

        # Loop through lag values and generate lag plots
        for i in range(num_plots):
            current_lag = lag + i
            ax = axes[i]
            pd_plot.lag_plot(self.tesla["closing_price"], lag=current_lag, ax=ax)
            ax.set_title(f"Lag {current_lag}")
            ax.grid(True)

        plt.tight_layout()
        plt.show()



    def autocorrelation(self, max_lag=10):
        """
        Calculate the Autocorrelation Function (ACF) of the closing prices for a range of lags. Autocorrelation measures the 
        similarity/correlation to previous lags. It ranges from -1 to 1. 1 indicates that past values strongly influences future
        values.

        Parameters:
        max_lag (int): Maximum lag value for which to compute ACF

        Returns:
        dict: A dictionary with lag values as keys and their corresponding autocorrelation as values
        """
        assert "closing_price" in self.tesla.columns, "DataFrame must contain 'closing_price' column"

        # Convert closing_price to numpy array
        series = self.tesla["closing_price"].values
        acf_values = {}

        # Calculate ACF for each lag from 1 to max_lag. Maxlag 10 means upto last 10 years
        for lag in range(1, max_lag + 1):
            # Shift the series by lag, align it with the original series, and calculate correlation
            shifted_series = series[lag:]
            original_series = series[:-lag]

            # Calculate the correlation
            correlation = np.corrcoef(original_series, shifted_series)[0, 1]
            acf_values[lag] = correlation

        return acf_values
