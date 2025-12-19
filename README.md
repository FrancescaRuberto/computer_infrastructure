# Computer Infrastructure

This repository has been created for the **Computer Infrastructure** course. Its primary purpose is to **collect assigned assessments**, showcasing practical implementations and exercises completed throughout the course.

This repository contains a set of practical exercises focused on data collection and analysis. It also demonstrates the use of cloud-based development environments and basic automation to run data analysis tasks on a scheduled basis.

---

## ⚙️ Setup Instructions

To ensure accessibility and consistency across different environments, I chose to use **GitHub Codespaces** for this project.  
Codespaces allows development directly in the cloud, from **any device**, without the need for a specific local setup — an advantage that promotes productivity and flexibility.

### Steps to Set Up and Run

1. **Open the repository** in GitHub.  
2. Click on the **“Code”** button and select the **“Codespaces”** tab.  
3. Choose **“Create codespace on main”** (or the relevant branch).  
4. Once the Codespace environment is ready, you can:
   - Run the notebooks or scripts directly in the integrated terminal.
   - Install additional dependencies if needed using:
     ```bash
     pip install -r requirements.txt
     ```
5. All necessary **data files** and **notebooks** are organized within the repository folders for straightforward execution.

---

## 📁 Repository Structure

This repository is organized to provide a clean and reproducible workflow for solving the assigned problems and generating visual analyses:

- **`.gitignore`** – Configured to exclude unnecessary files and keep the repository clean.  
- **`requirements.txt`** – Lists all dependencies needed to run the notebook and scripts:  
  `yfinance`, `ipython`, `numpy`, `scipy`, `matplotlib`, `pandas`, `seaborn`  
- **`notebook.ipynb`** – A Jupyter Notebook containing all solved problems, with the code split into clear sections and enriched with explanatory comments and resources for each problem.  
- **`data/`** – Stores CSV files containing the last 5 days of data for the five FAANG stocks.  
- **`plots/`** – Contains the generated plots. Each plot shows the Close prices of the five FAANG stocks on a single figure. Plots are saved with filenames in the format `YYYYMMDD-HHmmss.png`.
- **`.github/workflows/`** – Contains the GitHub Actions workflow (faang.yml), which automates the execution of the faang.py script every Saturday morning.

---

## Data Handling

All data used in this project is downloaded programmatically using the `yfinance` package. No external datasets need to be manually downloaded.

Generated CSV files and plots are stored locally within the repository structure for transparency and reproducibility.

---

## Reproducibility and Environment

The project is designed to be fully reproducible. All dependencies are explicitly listed in `requirements.txt`, and the same execution environment is used locally, in GitHub Codespaces, and within GitHub Actions workflows.


