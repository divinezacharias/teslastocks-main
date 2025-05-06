import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas.plotting as pd_plot

class PreProcess:
    """
    Handles preprocessing of Tesla stock data such as converting year to datetime format, filling missing values and 
    removing duplicate values.
    """
    def __init__(self, dataframe):
        assert isinstance(dataframe, pd.DataFrame), "Input should be a Pandas DataFrame"
        #This assertion checks whether the dataframe is a pandas dataframe or not
        self.tesla = dataframe.copy()

    def preprocess(self):
        """
        Convert 'Year' column to datetime format, so that it is easy to maintain consistency and
        extract month and year.
        """
        self.tesla["Year"] = pd.to_datetime(self.tesla["Year"], errors='coerce')
        self.tesla.dropna(subset=["Year"], inplace=True)  # Remove invalid dates
        self.tesla["Month"] = self.tesla["Year"].dt.month #extracting months from date
        self.tesla["Year_Num"] = self.tesla["Year"].dt.year #extracts year as an integer
        return self.tesla
    def handle_missing_values(self):
        """
        Handle missing values by filling them with the previous value.
        """
        self.tesla.fillna(method='ffill', inplace=True)
        return self.tesla

    def remove_duplicates(self):
        """
        Remove duplicate rows.
        """
        self.tesla.drop_duplicates(inplace=True)
        return self.tesla
