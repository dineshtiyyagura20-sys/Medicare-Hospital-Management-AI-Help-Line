import os
import pandas as pd


def read_csv(file_path, columns=None):
    """
    Read a CSV file.
    If the file does not exist, create it.
    """

    if not os.path.exists(file_path):

        df = pd.DataFrame(columns=columns)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        df.to_csv(file_path, index=False)

        return df

    return pd.read_csv(file_path)


def add_record(file_path, record, columns=None):
    """
    Add a new record into a CSV file.
    """

    df = read_csv(file_path, columns)

    new_record = pd.DataFrame([record])

    df = pd.concat([df, new_record], ignore_index=True)

    df.to_csv(file_path, index=False)


def save_csv(file_path, df):
    """
    Save complete DataFrame into CSV.
    """

    df.to_csv(file_path, index=False)