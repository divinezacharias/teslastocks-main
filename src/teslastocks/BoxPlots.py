import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import seaborn as sns
import pandas.plotting as pd_plot

class Boxplots:
    """
    This class generates boxplots to analyze Tesla stock data over different time intervals.
    The boxplots can visualize the distribution of the 'closing_price' column across various time intervals 
    such as days of the week, weeks of the year, months, and years.

    Methods:
    - boxplot_daywise: Creates a boxplot for the distribution of closing prices across days of the week.
    - boxplot_weeks: Creates a boxplot for the distribution of closing prices across weeks of the year.
    - boxplot_monthwise: Creates a boxplot for the distribution of closing prices across months of the year.
    - boxplot_years: Creates a boxplot for the distribution of closing prices across different years.
    """
    def __init__(self, dataframe):
        """
        Initializes the Boxplots class with a dataframe containing Tesla stock data.

        Parameters:
        dataframe (pd.DataFrame): The DataFrame containing Tesla stock data. 
        It should have at least a 'Year' column and 'closing_price' column.
        
        Raises:
        AssertionError: If the input is not a Pandas DataFrame or lacks the 'Year' column.
        """
        assert isinstance(dataframe, pd.DataFrame), "Input should be a Pandas DataFrame"
        self.tesla = dataframe.copy()

        # Ensure 'date' column exists and is in datetime format
        assert 'Year' in self.tesla.columns, "DataFrame must contain a 'date' column"
        self.tesla['Year'] = pd.to_datetime(self.tesla['Year'])

    def boxplot_daywise(self):
        """
        Generates a boxplot showing the distribution of closing prices across the days of the week.

        The days of the week are represented as numeric values from 0 (Monday) to 6 (Sunday).
        """
        self.tesla["Day"] = self.tesla["Year"].dt.dayofweek
        plt.figure(figsize=(10, 6))
        sns.boxplot(x="Day", y="closing_price", data=self.tesla)
        plt.xticks(ticks=range(7), labels=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
        plt.xlabel("Day of the Week")
        plt.ylabel("Closing Price")
        plt.title("Boxplot of Closing Prices Across Days of the Week")
        plt.show()

    def boxplot_weeks(self):
        """ 
        Generates a boxplot showing the distribution of closing prices across the weeks of the year.
        
        The weeks are represented by ISO calendar weeks 
        """
        self.tesla["Week"] = self.tesla["Year"].dt.isocalendar().week
        plt.figure(figsize=(12, 6))
        sns.boxplot(x="Week", y="closing_price", data=self.tesla)
        plt.xlabel("Week of the Year")
        plt.ylabel("Closing Price")
        plt.title("Boxplot of Closing Prices Across Weeks")
        plt.xticks(rotation=90)
        plt.show()

    def boxplot_monthwise(self):
        """ 
        Boxplot for months of the year. Generates a boxplot showing the distribution of closing prices across the months of the year.

        The months are represented by numbers from 1 (January) to 12 (December) 
        """
        self.tesla["Month"] = self.tesla["Year"].dt.month
        plt.figure(figsize=(13, 7))
        sns.boxplot(x="Month", y="closing_price", data=self.tesla)
        plt.xlabel("Month")
        plt.ylabel("Closing Price")
        plt.title("Boxplot of Closing Prices Across Months")
        plt.xticks(ticks=range(1, 13), labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                                               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
        plt.show()

    def boxplot_years(self):
        """ 
        Boxplot for years. 
        Generates a boxplot showing the distribution of closing prices across different years.

        The years are extracted from the 'Year' column.
        """
        self.tesla["Year_Num"] = self.tesla["Year"].dt.year  # Using "Year_Num" for consistency
        plt.figure(figsize=(13, 7))
        sns.boxplot(x="Year_Num", y="closing_price", data=self.tesla)
        plt.xlabel("Year")
        plt.ylabel("Closing Price")
        plt.title("Boxplot of Closing Prices Across Years")
        plt.xticks(rotation=45)
        plt.show()
