import src.reduce_mem_usage as reduce_mem_usage
import pickle
import os
import pandas as pd

# for the moment, just reduce the size of the dataframes and save to the interim dataframes folder
def clean_dataset(df, name):
    filename = name +'.pkl'
    print(filename)
    if os.path.exists(os.path.join('/data/interim_dataframes', filename)):
        print('Found file.')
        df_reduced = pd.read_pickle(os.path.join('data/interim_dataframes', name+'.pkl'))
    else:
        df_reduced = reduce_mem_usage.reduce_mem_usage(df)
        df_reduced.to_pickle(os.path.join('data/interm_dataframes', name+'.pkl'))

    return df_reduced