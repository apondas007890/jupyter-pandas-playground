# scripts/utils.py
import pandas as pd
import os

DATA_PATH = '/home/jovyan/work/data'
OUTPUT_PATH = '/home/jovyan/work/outputs'

def load_data(filename):
    """Load CSV from data folder"""
    path = f"{DATA_PATH}/{filename}"
    return pd.read_csv(path)

def save_data(df, filename):
    """Save DataFrame to outputs folder"""
    path = f"{OUTPUT_PATH}/{filename}"
    df.to_csv(path, index=False)
    print(f"✅ Saved to: {path}")

def create_sample():
    """Create sample data"""
    import numpy as np
    return pd.DataFrame({
        'id': range(1, 101),
        'name': [f'User_{i}' for i in range(1, 101)],
        'age': np.random.randint(18, 60, 100),
        'score': np.random.uniform(0, 100, 100)
    })