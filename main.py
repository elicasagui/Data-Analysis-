from src.load_data import load_test_results
from src.clean_data import clean_scores
from src.analyze import average_scores_by_borough
from src.visualize import plot_score_distribution
from src.utils import get_data_path

def main():
    # Load data
    print("📥 Loading data...")
    file_path = get_data_path("test_results_2022.csv")
    df = load_test_results(file_path)

    # Clean data
    print("🧼 Cleaning data...")
    df_clean = clean_scores(df)

    # Analyze data
    print("📊 Calculating average scores by borough...")
    borough_means = average_scores_by_borough(df_clean)
    print(borough_means)

    # Visualize results
    print("📈 Plotting score distribution...")
    plot_score_distribution(df_clean)

if __name__ == "__main__":
    main()
