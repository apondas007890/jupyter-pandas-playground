# 🐍 Pandas + Jupyter + Docker Setup

> Complete Data Engineering Environment with Docker, Pandas, and Jupyter

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)

---

## 📑 Table of Contents

- [📋 Overview](#-overview)
- [📁 Project Structure](#-project-structure)
- [🚀 Quick Start](#-quick-start)
- [📸 Screenshots](#-screenshots)
- [🔧 How It Works](#-how-it-works)
- [💻 Usage Examples](#-usage-examples)
- [🛠️ Helper Functions](#️-helper-functions)
- [📝 Running Notebooks](#-running-notebooks)
- [🚨 Troubleshooting](#-troubleshooting)
- [🔧 Commands](#-commands)
- [📚 Resources](#-resources)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 📋 Overview

This project provides a **complete, production-ready** data engineering environment with:

| Feature | Description |
|---------|-------------|
| 🐳 **Docker** | Containerized Jupyter environment |
| 🐍 **Python 3.11** | Latest Python with Conda |
| 📊 **Pandas 2.0** | Data manipulation library |
| 📓 **Jupyter Lab** | Interactive notebooks |
| 💻 **VS Code** | Full IDE integration |
| 🔄 **Volume Mounts** | Perfect file sync with Windows |
| 🚀 **Dev Containers** | VS Code inside Docker |

---

## 📁 Project Structure

```
py_panda_jupyter_note/
│
├── 📁 .devcontainer/
│   └── devcontainer.json          # VS Code Dev Container config
│
├── 📁 .vscode/
│   └── settings.json              # VS Code workspace settings
│
├── 📁 notebooks/                  # 📓 Your Jupyter notebooks
│   ├── 00_test.ipynb             # Test notebook
│   └── 01_analysis.ipynb         # Analysis notebook
│
├── 📁 scripts/                    # 🛠️ Reusable Python modules
│   └── utils.py                  # Helper functions
│
├── 📁 data/                       # 📂 Raw data (gitignored)
├── 📁 outputs/                    # 📤 Results (gitignored)
├── 📁 screenshots/                # 📸 Documentation images
│
├── 📄 docker-compose.yml          # Docker configuration
├── 📄 .gitignore                  # Git ignore rules
└── 📄 README.md                   # This file
```

---

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have these installed:

| Tool | Version | Download |
|------|---------|----------|
| Docker Desktop | 20.10+ | [Download](https://www.docker.com/products/docker-desktop) |
| VS Code | 1.80+ | [Download](https://code.visualstudio.com/) |
| Git | Latest | [Download](https://git-scm.com/) |

---

### Step-by-Step Setup

#### Step 1: Create Project Folder

```bash
# Windows (any drive)
F:
cd F:\
mkdir py_panda_jupyter_note
cd py_panda_jupyter_note
```

#### Step 2: Create docker-compose.yml

Create `F:\py_panda_jupyter_note\docker-compose.yml`:

```yaml
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
```

#### Step 3: Create Folders

```bash
# In F:\py_panda_jupyter_note\
mkdir notebooks
mkdir data
mkdir scripts
mkdir outputs
```

#### Step 4: Start Docker Container

```bash
docker-compose up -d
```

⏳ **Wait 30 seconds** for the container to start...

#### Step 5: Open Jupyter Lab

Open your browser and go to:
```
http://localhost:8888?token=simple123
```

🎉 **You're in!**

#### Step 6: Create Your First Notebook

1. In Jupyter, click **New → Python 3**
2. Name it: `00_test.ipynb`
3. Type this:

```python
import pandas as pd
print("✅ Pandas is working!")
print(f"Version: {pd.__version__}")
```

4. Press **Shift+Enter** to run

---

## 📸 Screenshots

### 1. Jupyter Lab Interface

![Jupyter Lab](screenshots/jupyter_lab.png)

*Jupyter Lab running inside Docker container with Python 3 kernel*

---

### 2. VS Code Dev Container

![VS Code Dev Container](screenshots/vscode_devcontainer.png)

*VS Code connected to Docker container*

---

### 3. Example Notebook Output

![Example Output](screenshots/example_output.png)

*Sample notebook showing pandas operations*

---

### 4. File Sync Verification

![File Sync](screenshots/file_sync.png)

*Files syncing between Docker container and Windows host*

---

### 5. Complete Project Structure

![Project Structure](screenshots/project_structure.png)

*Full project folder structure in VS Code*

---

## 🔧 How It Works

### Volume Mounts

| Host Path | Container Path | Purpose |
|-----------|---------------|---------|
| `./notebooks/` | `/home/jovyan/work/notebooks/` | Jupyter notebooks |
| `./data/` | `/home/jovyan/work/data/` | Raw data files |
| `./scripts/` | `/home/jovyan/work/scripts/` | Python modules |
| `./outputs/` | `/home/jovyan/work/outputs/` | Results and exports |

### Python Environment

| Component | Value |
|-----------|-------|
| **Kernel** | `base (Python 3.11.6) /opt/conda/bin/python` |
| **Environment** | Conda base with full data science stack |
| **Image** | `jupyter/datascience-notebook:latest` |

### Pre-installed Packages

```
✅ pandas 2.0.3
✅ numpy 1.24.3
✅ matplotlib 3.7.2
✅ seaborn 0.12.2
✅ scikit-learn 1.3.0
✅ and many more...
```

---

## 💻 Usage Examples

### Example 1: Create and Save Sample Data

```python
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
```

### Example 2: Load and Analyze Data

```python
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
```

### Example 3: Complete ETL Pipeline

```python
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
```

---

## 🛠️ Helper Functions

The `scripts/utils.py` provides these helper functions:

| Function | Description | Example |
|----------|-------------|---------|
| `load_data(filename)` | Load CSV from data folder | `df = load_data('sales.csv')` |
| `save_data(df, filename)` | Save to outputs folder | `save_data(df, 'result.csv')` |
| `create_sample()` | Generate sample data | `df = create_sample()` |
| `create_sales_data(n)` | Generate sales data | `df = create_sales_data(1000)` |

---

## 📝 Running Notebooks

### Option 1: Web Browser (Jupyter Lab)

1. Open: `http://localhost:8888?token=simple123`
2. Click **"New"** → **"Python 3"**
3. Write code and press **Shift+Enter** to run
4. Save notebook in `notebooks/` folder

### Option 2: VS Code (Recommended)

1. Open project in VS Code
2. Open any `.ipynb` file from `notebooks/` folder
3. Select kernel: **`base (Python 3.11.6)`** (bottom-right)
4. Run cells with **Shift+Enter**

### VS Code Dev Container Setup

Create `.devcontainer/devcontainer.json`:

```json
{
    "name": "Pandas Jupyter Dev Container",
    "dockerComposeFile": "../docker-compose.yml",
    "service": "jupyter",
    "workspaceFolder": "/home/jovyan/work",
    "customizations": {
        "vscode": {
            "extensions": [
                "ms-python.python",
                "ms-toolsai.jupyter"
            ]
        }
    }
}
```

Then:
1. Open Command Palette (`Ctrl+Shift+P`)
2. Select: **"Dev Containers: Reopen in Container"**

---

## 🚨 Troubleshooting

### Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| **Port 8888 already in use** | Change to `"8889:8888"` in docker-compose.yml |
| **Kernel not found in VS Code** | Click bottom-right and select `base (Python 3.11.6)` |
| **Files not syncing** | Check volume mounts in docker-compose.yml |
| **Permission errors** | Using `user: root` resolves this on Windows |
| **Container won't start** | Run `docker-compose logs` to see error details |
| **Can't access Jupyter** | Check firewall and ensure Docker is running |

---

## 🔧 Commands

### Docker Commands

```bash
# Start container in background
docker-compose up -d

# Stop and remove container
docker-compose down

# View container logs
docker-compose logs -f

# Enter container shell
docker exec -it pandas_jupyter bash

# Rebuild and start
docker-compose up -d --build

# Remove everything (including volumes)
docker-compose down -v

# List running containers
docker ps

# List Docker images
docker images
```

### Quick Start Scripts

**start.bat** (Windows):
```batch
@echo off
echo 🚀 Starting Pandas Jupyter...
docker-compose up -d
echo ✅ Running!
echo 🔗 http://localhost:8888?token=simple123
pause
```

**stop.bat** (Windows):
```batch
@echo off
echo 🛑 Stopping...
docker-compose down
echo ✅ Stopped!
pause
```

---

## 📚 Resources

### Official Documentation

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Docker Documentation](https://docs.docker.com/)
- [Jupyter Documentation](https://jupyter.org/documentation)
- [VS Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers)

### Docker Image

```bash
# The image used in this project
jupyter/datascience-notebook:latest
```

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

MIT License - Free to use and modify for any purpose.

---

## 🌟 Show Your Support

If this project helped you, please give it a ⭐️ on GitHub!

---

## 📞 Questions?

- Open an issue on GitHub
- Contact via GitHub Discussions

---

## 🔮 Future Enhancements

- [ ] Add PostgreSQL container
- [ ] Add PySpark support
- [ ] Add Airflow for scheduling
- [ ] Add Great Expectations for data quality
- [ ] Add dbt for transformations

---

**Happy Data Engineering! 🚀🐍**

---

*Made with ❤️ for the data engineering community*
```

---

## 🎯 **Key Improvements Made:**

| Improvement | Before | After |
|-------------|--------|-------|
| **Organization** | Messy, no structure | ✅ Table of Contents, clear sections |
| **Code Blocks** | Inconsistent | ✅ All properly formatted |
| **Screenshots** | Just links | ✅ Proper image placeholders |
| **Tables** | Scattered info | ✅ Clean, organized tables |
| **Step-by-Step** | Confusing | ✅ Numbered, clear steps |
| **Visuals** | Lacking | ✅ Emojis, badges, separators |

---

## 📸 **To Add Screenshots:**

Create `screenshots/` folder and add:
- `jupyter_lab.png` - Jupyter Lab interface
- `vscode_devcontainer.png` - VS Code in Dev Container
- `example_output.png` - Notebook output
- `file_sync.png` - File sync verification
- `project_structure.png` - Project structure in VS Code

---

**Copy and paste this README - it's professional, organized, and complete!** 🎉
