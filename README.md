# NYC Public Schools Test Results – Exploratory Data Analysis

## Project Overview
This project analyzes standardized test results from New York City public schools.It includes a exploratory data analysis, and visualization using Python libraries such as pandas, matplotlib, and seaborn.The goal is to uncover patterns in student performance across boroughs, grades, and demographic groups.

## Contents
```
# NYC_Public_Schools_Test_Results_Data_Analysis/
├── data/                 # CSV files go here
│   └── schools.csv
│
├── notebooks/            # Jupyter notebooks for EDA and testing
│   └── exploratory_analysis.ipynb
│   └── test         
├── src/                  # Source code for analysis
    ├── __init__.py                # Makes src a Python package
    ├── load_data.py               # Functions to load and validate datasets
    ├── clean_data.py              # Cleaning and preprocessing functions
    ├── analyze.py                 # EDA and summary statistics
    ├── visualize.py               # Plotting functions (e.g., seaborn/matplotlib)
    └── utils.py                   # Helper functions (e.g., file paths, formatting)
├── main.py               # Main execution script
├── requirements.txt      # Python dependencies
└── README.txt            # This file
```
## Data Instructions

**1. Visit NYC Open Data portal**
 https://opendata.cityofnewyork.us/

**2. Search and download relevant datasets (e.g., test scores)**

**3. Move the downloaded CSV files into the `data/` directory**
(create the folder if it does not exist)

mkdir -p data/
mv ~/Downloads/*.csv data/

## Data Description
- **schools.csv**  
  Contains school-level test performance for the latest academic year, including:  
  - `school_id`         — Unique identifier for each school  
  - `district`          — NYC school district code  
  - `math_score`        — Average math test score  
  - `reading_score`     — Average reading test score  
  - `attendance_rate`   — Annual attendance percentage  
  - _… plus additional demographic and performance metrics._

## Installation Steps

**1. Clone the repository**
```
git clone https://github.com/elicasagui/NYC_Public_Schools_Test_Results_Data_Analysis.git
cd NYC_Public_Schools_Test_Results_Data_Analysis
```
**2. (Optional) Create and activate a virtual environment**
```
python -m venv venv
```
-On Windows
```
.\venv\Scripts\Activate
```
-On macOS/Linux
```
source venv/bin/activate
```
**If PowerShell’s execution policy is blocking script activation for security reasons**
![image](https://github.com/user-attachments/assets/71539b38-2686-4fe1-99f4-e9dd4dcd2b4c)

**Quick and Safe Fix (temporary for current session only)**

Open PowerShell as Administrator
(Right-click PowerShell → “Run as administrator”).

Run this command to temporarily allow scripts only for this session:
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
Now activate your virtual environment again:
```
.\venv\Scripts\Activate
```
**3. Install required packages**
```
pip install -r requirements.txt
```

**4. Run main script to verify setup**
```
python main.py
```
**5 Launch Jupyter Notebook**
```
jupyter notebook
```

This will open a tab in your browser with an interface where you can navigate to the repository.
![image](https://github.com/user-attachments/assets/7745b2fd-dd66-4c04-b812-3c9874702aeb)


**6 Open and run the notebook**
```
notebooks/exploratory_analysis.ipynb
```
## Proyect Questions
**1.** Which NYC schools have the best math results?

**2.** What are the top 10 performing schools based on the combined SAT scores?

**3.** wich single borough has the largest standard deviation in the combined SAT score?

## Key Insights

**1.** 
- The best math results in NYC schools are:
  
![image](https://github.com/user-attachments/assets/65fa491f-3134-447e-a0ff-d1b0a3c2d129)

**2.** 
- The top 10 performing schools based on the combined SAT scores are: 
![image](https://github.com/user-attachments/assets/a450a10a-be72-40f9-8a4a-dffeed5694b4)

**3.**
- The largest standard deviation in the combined SAT score is:
  ![image](https://github.com/user-attachments/assets/e22e0cbd-35a5-489f-8693-e5ec3dac8d29)


Full analysis available in [exploratory_analysis.ipynb](notebooks/exploratory_analysis.ipynb).

## RUNNING TESTS

 Make sure pytest is installed
 ```
pip install pytest
```

Run tests (if test scripts are provided)
pytest tests/


## Dependencies
Python

pandas

numpy

matplotlib

seaborn

jupyter

(See requirements.txt for exact versions.)

## License
This project from Data Camp scientist's course.

## Contact
For questions or collaboration inquiries, please contact:
Eliecer Castro

– Data Scientist

– elicasagui@gmail.com

– GitHub repository's link: https://github.com/elicasagui/NYC_Public_Schools_Test_Results_Data_Analysis.git
