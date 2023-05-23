import pandas as pd
import matplotlib.pyplot as plt

class DataCleaner:
    def __init__(self, reader, view):
        self.reader = reader
        self.view = view


    def clean_data(self):
        data = self._reader.data
        

    



def percentstr2float(df, column):
    for idx, elem in enumerate(df[column]):
        if isinstance(elem, float):
            continue
        try:
            numeric_value = float(elem[:-1]) / 100
        except:
            numeric_value = float(elem[:-1].replace(',', '.')) / 100
        df.loc[idx, column] = numeric_value
    return df

def comma2dot(df, column):
    for idx, elem in enumerate(df[column]):
        if not isinstance(elem, str):
            continue
        numeric_value = float(elem.replace(',', '.'))
        df.loc[idx, column] = numeric_value
    return df