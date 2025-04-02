import pandas as pd
from typing import List, Dict

file_path = "C:\\Users\\Pokhlebin.G\\Downloads\\transactions.csv"

def read_transactions_from_csv(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла.
    """
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        raise ValueError(f"Ошибка при чтении CSV-файла: {e}")