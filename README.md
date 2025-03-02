---

```markdown
# MLOps Tutorial: Building a CI/CD Pipeline for MNIST Digit Classification

This repository provides a hands-on tutorial for building a **CI/CD pipeline** for MNIST digit classification using **GitHub Actions**, **JFrog Artifactory**, and **JFrog Xray**. The pipeline includes:

- Training a PyTorch model.
- Versioning and storing models in JFrog Artifactory.
- Generating a Software Bill of Materials (SBOM).
- Scanning for vulnerabilities using JFrog Xray.
- Monitoring model and data drift.

---

## Table of Contents
1. [Getting Started](#getting-started)
2. [Step-by-Step Tutorial](#step-by-step-tutorial)
   - [Step 1: Set Up the Environment](#step-1-set-up-the-environment)
   - [Step 2: Train the MNIST Model](#step-2-train-the-mnist-model)
   - [Step 3: Test the Model and Data](#step-3-test-the-model-and-data)
   - [Step 4: Monitor Model and Data Drift](#step-4-monitor-model-and-data-drift)
   - [Step 5: Store the Model in JFrog Artifactory](#step-5-store-the-model-in-jfrog-artifactory)
   - [Step 6: Generate SBOM and Scan for Vulnerabilities](#step-6-generate-sbom-and-scan-for-vulnerabilities)
   - [Step 7: CI/CD Pipeline with GitHub Actions](#step-7-cicd-pipeline-with-github-actions)
3. [Repository Structure](#repository-structure)
4. [Requirements](#requirements)
5. [Additional Setup](#additional-setup)
6. [Contributing](#contributing)
7. [License](#license)

---

## Getting Started

### Prerequisites
- Python 3.9 or higher.
- GitHub account for CI/CD pipeline.
- JFrog Artifactory and Xray account.
- Docker (optional, for local testing).

---

## Step-by-Step Tutorial

### Step 1: Set Up the Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/DougOr/mlops-tutorial.git
   cd mlops-tutorial
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   - On Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

### Step 2: Train the MNIST Model

1. Open the Jupyter Notebook:
   ```bash
   jupyter notebook notebooks/mnist_training.ipynb
   ```

2. Follow the notebook to:
   - Train a PyTorch model on the MNIST dataset.
   - Save the trained model as `mnist_model.pth` in the `models/` directory.

---

### Step 3: Test the Model and Data

#### **Test the Data**
1. Run the data validation tests to ensure the MNIST dataset is correctly loaded and preprocessed:
   ```bash
   python3 tests/test_data_validation.py
   ```

   If the tests pass, you should see output like this:
   ```
   Data shape test passed!
   Data normalization test passed!
   Data labels test passed!
   ```

#### **Test the Model**
2. Run the model performance test to evaluate the trained model's accuracy:
   ```bash
   python3 tests/test_model_performance.py
   ```

   If the model accuracy is above 90%, the test will pass. Otherwise, it will raise an assertion error.

---

### Step 4: Monitor Model and Data Drift

1. **Set Up Drift Detection**:
   - The repository includes a script (`scripts/monitor_drift.py`) to detect data drift using **Evidently.ai**.

2. **Run the Drift Detection Script**:
   ```bash
   python scripts/monitor_drift.py
   ```

   This script compares the reference dataset (baseline) with the current dataset and generates a drift report at `data_drift_report.html`.

3. **Interpret the Drift Report**:
   - Open `data_drift_report.html` in your browser.
   - The report highlights features with significant drift and provides statistical insights.

4. **Automate Drift Detection**:
   - Integrate drift detection into your CI/CD pipeline by adding a step in `.github/workflows/ci-cd-pipeline.yml`.

---

### Step 5: Store the Model in JFrog Artifactory

1. **Set Up JFrog Artifactory**:
   - Log in to your JFrog Artifactory account.
   - Create a new repository (e.g., `mlops-models`) to store and version the trained model.

2. **Install the JFrog CLI**:
   - Download and install the JFrog CLI from [here](https://jfrog.com/getcli/).

3. **Configure the JFrog CLI**:
   ```bash
   jfrog c add
   ```
   - Follow the prompts to configure your Artifactory instance.

4. **Upload the Model to Artifactory**:
   ```bash
   jfrog rt upload models/mnist_model.pth mlops-models/mnist_model_v1.pth
   ```

   Append a version tag (e.g., `v1`, `v2`) to the filename for versioning.

5. **Retrieve a Specific Model Version**:
   ```bash
   jfrog rt download mlops-models/mnist_model_v1.pth
   ```

---

### Step 6: Generate SBOM and Scan for Vulnerabilities

1. Generate a Software Bill of Materials (SBOM):
   ```bash
   python scripts/generate_sbom.py
   ```

2. **Upload the SBOM to JFrog Artifactory**:
   ```bash
   jfrog rt upload sbom.json mlops-models/sbom.json
   ```

3. **Scan for Vulnerabilities with JFrog Xray**:
   - In the JFrog Artifactory UI, navigate to the `mlops-models` repository.
   - Use JFrog Xray to scan the uploaded SBOM for vulnerabilities.

---

### Step 7: CI/CD Pipeline with GitHub Actions

The CI/CD pipeline is defined in `.github/workflows/ci-cd-pipeline.yml`. It automates:
- Training the model.
- Uploading the model to JFrog Artifactory.
- Generating the SBOM.
- Scanning for vulnerabilities.
- Monitoring model and data drift.

#### **How to Use the Pipeline**
1. Push your code to the `main` branch.
2. GitHub Actions will automatically trigger the pipeline.

---

## Repository Structure

```
mlops-tutorial/
├── README.md
├── requirements.txt
├── data/
│   ├── reference_data.csv
│   └── current_data.csv
├── notebooks/
│   ├── mnist_training.ipynb
│   └── mnist_training_colab.ipynb
├── scripts/
│   ├── train_model.py
│   ├── monitor_drift.py
│   ├── deploy_model.py
│   └── generate_sbom.py
├── models/
│   └── mnist_model.pth
├── tests/
│   ├── test_data_validation.py
│   └── test_model_performance.py
├── .github/
│   └── workflows/
│       └── ci-cd-pipeline.yml
└── docs/
    └── mlops_workflow.md
```

---

## Requirements

The `requirements.txt` file includes the following dependencies:

```plaintext
torch==2.2.0
torchvision==0.17.0
evidently==0.3.0
pandas==2.0.3
scikit-learn==1.3.0
jupyter==1.0.0
```

---

## Additional Setup

### Install Syft for SBOM Generation

`syft` is a CLI tool used to generate Software Bill of Materials (SBOM). It is not a Python package, so it must be installed separately.

#### On Linux/Mac
1. Run the following command to install `syft`:
   ```bash
   curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin
   ```

2. Verify the installation:
   ```bash
   syft --version
   ```

#### On Windows
1. Download the latest release of `syft` from the [Syft GitHub releases page](https://github.com/anchore/syft/releases).
2. Extract the binary and add it to your system's PATH.

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

---
