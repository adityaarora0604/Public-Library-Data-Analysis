import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run_eda(file_path):
    df = pd.read_csv('data/cleaned_libraries.csv')

    sns.set(style="whitegrid")

    # 1: Operating Expenditures vs Total Circulation
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x="Operating Expenditures", y="Total Circulation", color="#FF6F61", edgecolor='black', s=60)
    plt.title("Operating Expenditures vs Total Circulation", fontsize=14, fontweight='bold')
    plt.xlabel("Operating Expenditures")
    plt.ylabel("Total Circulation")
    plt.tight_layout()
    plt.show()

    # 2: Total Library Visits vs Population
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x="Population of Service Area", y="Total Library Visits", color="#6A5ACD", edgecolor='black', s=60)
    plt.title("Total Library Visits vs Population", fontsize=14, fontweight='bold')
    plt.xlabel("Population of Service Area")
    plt.ylabel("Total Library Visits")
    plt.tight_layout()
    plt.show()
