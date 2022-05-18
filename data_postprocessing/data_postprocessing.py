import pandas as pd
import numpy as np

def read_csv_to_df(files: list, filepath: str):
    # read a number of files in one folder and return the data as a pd.DataFrame()
    firstrun = True
    for file in files:
        df = pd.read_csv(filepath+'\\'+file, sep=';', encoding='latin1')
        if firstrun:
            data = df
            firstrun = False
        else:
            data = data.append(df)
    return data


def aggregate_samplingtime(data: pd.DataFrame(), aggregation_rate: int):
    return data.groupby(np.arange(len(data)//aggregation_rate).mean())


def convert_column_names(data: pd.DataFrame(), parameterID: pd.DataFrame()):
    new_header = []
    for id in data.columns:
        if id in parameterID['ID(hex)'].values:
            id_clear = parameterID[parameterID['ID(hex)'] == id]['Custom name'].item()
        else:
            id_clear = id
        if id == 'Timestamp':
            id_clear = 'timestamp'
        new_header.append(id_clear)
    data.columns = new_header
    return data
