
# 🧬 GENE EXPRESSION BY PATIENTS

### 🔬 A Python-Based Computational Biology & Gene Expression Analysis Project

**Gene Expression by Patients** is a Python-based Computational Biology project designed to analyze the expression levels of multiple genes across different patients.

The project analyzes **BRCA1, TP53, and EGFR** gene expression values and demonstrates how biological data can be transformed from **Python dictionaries → Lists → NumPy 2D Arrays → Pandas DataFrames** for systematic analysis.

It also performs patient-level and gene-level analysis and generates **4 professional visualizations** using Matplotlib and Seaborn.

---

# 🎯 PROJECT OBJECTIVES

- 🧬 Analyze gene expression data for multiple patients.
- 📊 Calculate mean expression by gene.
- 👥 Calculate mean expression by patient.
- 🔢 Convert biological data into NumPy arrays.
- 🐼 Create and analyze Pandas DataFrames.
- 📈 Perform `groupby()` and `agg()` analysis.
- 🔍 Identify highest and lowest gene expression.
- 🔥 Visualize gene expression patterns.
- 🧠 Interpret the results from a Computational Biology perspective.

---

# 🧬 GENES ANALYZED

The project analyzes three genes:

| Gene | Biological Role |
|---|---|
| **BRCA1** | Involved in DNA damage response and repair |
| **TP53** | Important tumor-suppressor gene involved in cell-cycle regulation |
| **EGFR** | Involved in cell signaling, growth, and proliferation |

> **Note:** The values used in this project are example values for programming and Computational Biology practice. They are not clinical or diagnostic measurements.

---

# 👥 PATIENT DATA

The project contains gene-expression values for four example patients:

