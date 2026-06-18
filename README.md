# 🐍 Pandas + Jupyter + Docker Setup

## 🚀 Complete Data Engineering Environment

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

---

## 📋 What's Inside

- ✅ **Docker** container with Jupyter/datascience-notebook
- ✅ **Pandas** 2.0.3 for data manipulation
- ✅ **Jupyter Lab** with full data science stack
- ✅ **VS Code** integration with Dev Containers
- ✅ **Volume mounts** for perfect file sync
- ✅ **Pre-configured** Python environment

---

## 🏗️ Project Structure
py_panda_jupyter_note/
├── .devcontainer/
│ └── devcontainer.json # VS Code Dev Container config
├── .vscode/
│ └── settings.json # VS Code workspace settings
├── notebooks/ # Your Jupyter notebooks
│ ├── 00_test.ipynb # Test notebook
│ └── 01_analysis.ipynb # Analysis notebook
├── scripts/ # Reusable Python modules
│ └── utils.py # Helper functions
├── data/ # Raw data (gitignored)
├── outputs/ # Results (gitignored)
├── screenshots/ # Documentation images
│ ├── jupyter_lab.png
│ ├── vscode_devcontainer.png
│ ├── example_output.png
│ ├── file_sync.png
│ └── project_structure.png
├── docker-compose.yml # Docker configuration
├── .gitignore # Git ignore rules
└── README.md # This file

text

---

## 🚀 Quick Start

### Prerequisites

