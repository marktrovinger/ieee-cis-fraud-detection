import src.data_cleaning as data_cleaning
import os
import pandas as pd
import src.notify as notify

def main():
    train_identity_df = pd.read_csv(os.path.join('data/raw', 'train_identity.csv'), index_col='TransactionID')
    train_transaction_df = pd.read_csv(os.path.join('data/raw', 'train_transaction.csv'), index_col='TransactionID')

    train_identity_df_clean = data_cleaning.clean_dataset(train_identity_df, 'train_identity')
    train_transaction_df_clean = data_cleaning.clean_dataset(train_transaction_df, 'train_transaction')

    train_full_df = train_transaction_df_clean.merge(train_identity_df_clean, how='left', left_index=True, right_index=True)

    notify.notify('Kaggle submission complete.')

if __name__ == "__main__":
    main()