```python
patients = {

    "Ali": {"BRCA1": 45, "TP53": 67, "EGFR": 32},

    "Sara": {"BRCA1": 78, "TP53": 54, "EGFR": 81},

    "Ahmad": {"BRCA1": 56, "TP53": 72, "EGFR": 44},

    "Ayesha": {"BRCA1": 89, "TP53": 61, "EGFR": 76}

}

Each patient contains expression values for:

BRCA1
TP53
EGFR
🔄 DATA TRANSFORMATION

The project follows this workflow:

PATIENT GENE DATA
       ↓
PYTHON DICTIONARY
       ↓
LIST
       ↓
NUMPY 2D ARRAY
       ↓
MEAN ANALYSIS
       ↓
PANDAS DATAFRAME
       ↓
GROUPBY + AGG
       ↓
HIGH / LOW EXPRESSION ANALYSIS
       ↓
VISUALIZATION
       ↓
BIOLOGICAL INTERPRETATION
🔢 NUMPY ANALYSIS

The project converts gene-expression values into a NumPy 2D array.

gene_array = np.array(result)

The resulting array has the shape:

(4, 3)

Meaning:

4 Patients × 3 Genes
Mean Expression By Gene
mean_by_gene = np.mean(
    gene_array,
    axis=0
)

This calculates the average expression of each gene across all patients.

Mean Expression By Patient
patient_mean = np.mean(
    gene_array,
    axis=1
)

This calculates the average expression of the three genes for each patient.

🐼 PANDAS DATAFRAME

The NumPy array is converted into a Pandas DataFrame:

dataframe = pd.DataFrame(

    gene_array,

    columns=["BRCA1", "TP53", "EGFR"]

)

Patient names are then inserted into the DataFrame.

The resulting structure is:

Patients	BRCA1	TP53	EGFR
Ali	45	67	32
Sara	78	54	81
Ahmad	56	72	44
Ayesha	89	61	76
📊 GENE ANALYSIS USING GROUPBY & AGG

The project uses Pandas groupby() and agg():

gene_analysis = dataframe.groupby(
    "patients"
)[["BRCA1", "TP53", "EGFR"]].agg(
    ["mean", "min", "max"]
)

This generates:

Mean expression
Minimum expression
Maximum expression

for the analyzed patient data.

🔍 HIGH & LOW GENE EXPRESSION

The program automatically identifies the patients with the highest and lowest expression for each gene.

for gene in genes:

    high_patients = dataframe.loc[
        dataframe[gene].idxmax(),
        "patients"
    ]

    high_values = dataframe[gene].max()

    low_patients = dataframe.loc[
        dataframe[gene].idxmin(),
        "patients"
    ]

    low_values = dataframe[gene].min()

This makes the analysis automatic rather than manually checking every value.

📈 DATA VISUALIZATION

The project contains 4 visualizations.

1. 📊 Gene Expression By Patient

A grouped bar chart compares:

BRCA1
TP53
EGFR

across all patients.

This allows direct comparison of gene-expression profiles between patients.

2. 📊 Mean Expression By Gene

A bar chart displays the average expression of:

BRCA1
TP53
EGFR

across all patients.

This helps identify the gene with the highest average expression in the example dataset.

3. 📊 Mean Expression By Patient

This visualization displays the average expression of all three genes for each patient.

It provides a simple overview of overall gene-expression levels across patients.

4. 🔥 Gene Expression Heatmap

A Seaborn heatmap visualizes:

Patients × Genes × Expression Values

using color intensity.

sns.heatmap(
    heatmap_data,
    annot=True,
    fmt=".0f",
    cmap="viridis"
)

The heatmap provides a quick visual overview of gene-expression patterns.

🖼️ PROJECT VISUALIZATION

The project includes a professional visualization image containing:

INPUT CODE
      ↓
PROGRAM OUTPUT
      ↓
ANALYSIS
      ↓
VISUALIZATION CODE
      ↓
4 VISUALIZATION GRAPHS
      ↓
BIOLOGICAL INSIGHTS

Add the project image to your repository and display it in the README:

![Gene Expression By Patients](gene_expression_by_patients.png)
🧠 BIOLOGICAL INSIGHTS

Based on the example dataset:

BRCA1 shows its highest expression in Ayesha.
TP53 shows its highest expression in Ahmad.
EGFR shows its highest expression in Sara.
The heatmap provides an easy visual comparison of gene-expression patterns.
Mean expression provides a simple summary of overall gene-expression levels.
Different patients show different expression profiles across the three genes.

Important: These values are example data for educational purposes. Gene-expression values alone cannot be used to diagnose disease or make clinical decisions.

🛠️ TECHNOLOGIES USED
Technology	Purpose
🐍 Python	Core programming
🔢 NumPy	Numerical calculations and 2D arrays
🐼 Pandas	DataFrames and data analysis
📊 Matplotlib	Bar-chart visualization
🎨 Seaborn	Heatmap visualization
📦 INSTALLATION

Clone the repository:

git clone YOUR_REPOSITORY_URL

Move into the project directory:

cd Gene-Expression-By-Patients

Install the required libraries:

pip install numpy pandas matplotlib seaborn
▶️ HOW TO RUN

Run the Python file:

python gene_expression_by_patients.py

The program will:

1. Display patient data
2. Convert dictionary into a list
3. Create NumPy 2D array
4. Calculate mean expression by gene
5. Calculate mean expression by patient
6. Create Pandas DataFrame
7. Perform groupby & aggregation
8. Find high/low gene expression
9. Generate 4 visualizations
10. Complete the analysis
📂 PROJECT STRUCTURE
Gene-Expression-By-Patients/
│
├── gene_expression_by_patients.py
│
├── gene_expression_by_patients.png
│
├── requirements.txt
│
└── README.md
📄 REQUIREMENTS

Create a requirements.txt file containing:

numpy
pandas
matplotlib
seaborn

Install all dependencies:

pip install -r requirements.txt
🧠 PYTHON CONCEPTS PRACTICED

This project demonstrates:

Dictionaries
Nested Dictionaries
Lists
For Loops
Functions
NumPy Arrays
2D Arrays
Array Shape
Mean Calculation
Pandas DataFrames
DataFrame Insert
Groupby
Aggregation
Indexing
Maximum & Minimum
Matplotlib
Seaborn
Heatmaps
Data Visualization
🔬 COMPUTATIONAL BIOLOGY VALUE

This project demonstrates how biological measurements can be converted into structured computational data.

The complete workflow is:

BIOLOGICAL DATA
      ↓
DATA STRUCTURE
      ↓
NUMERICAL REPRESENTATION
      ↓
STATISTICAL ANALYSIS
      ↓
DATAFRAME
      ↓
COMPARISON
      ↓
VISUALIZATION
      ↓
BIOLOGICAL INTERPRETATION

This provides a foundation for working with larger gene-expression datasets and more advanced Computational Biology techniques.

🌟 KEY FEATURES
🧬 Multi-Gene Analysis

Analyzes multiple genes across multiple patients.

🔢 NumPy Processing

Converts biological measurements into a numerical 2D array.

🐼 Pandas Data Analysis

Uses DataFrames for structured gene-expression analysis.

📊 Automated Comparison

Automatically identifies highest and lowest expression values.

📈 Multiple Visualizations

Generates four different visual representations of the dataset.

🔥 Heatmap Analysis

Uses Seaborn to visualize patient-gene expression patterns.

💻 Computational Biology Workflow

Combines biological concepts with Python programming and data analysis.

🚀 FUTURE IMPROVEMENTS

Future versions can include:

📁 CSV gene-expression input
📊 Excel file support
🧬 More genes
👥 Larger patient datasets
📈 Statistical significance testing
🔥 Advanced heatmap analysis
📊 Box plots
📊 Distribution plots
🧪 Expression-data normalization
🔬 Differential gene-expression analysis
📉 PCA-based analysis
🤖 Machine-learning-based classification
📊 Interactive dashboards
🎓 LEARNING OUTCOME

This project provides practical experience with:

Python
   ↓
Biological Data Structures
   ↓
NumPy
   ↓
Pandas
   ↓
Statistical Analysis
   ↓
Data Visualization
   ↓
Computational Biology
👨‍💻 DEVELOPER
Muhammad Maaz

Computational Biology | Python | Data Analysis | Machine Learning

Built with:

🐍 Python
🔢 NumPy
🐼 Pandas
📊 Matplotlib
🎨 Seaborn

⭐ PROJECT HIGHLIGHT

Turning patient gene-expression data into structured biological insights using Python.

This project is part of a growing collection of Computational Biology projects focused on combining biological knowledge with programming, data analysis, visualization, and machine learning.

#**📜 LICENSE**

This project is available for educational and learning purposes.

⭐ If you find this project useful, consider giving the repository a star!

#Python #ComputationalBiology #GeneExpression #Genomics #DataScience #NumPy #Pandas #Matplotlib #Seaborn #Bioinformatics #MachineLearning
