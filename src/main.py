from load_and_clean import load_data, clean_data

def main():
    print("Public Library Data Analysis Project")

    file_path = "data/libraries.csv"
    df = load_data(file_path)

    if df is not None:
        df = clean_data(df)

       from visualizations import run_visuals
        run_visuals(df)

       from eda_analysis import funding_vs_usage, population_vs_percapita
        funding_vs_usage(df)
        population_vs_percapita(df)


        print("\nProject ran successfully!")

        cleaned_file_path = "data/cleaned_libraries.csv"
        df.to_csv(cleaned_file_path, index=False)
        print(f"Cleaned data saved to: {cleaned_file_path}")

    else:
        print("Project aborted due to data loading issue.")


if __name__ == "__main__":
    main()

