import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="white")

def run_visuals(df):
    # Pie Chart on Expenditure Breakdown
    expenditures = df[['Library Materials Expenditures', 'Wages & Salaries Expenditures']].sum()
    labels = ['Library Materials', 'Wages & Salaries']
    colors = ['#4DB6AC', '#FF8A65']
    explode = (0.05, 0.05)

    plt.figure(figsize=(6, 6))
    plt.pie(
        expenditures,
        labels=labels,
        autopct='%1.1f%%',
        startangle=140,
        colors=colors,
        explode=explode,
        wedgeprops={'edgecolor': 'black', 'linewidth': 1}
    )
    plt.title('Expenditure Breakdown', fontsize=16, fontweight='bold')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
    input("Press Enter to continue...")

    
    # Top 10 Libraries by Program Attendance Per Capita (bar chart)
    top_libraries = df[['Library', 'Total Program Attendance & Views Per Capita Served']].copy()
    top_libraries['Total Program Attendance & Views Per Capita Served'] = pd.to_numeric(
        top_libraries['Total Program Attendance & Views Per Capita Served'], errors='coerce')
    top_libraries = top_libraries.dropna().sort_values(
        by='Total Program Attendance & Views Per Capita Served', ascending=False).head(10)

    plt.figure(figsize=(12, 6))
    sns.barplot(data=top_libraries, y='Library', x='Total Program Attendance & Views Per Capita Served', palette='mako')
    plt.title('Top 10 Libraries by Program Attendance Per Capita')
    plt.tight_layout()
    plt.show()
    input("Press Enter to continue...")

    # Top 10 Libraries by Total Program Attendance (vertical bar chart)
    def top_10_program_attendance(df):
        df_attendance = df[['Library', 'Total Program Attendance & Views']].copy()
        df_attendance['Total Program Attendance & Views'] = pd.to_numeric(
            df_attendance['Total Program Attendance & Views'], errors='coerce'
        )
        df_attendance = df_attendance.dropna()
        df_attendance = df_attendance[df_attendance['Total Program Attendance & Views'] > 0]
        top10 = df_attendance.groupby('Library').sum(numeric_only=True).nlargest(10, 'Total Program Attendance & Views')

        plt.figure(figsize=(12, 6))
        sns.barplot(data=top10.reset_index().sort_values('Total Program Attendance & Views'),
                    x='Library', y='Total Program Attendance & Views',
                    palette='rocket')
        plt.title("Top 10 Libraries by Program Attendance")
        plt.xlabel("Library")
        plt.ylabel("Total Program Attendance & Views")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        input("Press Enter to continue...")

    top_10_program_attendance(df)

    # Population Served vs. Library Visits
    df['Population of Service Area'] = pd.to_numeric(df['Population of Service Area'], errors='coerce')
    df['Total Library Visits'] = pd.to_numeric(df['Total Library Visits'], errors='coerce')

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Population of Service Area', y='Total Library Visits', hue='County', alpha=0.7)
    plt.title('Population vs. Library Visits')
    plt.xlabel('Population of Service Area')
    plt.ylabel('Total Library Visits')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()
    input("Press Enter to continue...")

    # Boxplot – Circulation Per Capita by County
    plt.figure(figsize=(14, 6))
    sns.boxplot(data=df, x='County', y='Circulation Per Capita Served', palette='Set2')
    plt.xticks(rotation=45)
    plt.title('Circulation Per Capita Distribution by County')
    plt.tight_layout()
    plt.show()
    input("Press Enter to continue...")

    # Heatmap – Focused Correlation on Key Metrics
    important_cols = [
        'Total Library Visits',
        'Total Circulation',
        'Population of Service Area',
        'Total Program Attendance & Views',
        'Use of Public Internet Computers',
        'Town Tax Appropriation for Library'
    ]
    # Convert to numeric
    df_subset = df[important_cols].apply(pd.to_numeric, errors='coerce')
    df_subset = df_subset.dropna()

    correlation = df_subset.corr()

    plt.figure(figsize=(10, 7))
    sns.heatmap(correlation, cmap='coolwarm', annot=True, fmt='.2f', linewidths=0.5)
    plt.title("Correlation Among Key Public Library Metrics")
    plt.tight_layout()
    plt.show()
    input("Press Enter to continue...")

