# Student Data Analysis & Visualization (Pandas + Matplotlib)

This project demonstrates basic **data cleaning, feature engineering, and visualization** using **Pandas** and **Matplotlib** on a student marks dataset.

It includes:
- Reading a CSV dataset
- Extracting and saving the first 3 rows to a new CSV file
- Selecting specific rows/columns using `iloc`
- Cleaning mixed-type columns (`Age`, `speech`)
- Dropping invalid rows (NaN / non-numeric values)
- Adding computed columns (`Total`, `Average`, `Subjects_Attempted`)
- Creating visualizations:
  - Bar chart: **Total Marks per Student**
  - Line chart: **Average Score per Subject**

---

## Dataset

The input file contains columns:

- `Student_Name`
- `Age` (contains numeric values and invalid text like `no`)
- `python`
- `math`
- `english`
- `speech` (contains numeric values, `NaN`, and invalid text like `no`)

Example snippet:

| Student_Name | Age  | python | math | english | speech |
|------------|------|--------|------|---------|--------|
| Raj        | 21   | 89     | 82   | 89      | 82     |
| Pritam     | 20   | 88     | 98   | 88      | NaN    |
| Sony       | 22   | 78     | 95   | 78      | no     |

---

## What This Project Does

### 1) Load the dataset
```python
import pandas as pd
df = pd.read_csv("Studenta_data.csv")
