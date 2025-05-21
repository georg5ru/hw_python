import pandas as pd
from typing import List, Dict


def read_csv_transactions(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV файла и возвращает их в виде списка словарей,
    где каждый словарь представляет собой пары "ключ-значение".
    """
    return pd.read_csv(file_path).to_dict(orient='records')


def read_excel_transactions(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel файла.
    """
    df = pd.read_excel(file_path)
    return df.to_dict('records')
