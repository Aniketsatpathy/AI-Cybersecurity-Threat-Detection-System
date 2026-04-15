# 🛡️ AI-Powered Cybersecurity Threat Detection System

**Real-time Anomaly Detection using Machine Learning & SOC Dashboard**

---

## 📋 Overview

An advanced AI-based cybersecurity system designed to detect cyber threats in network traffic using machine learning algorithms and real-time anomaly detection. This system leverages ensemble methods to identify suspicious patterns and unknown threats that traditional security systems often miss.

**Primary Use Cases:**
- Security Operations Centers (SOC)
- Network traffic monitoring
- Banking and financial security
- Cloud infrastructure protection
- Real-time threat detection and alerting

---

## 🎯 Problem Statement

Traditional signature-based security systems struggle with zero-day attacks and novel threats. This project solves that challenge by:

- ✅ Detecting **unknown threats** using unsupervised learning
- ✅ Identifying **anomalous patterns** in network traffic
- ✅ Providing **real-time alerts** with high accuracy (~98%)
- ✅ Visualizing threats through an interactive **SOC dashboard**

---

## 💻 Tech Stack

| Category | Technologies |
|----------|--------------|
| **Language** | Python (90.9%), C++ (4.5%), Cython (3.8%) |
| **Data Processing** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn, Isolation Forest, Random Forest |
| **Visualization** | Matplotlib, Streamlit |
| **Dashboard** | Streamlit (Real-time Web UI) |

---

## 🧠 Machine Learning Models

- **Isolation Forest** - Unsupervised anomaly detection
- **Random Forest** - Supervised classification with 98% accuracy

---

## 🏗️ Architecture
Raw Network Traffic 
↓ 
Data Loading 
↓ 
Preprocessing (Cleaning, Encoding, Normalization) 
↓ 
Feature Engineering (Extraction, Selection, Scaling)
↓ 
Model Training (IF & RF) 
↓ 
Real-time Predictions 
↓ 
Visualization & SOC Dashboard


---

## 📊 Dataset

- **UNSW-NB15**: Comprehensive network security dataset
- Contains normal and attack traffic samples
- Used for training and validation

---

## ⚙️ Installation

# Clone the repository
git clone https://github.com/Aniketsatpathy/AI-Cybersecurity-Threat-Detection-System.git
cd AI-Cybersecurity-Threat-Detection-System

# Install dependencies
pip install -r requirement.txt

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

▶️ How to Run

Train the Model
python main.py

Trains both Isolation Forest and Random Forest models on the UNSW-NB15 dataset.

Launch the SOC Dashboard
streamlit run dashboard/app.py

Opens interactive dashboard at http://localhost:8501

Run Tests
python test.py

📈 Model Performance
Metric	Random Forest	Isolation Forest
Accuracy	~98%	~95%
Detection Type	Supervised	Unsupervised
Use Case	Known threats	Unknown threats


🎨 Features
✨ Real-time Threat Detection

Live network traffic analysis
Instant anomaly detection and flagging
📊 Interactive SOC Dashboard

Real-time metrics and KPIs
Visual threat indicators
Network traffic visualization
📝 Live Logs & Alerting

Real-time event feed
Threat severity indicators
Detailed anomaly reports
🔍 Risk Assessment

Risk scoring for each connection
Threat classification and categorization
🎓 Learning Outcomes
Upon completing this project, you'll understand:

✅ End-to-end ML pipeline development
✅ Data preprocessing and feature engineering techniques
✅ Anomaly detection algorithms (Isolation Forest, Random Forest)
✅ Building production-ready dashboards
✅ Real-world error handling and edge cases
✅ Deployment considerations for security systems

📌 Future Improvements
🚀 Real-time Streaming: Apache Kafka/Spark integration
🔌 API Deployment: FastAPI/Flask REST endpoints
📱 Mobile Alerts: Push notifications for critical threats
🤖 Deep Learning: LSTM/GRU models for sequential patterns
☁️ Cloud Scaling: AWS/Azure/GCP deployment


🗓️ Development Timeline

Day	Task	Details
1️⃣	Setup	Project structure, requirements.txt, git initialization
2️⃣	Dataset	Load UNSW-NB15 data, exploratory analysis
3️⃣	Preprocessing	Data cleaning, encoding, normalization
4️⃣	Models	Isolation Forest & Random Forest implementation
5️⃣	Evaluation	Metrics, confusion matrices, ROC curves
6️⃣	Visualization	Analysis graphs, anomaly distribution plots
7️⃣	Dashboard	Streamlit UI, real-time SOC interface
📸 Project Proof & Visualizations
1. Dataset Preview
Shows the first records and statistics of the UNSW-NB15 dataset ![Dataset Preview](https://github.com/Aniketsatpathy/AI-Cybersecurity-Threat-Detection-System/raw/main/images/Dataset_Preview.png)

2. Preprocessed Data
Cleaned and normalized data ready for model training ![Preprocessed Data](https://github.com/Aniketsatpathy/AI-Cybersecurity-Threat-Detection-System/raw/main/images/preprocessed_data.png)

3. Random Forest Model Evaluation
Performance metrics and classification results for RF model ![Random Forest Evaluation](https://github.com/Aniketsatpathy/AI-Cybersecurity-Threat-Detection-System/raw/main/images/Random_Forest_Evaluation.png)

4. Isolation Forest Model Evaluation
Performance metrics for unsupervised anomaly detection ![Isolation Forest Evaluation](https://github.com/Aniketsatpathy/AI-Cybersecurity-Threat-Detection-System/raw/main/images/Isolation_Forest_Evaluation.png)

5. Confusion Matrix - Random Forest
Classification performance visualization ![Random Forest Confusion Matrix](https://github.com/Aniketsatpathy/AI-Cybersecurity-Threat-Detection-System/raw/main/images/confusion_rf.png)

6. Confusion Matrix - Isolation Forest
Anomaly detection performance visualization ![Isolation Forest Confusion Matrix](https://github.com/Aniketsatpathy/AI-Cybersecurity-Threat-Detection-System/raw/main/images/confusion_iso.png)

7. Anomaly Distribution Graph
Distribution of detected anomalies across network traffic ![Anomaly Distribution](https://github.com/Aniketsatpathy/AI-Cybersecurity-Threat-Detection-System/raw/main/images/Anomaly_Distribution_graph.png)

8. SOC Dashboard Interface
Real-time threat detection and monitoring dashboard ![Dashboard UI](https://github.com/Aniketsatpathy/AI-Cybersecurity-Threat-Detection-System/raw/main/images/Dashboard_UI.png)

9. Live Logs & SOC Feed
Real-time event stream and threat alerts ![Live Logs](https://github.com/Aniketsatpathy/AI-Cybersecurity-Threat-Detection-System/raw/main/images/Live_Logs_UI.png)

🎥 Demo Video
Watch the dashboard in action: Dashboard Demo Video

👨‍💻 Author
Aniket Satpathy

GitHub: @Aniketsatpathy
Project: AI Cybersecurity Threat Detection System

📄 License
This project is open-source and available under the MIT License.

🤝 Contributing
Contributions are welcome! Please feel free to:

Report issues and bugs
Suggest improvements and new features
Submit pull requests

📚 Additional Resources
UNSW-NB15 Dataset Paper
Scikit-learn Documentation
Streamlit Documentation


Last Updated: 2026-04-15
