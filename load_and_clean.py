import pandas as pd

def load_data(file_path):

    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns.")
        return df
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):

    print("Cleaning data...")
    #where the values are missing more than 50%, remove them
    threshold = len(df) * 0.5
    df = df.dropna(thresh=threshold, axis=1)

    num_cols = df.select_dtypes(include='number').columns
    df[num_cols] = df[num_cols].fillna(0)

    cat_cols = df.select_dtypes(include='object').columns
    df[cat_cols] = df[cat_cols].fillna('Unknown')

    print("Cleaning complete.")
    return df

