# NYC Public Schools Test Results – Exploratory Data Analysis

## Project Overview
This repository contains an end-to-end exploratory data analysis (EDA) of standardized test results for New York City public schools. As a Data Scientist, the goal of this project is to uncover trends, identify strengths and weaknesses across districts, and generate actionable insights to inform educational stakeholders.

## Contents
```
Data-Analysis-/
├── data/
│   └── schools.csv
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── requirements.txt
│
└── README.md
```

## Data Description
- **schools.csv**  
  Contains school-level test performance for the latest academic year, including:  
  - `school_id`         — Unique identifier for each school  
  - `district`          — NYC school district code  
  - `math_score`        — Average math test score  
  - `reading_score`     — Average reading test score  
  - `attendance_rate`   — Annual attendance percentage  
  - _… plus additional demographic and performance metrics._

## Setup & Installation

1. **Install dependencies**

pip install -r requirements.txt
## How to Run
2. **Launch Jupyter Notebook**

jupyter notebook

3. **Open** notebooks/exploratory_analysis.ipynb

4. **Execute all cells** to reproduce data cleaning, analysis, and visualization steps.

**Analysis Highlights**
**Data Cleaning & Validation**

Handled missing values and outliers

Standardized district codes and school names

**Exploratory Visualizations**

Distributions of math and reading performance

Attendance vs. test scores correlation

District-level comparison using boxplots and heatmaps

**Key Findings**

Districts X and Y exhibit the highest reading score variability

Positive correlation (r ≈ 0.65) between attendance rate and overall performance

Underperforming schools share common demographic characteristics

**Reproducibility & Extensibility**
All data processing and visualization code is contained in the notebook.

To adapt this analysis to future years or different metrics, replace data/schools.csv with the updated dataset and rerun the notebook.

**Dependencies**
Python 3.8+

pandas

numpy

matplotlib

seaborn

jupyter

(See requirements.txt for exact versions.)

**License**
This project from Data Camp scientist's course.

**Contact**
For questions or collaboration inquiries, please contact:
Eliecer Castro

– Data Scientist

– elicasagui@gmail.com

– GitHub: https://github.com/elicasagui/Data-Analysis-.git
