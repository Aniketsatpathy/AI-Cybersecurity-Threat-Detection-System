# src/evaluate.py

from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate(y_true, y_pred):
    print("\n📊 Evaluation Report:\n")
    print(classification_report(y_true, y_pred))

    # 🔥 Confusion Matrix
    cm = confusion_matrix(y_true, y_pred)

    plt.figure()
    sns.heatmap(cm, annot=True, fmt='d')
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()