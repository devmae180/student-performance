from src.cleaning import clean_data
import pandas as pd

def test_clean_data_removes_duplicates():
       df = pd.DataFrame({
       "name": ["Alieh", "Mae", "Bob"],
       "score": [80, 90, 70]
        })

       result = clean_data(df)
       assert len(result) == 2