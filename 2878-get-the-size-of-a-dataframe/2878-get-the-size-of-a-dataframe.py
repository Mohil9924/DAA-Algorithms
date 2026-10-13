import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    shape = players.shape
    return [shape[0], shape[1]]  # Return as a list: [number of rows, number of columns]