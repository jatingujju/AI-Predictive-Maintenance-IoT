print("🚀 STARTING PROJECT")

from data_loader import load_data
from preprocess import preprocess_data
from train_model import train_model
from predict import predict_sample
from visualize import plot_temperature


def main():
    print("➡️ Inside main()")

    df = load_data("data/data.csv")
    print("➡️ Data Loaded")

    df = preprocess_data(df)
    print("➡️ Data Preprocessed")

    train_model(df)
    print("➡️ Model Trained")

    predict_sample()

    plot_temperature(df)

    print("✅ DONE")


if __name__ == "__main__":
    print("🔥 MAIN EXECUTING")
    main()