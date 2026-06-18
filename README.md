# Pandas + Jupyter + Docker Setup

> Complete Data Engineering Environment with Docker, Pandas, and Jupyter

[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Screenshots](#screenshots)
- [How It Works](#how-it-works)
- [Usage Examples](#usage-examples)
- [Helper Functions](#helper-functions)
- [Running Notebooks](#running-notebooks)
- [Troubleshooting](#troubleshooting)
- [Commands](#commands)
- [Resources](#resources)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This project provides a **complete, production-ready** data engineering environment with:

| Feature | Description |
|---------|-------------|
| Docker | Containerized Jupyter environment |
| Python 3.11 | Latest Python with Conda |
| Pandas 2.0 | Data manipulation library |
| Jupyter Lab | Interactive notebooks |
| VS Code | Full IDE integration |
| Volume Mounts | Perfect file sync with Windows |
| Dev Containers | VS Code inside Docker |

---

## Project Structure

```
py_panda_jupyter_note/
│
├── .devcontainer/
│   └── devcontainer.json          # VS Code Dev Container config
│
├── .vscode/
│   └── settings.json              # VS Code workspace settings
│
├── notebooks/                     # Your Jupyter notebooks
│   ├── 00_test.ipynb             # Test notebook
│   └── 01_analysis.ipynb         # Analysis notebook
│
├── scripts/                       # Reusable Python modules
│   └── utils.py                  # Helper functions
│
├── data/                          # Raw data (gitignored)
├── outputs/                       # Results (gitignored)
├── screenshots/                   # Documentation images
│
├── docker-compose.yml             # Docker configuration
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

---

## Quick Start

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

**Wait 30 seconds** for the container to start...

#### Step 5: Open Jupyter Lab

Open your browser and go to:

```
http://localhost:8888?token=simple123
```

**You're in!**

#### Step 6: Create Your First Notebook

1. In Jupyter, click **New → Python 3**
2. Name it: `00_test.ipynb`
3. Type this:

```python
import pandas as pd
print("Pandas is working!")
print(f"Version: {pd.__version__}")
```

4. Press **Shift+Enter** to run

#### Step 7: VS Code Setup (Perfect Sync)

Open in VS Code:

```
File → Open Folder → F:\py_panda_jupyter_note
```

Create VS Code Settings:

Create `.vscode/settings.json`:

```json
{
    "files.autoSave": "onFocusChange",
    "python.terminal.activateEnvironment": false
}
```

#### Step 8: Helper Script (For Easy Work)

Create `scripts/utils.py`:

```python
# scripts/utils.py
import pandas as pd
import os

DATA_PATH = '/home/jovyan/work/data'
OUTPUT_PATH = '/home/jovyan/work/outputs'

def load_data(filename):
    """Load CSV from data folder"""
    path = f"{DATA_PATH}/{filename}"
    return pd.read_csv(path)

def save_data(df, filename):
    """Save DataFrame to outputs folder"""
    path = f"{OUTPUT_PATH}/{filename}"
    df.to_csv(path, index=False)
    print(f"Saved to: {path}")

def create_sample():
    """Create sample data"""
    import numpy as np
    return pd.DataFrame({
        'id': range(1, 101),
        'name': [f'User_{i}' for i in range(1, 101)],
        'age': np.random.randint(18, 60, 100),
        'score': np.random.uniform(0, 100, 100)
    })
```

#### Step 9: Test Notebook

In Jupyter Notebook, run:

```python
# Cell 1: Setup
import sys
sys.path.append('/home/jovyan/work/scripts')
from utils import *

print("All ready!")

# Cell 2: Create data
df = create_sample()
df.head()

# Cell 3: Save data
save_data(df, 'sample_output.csv')

# Cell 4: Check your files
import os
print("Files in outputs folder:")
for f in os.listdir('/home/jovyan/work/outputs'):
    print(f"  - {f}")
```

#### Step 10: Check Sync

**In VS Code:**
- Click on `outputs` folder
- You'll see `sample_output.csv` instantly!

**In Windows Explorer:**
```
F:\py_panda_jupyter_note\outputs\sample_output.csv
```

**File is there! Full sync!**

#### Step 11: VS Code Dev Container Setup (Optional but Recommended)

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

#### Step 12: Select Python Kernel in VS Code

When you open a `.ipynb` file in VS Code:

1. Look for the kernel picker at the **bottom-right**
2. Click on it
3. Select: **`base (Python 3.11.6) /opt/conda/bin/python`**

**Why choose this kernel?**
- `Python 3.10.12 /usr/bin/python3` → Basic system Python (no pandas)
- `base (Python 3.11.6) /opt/conda/bin/python` → Full data science stack (pandas, numpy, etc.)

**Choose the base kernel!**

---

## Screenshots

### 1. Jupyter Lab Interface

![Jupyter Lab](screenshots/jupyter_notebook.png)

*Jupyter Lab running inside Docker container with Python 3 kernel*

---

## How It Works

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


---

---

## Helper Functions

The `scripts/utils.py` provides these helper functions:

| Function | Description | Example |
|----------|-------------|---------|
| `load_data(filename)` | Load CSV from data folder | `df = load_data('sales.csv')` |
| `save_data(df, filename)` | Save to outputs folder | `save_data(df, 'result.csv')` |
| `create_sample()` | Generate sample data | `df = create_sample()` |
| `create_sales_data(n)` | Generate sales data | `df = create_sales_data(1000)` |

---

## Running Notebooks

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

---

## Troubleshooting

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

## Commands

### Docker Commands Cheat Sheet

| Command | What It Does | When to Use |
|---------|-------------|-------------|
| `docker-compose up -d` | Starts container in background | Daily use |
| `docker-compose down` | Stops container | Daily use |
| `docker-compose logs -f` | Shows container logs | Debugging |
| `docker-compose down --rmi all` | Removes container AND image | Starting fresh |
| `docker-compose down -v` | Deletes ALL volumes | Clean everything |
| `docker ps` | Shows running containers | Check status |
| `docker images` | Shows downloaded images | Check disk space |

---

## Resources

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

## Future Enhancements

- [ ] Add PostgreSQL container
- [ ] Add PySpark support
- [ ] Add Airflow for scheduling
- [ ] Add Great Expectations for data quality
- [ ] Add dbt for transformations

---

