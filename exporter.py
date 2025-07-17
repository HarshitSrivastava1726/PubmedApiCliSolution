import pandas as pd
from typing import List, Dict

def export_to_csv(data: List[Dict], filename: str = None):
    df = pd.DataFrame(data)
    if filename:
        df.to_csv(filename, index=False)
    else:
        print(df.to_csv(index=False))
