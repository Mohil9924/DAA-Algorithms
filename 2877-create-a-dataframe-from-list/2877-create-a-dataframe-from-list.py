import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    """
    Creates a DataFrame from a list of student data.
    """
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df