@echo off
echo Creating virtual environment...
python -m venv venv
call venv\Scripts\activate

echo Installing requirements...
pip install -r requirements.txt

echo Launching Jupyter Notebook...
jupyter notebook notebooks\exploratory_analysis.ipynb

