# Load a data for Auckland and Christchurch and compare the temperature between two cities in a year monthly basis -  See Link: https://data.niwa.co.nz/pages/clidb-on-datahub

import pandas as pd
from pathlib import Path


class TemperatureData:
    def __init__(self, city, file_path):
        self.file_path = file_path
        self.city = city
        self.df = None

    def load_data(self):
        # Load the data from the CSV file
        self.df = pd.read_csv(self.file_path)

    def compare_temperature(self, other, year=2020):
        # Check if data is loaded
        if self.df is None or other.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")

        # Check if year exists in both datasets
        if year not in self.df['YEAR'].values:
            raise ValueError(f"Year {year} not found in {self.city} dataset.")
        if year not in other.df['YEAR'].values:
            raise ValueError(f"Year {year} not found in {other.city} dataset.")
        
        # Drop non-month columns
        months = self.df.columns[1:-1]  

        # Get the temperature values for the specified year
        my_city_values = self.df[self.df['YEAR'] == year][months].iloc[0].values
        other_city_values = other.df[other.df['YEAR'] == year][months].iloc[0].values

        # Compare month by month
        print(f"Comparing temperatures for {self.city} and {other.city} in {year}:")
        for month, my_val, other_val in zip(months, my_city_values, other_city_values):
            if pd.isna(my_val) or pd.isna(other_val):
                print(f"In {month}, temperature data is missing for one or both cities.")
            elif my_val > other_val:
                print(f"In {month}, {self.city} was hotter.")
            elif my_val < other_val:
                print(f"In {month}, {other.city} was hotter.")
            else:
                print(f"In {month}, both cities had the same temperature.")



if __name__ == "__main__":
    current_dir = Path(__file__).parent

    file_path = current_dir / "auckland_monthly_temperature.csv"
    auckland_temperature = TemperatureData('Auckland', file_path)
    auckland_temperature.load_data()

    file_path = current_dir / "christchurch_monthly_temperature.csv"
    christchurch_temperature = TemperatureData('Chirstchurch', file_path)
    christchurch_temperature.load_data()

    auckland_temperature.compare_temperature(christchurch_temperature)
        
