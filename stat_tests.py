import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

def run_stats(df):
    print("Hypothesis Test: Does population affect per capita program attendance?\n")


    df = df.dropna(subset=["Population of Service Area", "Total Program Attendance & Views Per Capita Served"])

    # Split into high/low population groups
    median_pop = df["Population of Service Area"].median()
    df["Population Group"] = df["Population of Service Area"].apply(
        lambda x: "High Population" if x > median_pop else "Low Population"
    )

    # Grouped data
    high_group = df[df["Population Group"] == "High Population"]["Total Program Attendance & Views Per Capita Served"]
    low_group = df[df["Population Group"] == "Low Population"]["Total Program Attendance & Views Per Capita Served"]

    # T-test
    t_stat, p_val = ttest_ind(high_group, low_group)


    print(f"🔹 t-statistic: {t_stat:.3f}")
    print(f"🔹 p-value: {p_val:.4f}")

    # what do results say?
    if p_val < 0.05:
        print("\033[92mStatistically significant difference in per capita attendance!\033[0m")
        print("\033[1mConclusion:\033[0m The hypothesis is supported ")
    else:
        print("\033[91mNo statistically significant difference found.\033[0m")
        print("\033[1mConclusion:\033[0m The hypothesis is not supported ")

    #visualisation:
    plt.figure(figsize=(9, 5))
    sns.boxplot(data=df,
                x="Population Group",
                y="Total Program Attendance & Views Per Capita Served",
                palette=["#4DB6AC", "#FF8A65"])
    plt.title("Program Attendance per Capita by Population Group", fontsize=13, fontweight='bold')
    plt.xlabel("")
    plt.ylabel("Per Capita Attendance")
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.tight_layout()
    plt.show()
