import pandas as pd

from .utils import encode_target, binary_encode, one_hot_encode
from .settings import SELECTED_FEATURES, BINARY_FEATURES, CATEGORY_FEATURES


def transform(dataset: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms raw data into defined format

    :param dataset: raw format DataFrame
    :return: transformed DataFrame
    """
    dataset = dataset\
        .pipe(encode_target, predicate=lambda df: (df.loan_status == 'Fully Paid').astype(int))\
        #.pipe(split_date, date_features=DATE_FEATURES, sep='-', units=['month', 'year'])

    dataset = dataset[SELECTED_FEATURES]

    return dataset\
        .pipe(binary_encode, features=BINARY_FEATURES)\
        .pipe(one_hot_encode, features=CATEGORY_FEATURES)
