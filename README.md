## 📌 Project Objective
The goal of this project is to practice fundamental Pandas operations while developing a **DataFrame-as-a-table mindset**, similar to working with relational databases.

This project focuses on understanding how tabular data behaves in memory and how to inspect, filter, and validate it before applying any transformations.

---

## 📊 Dataset Description
The dataset is a CSV file containing information about gym members, including:
- First name
- Last name
- Age
- Sex
- Height
- Weight
- City
- Hobbies

Each row represents one gym member, and each column represents an attribute.

---

## 🧠 Learning Focus
In this project, I practiced:
- Reading CSV files using Pandas
- Inspecting data structure and schema using:
  - `head()`
  - `info()`
  - `describe()`
- Selecting specific columns (projection)
- Filtering rows based on conditions (selection)
- Identifying missing values and analyzing data quality

---

## ⚠️ Data Quality Observations
- Some columns contain missing values
- Data types were inspected to ensure numerical and categorical fields are correctly represented
- Decisions regarding missing values are documented separately

---

## 📁 Project Structure
01-06-2026/
├── data/
│ └── athletes_raw.csv
├── notebooks/
│ └── day1_exploration.ipynb
├── README.md


---

## 🚀 Next Steps
In the next phase, this dataset will be used to:
- Apply aggregations and group-by operations
- Perform joins and more advanced transformations
