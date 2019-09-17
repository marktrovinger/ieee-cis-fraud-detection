from tpot import TPOTClassifier
from sklearn.model_selection import train_test_split

from dask.distributed import Client

def generate_tpot_model(self, train_df, test_df,  generations, population, use_dask=True):
    
    client = Client(workers=6, threads=2)
    
    X_train, y_train, X_test, y_test = train_test_split(train_df, test_df, random_state=42, test_size=0.25)

    tp = TPOTClassifier(generations=generations, population_size=population, use_dask=use_dask, verbosity=2, n_jobs=-1)

    tp.fit(X_train, y_train)