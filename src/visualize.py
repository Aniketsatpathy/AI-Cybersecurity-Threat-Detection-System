# src/visualize.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(preds):
    plt.figure()
    sns.countplot(x=preds)
    plt.title("Normal vs Anomaly")
    plt.xlabel("Class (0 = Normal, 1 = Anomaly)")
    plt.ylabel("Count")
    plt.show()