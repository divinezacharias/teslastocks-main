import pandas as pd

class Summary:
    """
    Computes numeric statistical descriptors like mean, median, std deviation, minimum, maximum value and quantiles on Tesla stock data.
    """
    def __init__(self, dataframe):
        assert isinstance(dataframe, pd.DataFrame), "Input should be a Pandas DataFrame"
        #This assertion checks whether the dataframe is a pandas dataframe or not
        self.tesla = dataframe

    def get_summary(self):
        """
        Returns mean, median, minimum, maximum value, quantiles and standard deviation of the closing price.
        """
        assert "closing_price" in self.tesla.columns, "DataFrame must contain 'closing_price' column"
        #This assertion checks if dataframe have the required column or not
        return {
            "Mean": self.tesla["closing_price"].mean(),
            "Median": self.tesla["closing_price"].median(),
            "Std Dev": self.tesla["closing_price"].std(),
            "Min": self.tesla["closing_price"].min(),
            "Max": self.tesla["closing_price"].max(),
            "Quantiles": self.tesla["closing_price"].quantile([0.25, 0.5, 0.75]).to_dict()
        }
