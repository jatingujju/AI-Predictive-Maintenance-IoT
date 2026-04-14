import matplotlib.pyplot as plt

def plot_temperature(df):
    print("📊 Plotting Graph...")

    plt.figure()
    plt.plot(df['temperature'])
    plt.title("Temperature Trend")
    plt.xlabel("Index")
    plt.ylabel("Temperature")

    plt.savefig("temperature.png")
    plt.show()

    print("✅ Graph Saved!")