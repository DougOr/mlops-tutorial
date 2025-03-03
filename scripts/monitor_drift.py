import pandas as pd
from evidently.dashboard import Dashboard
from evidently.tabs import DataDriftTab

# Load data
reference_data = pd.read_csv("data/reference_data.csv")
current_data = pd.read_csv("data/current_data.csv")

# Create a DataDrift dashboard
data_drift_dashboard = Dashboard(tabs=[DataDriftTab()])
data_drift_dashboard.calculate(reference_data, current_data, column_mapping=None)

# Save the dashboard as an HTML report
data_drift_dashboard.save("data_drift_report.html")
