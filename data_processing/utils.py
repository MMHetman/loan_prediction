from typing import Callable, Iterable, List

import pandas as pd
from sklearn.preprocessing import LabelEncoder


def encode_target(dataset: pd.DataFrame, predicate: Callable) -> pd.DataFrame:
    """
    Encode binary target

    :param dataset: DataFrame
    :param predicate: boolean callable - condition for 0/1 target coding
    :return: dataset with target column
    """
    target = predicate(dataset).astype(int)
    transformed_dataset = dataset.copy()
    transformed_dataset['target'] = target
    return transformed_dataset


def split_date(dataset: pd.DataFrame, date_features: List[str], sep: str, units: List[str]) -> pd.DataFrame:
    """
    Split date columns into separate columns

    :param dataset: DataFrame
    :param date_features: Date columns names
    :param sep: Date units separator
    :param units: Date units included in date features
    :return: DataFrame with split date columns
    """
    df = dataset.copy()
    for feat in date_features:
        df[[f'{feat}{unit}' for unit in units]] = df[feat].str.split(sep, 1, expand=True)
    return df.drop(columns=date_features)


# https://www.kaggle.com/yogeshrampariya/lending-club-classification-cleaning-modeling
def one_hot_encode(df: pd.DataFrame, features: Iterable) -> pd.DataFrame:
    """
    Encode categorical features using one-hot

    :param df: DataFrame
    :param features: Features to encode
    :return: DataFrame with encoded features
    """
    for value in features:
        dummy = pd.get_dummies(df[value], prefix=value)
        df = pd.concat([df, dummy], axis=1)
        df = df.drop(value, axis=1)
    return df


def binary_encode(df: pd.DataFrame, features: Iterable) -> pd.DataFrame:
    """
    Encode binary features

    :param df: DataFrame
    :param features: Features to encode
    :return: DataFrame with encoded features
    """
    df = df.copy()
    for value in features:
        lbl = LabelEncoder()
        df[value] = lbl.fit_transform(df[[value]])
    return df