- **Docker Desktop** (20.10+) - [Download](https://www.docker.com/products/docker-desktop)
- **VS Code** (1.80+) - [Download](https://code.visualstudio.com/)
- **Git** - [Download](https://git-scm.com/)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/pandas-docker-setup.git
cd pandas-docker-setup
2️⃣ Start the Docker Container
bash
docker-compose up -d
Wait 30 seconds for the container to start...

3️⃣ Open Jupyter Lab
Open your browser and go to:

text
http://localhost:8888?token=simple123
4️⃣ Open in VS Code
bash
code .
Or open VS Code and select: File → Open Folder → py_panda_jupyter_note

📸 Screenshots
Jupyter Lab Interface
https://screenshots/jupyter_lab.png

Jupyter Lab running inside Docker container with Python 3 (ipykernel)

VS Code Dev Container
https://screenshots/vscode_devcontainer.png

VS Code connected to Docker container with "base (Python 3.11.6)" kernel

Example Notebook Output
https://screenshots/example_output.png

Sample notebook showing pandas operations and file saving

File Sync Verification
https://screenshots/file_sync.png

Files syncing between Docker container and Windows host

Complete Project Structure
https://screenshots/project_structure.png

Full project folder structure in VS Code Explorer

🔧 How It Works
Docker Compose Configuration
yaml
version: '3.8'

services:
  jupyter:
    image: jupyter/datascience-notebook:latest
    container_name: pandas_jupyter
    ports:
      - "8888:8888"      # Jupyter
      - "4040:4040"      # For future Spark
    environment:
      - JUPYTER_ENABLE_LAB=yes
      - JUPYTER_TOKEN=simple123
    volumes:
      - ./notebooks:/home/jovyan/work/notebooks
      - ./data:/home/jovyan/work/data
      - ./scripts:/home/jovyan/work/scripts
      - ./outputs:/home/jovyan/work/outputs
    user: root
    command: start.sh jupyter lab
    restart: unless-stopped
Volume Mounts
Host Path	Container Path	Purpose
./notebooks/	/home/jovyan/work/notebooks/	Jupyter notebooks
./data/	/home/jovyan/work/data/	Raw data files
./scripts/	/home/jovyan/work/scripts/	Python modules
./outputs/	/home/jovyan/work/outputs/	Results and exports
Python Environment
Kernel: base (Python 3.11.6) /opt/conda/bin/python

Environment: Conda base with full data science stack

Pre-installed packages:

pandas 2.0.3

numpy 1.24.3

matplotlib 3.7.2

seaborn 0.12.2

scikit-learn 1.3.0

And many more...

💻 Usage Examples
Create Sample Data
python
# Cell 1: Setup
import sys
sys.path.append('/home/jovyan/work/scripts')
from utils import *

print("✅ All ready!")

# Cell 2: Create sample data
df = create_sample()
print("📊 Sample Data:")
df.head()

# Cell 3: Save to outputs folder
save_data(df, 'my_sample_data.csv')
print("✅ Saved!")

# Cell 4: Verify
import os
print("\n📁 Files in outputs:")
for f in os.listdir('/home/jovyan/work/outputs'):
    print(f"  - {f}")
Load and Analyze Data
python
# Load data from data folder
df = load_data('your_data.csv')

# Quick statistics
print("📊 Data Summary:")
print(df.describe())

# Group by and aggregate
summary = df.groupby('category').agg({
    'sales': ['sum', 'mean', 'count']
})

# Save processed data
save_data(summary, 'summary_report.csv')
Complete ETL Pipeline
python
# 1. EXTRACT - Load raw data
df = load_data('raw_sales.csv')

# 2. TRANSFORM - Clean and process
df_clean = df.drop_duplicates()
df_clean['date'] = pd.to_datetime(df_clean['date'])
df_clean = df_clean.fillna(df_clean.mean())

# 3. AGGREGATE - Group and summarize
monthly_sales = df_clean.groupby(
    df_clean['date'].dt.to_period('M')
).agg({
    'sales': 'sum',
    'quantity': 'sum'
})

# 4. LOAD - Save results
save_data(df_clean, 'cleaned_sales.csv')
save_data(monthly_sales, 'monthly_sales_summary.csv')

print("✅ ETL Pipeline Complete!")
🛠️ Helper Functions (scripts/utils.py)
Function	Description	Example
load_data(filename)	Load CSV from data folder	df = load_data('sales.csv')
save_data(df, filename)	Save to outputs folder	save_data(df, 'result.csv')
create_sample()	Generate sample data	df = create_sample()
create_sales_data(n)	Generate sales data	df = create_sales_data(1000)
📝 How to Run Notebooks
Option 1: Web Browser (Jupyter Lab)
Open: http://localhost:8888?token=simple123

Click "New" → "Python 3"

Write code and press Shift+Enter to run

Save notebook in notebooks/ folder

Option 2: VS Code (Recommended)
Open project in VS Code

Open any .ipynb file from notebooks/ folder

Select kernel: base (Python 3.11.6) (bottom-right)

Run cells with Shift+Enter

🚨 Common Issues & Solutions
Issue	Solution
Port 8888 already in use	Change to "8889:8888" in docker-compose.yml
Kernel not found in VS Code	Click bottom-right and select base (Python 3.11.6)
Files not syncing	Check volume mounts in docker-compose.yml
Permission errors	Using user: root resolves this on Windows
Container won't start	Run docker-compose logs to see error details
Can't access Jupyter	Check firewall and ensure Docker is running
🔧 Commands Cheat Sheet
Command	Description
docker-compose up -d	Start container in background
docker-compose down	Stop and remove container
docker-compose logs -f	View container logs
docker exec -it pandas_jupyter bash	Enter container shell
docker-compose up -d --build	Rebuild and start
docker-compose down -v	Remove everything (including volumes)
docker ps	List running containers
docker images	List Docker images
📊 Quick Start Scripts
start.bat (Windows)
batch
@echo off
echo 🚀 Starting Pandas Jupyter...
docker-compose up -d
echo ✅ Running!
echo 🔗 http://localhost:8888?token=simple123
pause
stop.bat (Windows)
batch
@echo off
echo 🛑 Stopping...
docker-compose down
echo ✅ Stopped!
pause
🎯 Project Features
✅ Zero configuration - Just clone and run

✅ Persistent data - All data stays on your host

✅ VS Code integration - Full IDE inside container

✅ Perfect sync - Real-time file synchronization

✅ Ready for production - Enterprise-grade setup

✅ Scalable - Easy to add more services

📚 What You Can Build
ETL Pipelines - Extract, Transform, Load

Data Cleaning - Handle missing values, duplicates

Data Analysis - Group by, aggregation, pivots

Data Visualization - Charts, plots, graphs

File Processing - CSV, Excel, JSON, Parquet

🎓 Learning Resources
Pandas Documentation

Docker Documentation

Jupyter Documentation

VS Code Dev Containers

🏆 Acknowledgments
Jupyter Docker Stacks for the base image

VS Code team for Dev Containers

Pandas team for amazing data tools

📊 Version History
v1.0.0 (2024)

Initial release

Docker + Jupyter + Pandas setup

VS Code Dev Container integration

Complete documentation

🔮 Future Enhancements
Add PostgreSQL container

Add PySpark support

Add Airflow for scheduling

Add Great Expectations for data quality

Add dbt for transformations

Happy Data Engineering! 🚀🐍



Data Quality - Validation and testing
