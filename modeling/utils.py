from typing import Dict, List

import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score


def evaluate(
        model, model_label: str, X_train: pd.DataFrame, y_train: pd.Series, X_test: pd.DataFrame, y_test: pd.Series, tsh: float
) -> List[Dict]:
    """
    Evaluate model using accuracy, precision, recall, f1 and auc score

    :param model: Predictor
    :param model_label: Descrpitive model name string
    :param X_train: train dataset
    :param y_train: train target
    :param X_test: test dataset
    :param y_test: test target
    :param tsh: cut of value
    :return:
    """
    result = []
    for X, y, label in ((X_train, y_train, 'train'), (X_test, y_test, 'test')):
        y_pred = model.predict_proba(X)[:, 1]
        tn, fp, fn, tp = confusion_matrix(y, y_pred > tsh).ravel()
        accuracy = accuracy_score(y, y_pred > tsh)
        auc = roc_auc_score(y, y_pred)

        record = {
            'model': model_label,
            'data': label,
            'accuracy': accuracy,
            'sensitivity': tp/(tp+fn),
            'specifity': tn/(tn+fp),
            'auc': auc
        }

        result.append(record)

    return result
