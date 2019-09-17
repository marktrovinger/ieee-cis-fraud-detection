import src.data_cleaning as data_cleaning
import os
import pandas as pd
import src.notify as notify
import src.generate_model as gen_model

def main():
    if os.path.isfile(os.path.join('/data/interim_dataframes', 'train_identity.csv')):
        print('reading file')
        train_identity_df = pd.read_csv(os.path.join('data/raw', 'train_identity.csv'), index_col='TransactionID')
        train_transaction_df = pd.read_csv(os.path.join('data/raw', 'train_transaction.csv'), index_col='TransactionID')

    test_identity_df = pd.read_csv(os.path.join('data/raw', 'test_identity.csv'), index_col='TransactionID')
    test_transaction_df = pd.read_csv(os.path.join('data/raw', 'test_transaction.csv'), index_col='TransactionID')

    train_identity_df_clean = data_cleaning.clean_dataset(train_identity_df, 'train_identity')
    train_transaction_df_clean = data_cleaning.clean_dataset(train_transaction_df, 'train_transaction')

    test_identity_df_clean = data_cleaning.clean_dataset(test_identity_df, 'test_identity')
    test_transaction_df_clean = data_cleaning.clean_dataset(test_transaction_df, 'test_transaction')

    train_full_df = train_transaction_df_clean.merge(train_identity_df_clean, how='left', left_index=True, right_index=True)
    test_full_df = test_transaction_df_clean.merge(test_identity_df_clean, how='left', left_index=True, right_index=True)

    train_full_df = train_full_df.fillna(-999)
    
    X = train_full_df.drop('isFraud', axis = 1).values
    y = train_full_df['isFraud'].values

    gen_model.generate_tpot_model(X, y, 10, 10, True)

    notify.submit_kaggle(train_full_df, 'test', '', test=True)
    notify.notify('Kaggle submission complete.')

if __name__ == "__main__":
    main()