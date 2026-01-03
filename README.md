# Ransomware Detection using ML

This repository contains datasets and Jupyter notebooks used for experimenting with machine learning models to detect ransomware/malware.

Contents
- `Dataset/` — raw CSV data and `sample.py` (simple script to print the CSV head).
- `Model/` — Jupyter notebooks and related assets:
  - [Model/Malware Detection.ipynb](Model/Malware%20Detection.ipynb)
  - [Model/Ransomware Detection using ml.ipynb](Model/Ransomware%20Detection%20using%20ml.ipynb)
  - [Model/Untitled.ipynb](Model/Untitled.ipynb)

Quickstart

1. Create and activate a Python virtual environment (Windows example):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install common dependencies (adjust as needed based on notebook requirements):

```powershell
pip install --upgrade pip
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

3. Open the notebooks with Jupyter Lab/Notebook:

```powershell
jupyter notebook
# then open the notebooks listed under the Model/ folder in your browser
```

4. Run `sample.py` to quickly inspect the dataset:

```powershell
python Dataset\sample.py
```

Notes
- Notebooks may require additional libraries depending on specific cells (e.g., `xgboost` or plotting libraries). If you hit an ImportError, install the missing package and re-run.
- Large datasets or long-running training cells may take time; consider running heavy cells on a machine with sufficient RAM/CPU.

If you'd like, I can:
- run the notebooks programmatically and save executed outputs
- add a `requirements.txt` matching the notebooks
- commit and push any further changes
