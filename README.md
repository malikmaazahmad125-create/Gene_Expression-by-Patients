
# 🧬 **GENE EXPRESSION BY PATIENTS**

### 🔬 **A Python-Based Computational Biology & Gene Expression Analysis Project**

**Gene Expression by Patients** is a Python-based Computational Biology project designed to analyze the expression levels of multiple genes across different patients.

The project analyzes **BRCA1, TP53, and EGFR** gene expression values and demonstrates how biological data can be transformed from **Python Dictionaries → Lists → NumPy 2D Arrays → Pandas DataFrames** for systematic analysis.

It also performs patient-level and gene-level analysis and generates **4 professional visualizations** using Matplotlib and Seaborn.

---

# 🎯 **PROJECT OBJECTIVES**

- 🧬 Analyze gene expression data for multiple patients.
- 📊 Calculate mean expression by gene.
- 👥 Calculate mean expression by patient.
- 🔢 Convert biological data into NumPy arrays.
- 🐼 Create and analyze Pandas DataFrames.
- 📈 Perform `groupby()` and `agg()` analysis.
- 🔍 Identify highest and lowest gene expression.
- 🔥 Visualize gene expression patterns.
- 🧠 Interpret results from a Computational Biology perspective.

---

# 🧬 **GENES ANALYZED**

| Gene | Biological Role |
|---|---|
| **BRCA1** | Involved in DNA damage response and repair |
| **TP53** | Important tumor-suppressor gene involved in cell-cycle regulation |
| **EGFR** | Involved in cell signaling, growth, and proliferation |

> **Note:** The values used in this project are example values for programming and Computational Biology practice. They are not clinical or diagnostic measurements.

---

# 👥 **PATIENT DATA**

The project contains gene-expression values for four example patients:

**Ali, Sara, Ahmad, and Ayesha**

Each patient contains expression values for:

- **BRCA1**
- **TP53**
- **EGFR**

```python
patients = {

    "Ali": {"BRCA1": 45, "TP53": 67, "EGFR": 32},

    "Sara": {"BRCA1": 78, "TP53": 54, "EGFR": 81},

    "Ahmad": {"BRCA1": 56, "TP53": 72, "EGFR": 44},

    "Ayesha": {"BRCA1": 89, "TP53": 61, "EGFR": 76}

}
```

---

# 🔄 **DATA TRANSFORMATION**

```text
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
```

---

# 🔢 **NUMPY ANALYSIS**

The project converts gene-expression values into a NumPy 2D array:

```python
gene_array = np.array(result)
```

The resulting array has the shape:

```text
(4, 3)
```

Meaning:

```text
4 Patients × 3 Genes
```

### **Mean Expression By Gene**

```python
mean_by_gene = np.mean(
    gene_array,
    axis=0
)
```

This calculates the average expression of each gene across all patients.

### **Mean Expression By Patient**

```python
patient_mean = np.mean(
    gene_array,
    axis=1
)
```

This calculates the average expression of the three genes for each patient.

---

# 🐼 **PANDAS DATAFRAME**

```python
dataframe = pd.DataFrame(
    gene_array,
    columns=["BRCA1", "TP53", "EGFR"]
)
```

The resulting structure is:

| Patients | BRCA1 | TP53 | EGFR |
|---|---:|---:|---:|
| Ali | 45 | 67 | 32 |
| Sara | 78 | 54 | 81 |
| Ahmad | 56 | 72 | 44 |
| Ayesha | 89 | 61 | 76 |

---

# 📊 **GENE ANALYSIS USING GROUPBY & AGG**

```python
gene_analysis = dataframe.groupby(
    "patients"
)[["BRCA1", "TP53", "EGFR"]].agg(
    ["mean", "min", "max"]
)
```

This generates:

- **Mean expression**
- **Minimum expression**
- **Maximum expression**

for the analyzed patient data.

---

# 🔍 **HIGH & LOW GENE EXPRESSION**

The program automatically identifies the patients with the highest and lowest expression for each gene.

```python
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
```

This makes the analysis automatic rather than manually checking every value.

---

# 📈 **DATA VISUALIZATION**

The project contains **4 visualizations**.

## **1. 📊 Gene Expression By Patient**

A grouped bar chart compares **BRCA1, TP53, and EGFR** across all patients.

## **2. 📊 Mean Expression By Gene**

A bar chart displays the average expression of **BRCA1, TP53, and EGFR** across all patients.

## **3. 📊 Mean Expression By Patient**

A bar chart displays the average expression of all three genes for each patient.

## **4. 🔥 Gene Expression Heatmap**

A Seaborn heatmap visualizes:

```text
Patients × Genes × Expression Values
```

```python
sns.heatmap(
    heatmap_data,
    annot=True,
    fmt=".0f",
    cmap="viridis"
)
```

The heatmap provides a quick visual overview of gene-expression patterns.

---

# 🖼️ **PROJECT VISUALIZATION**

The project includes a professional visualization image containing:

```text
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
```

Add the project image:
# 🖼️ **PROJECT VISUALIZATION**

![Gene Expression By Patients](./gene_expression_by_patients.png)
# 🧠 **BIOLOGICAL INSIGHTS**

Based on the example dataset:

- **BRCA1** shows its highest expression in **Ayesha**.
- **TP53** shows its highest expression in **Ahmad**.
- **EGFR** shows its highest expression in **Sara**.
- The heatmap provides an easy visual comparison of gene-expression patterns.
- Mean expression provides a simple summary of overall gene-expression levels.
- Different patients show different expression profiles across the three genes.

> **Important:** These values are example data for educational purposes. Gene-expression values alone cannot be used to diagnose disease or make clinical decisions.

---

# 🛠️ **TECHNOLOGIES USED**

| Technology | Purpose |
|---|---|
| 🐍 **Python** | Core programming |
| 🔢 **NumPy** | Numerical calculations and 2D arrays |
| 🐼 **Pandas** | DataFrames and data analysis |
| 📊 **Matplotlib** | Bar-chart visualization |
| 🎨 **Seaborn** | Heatmap visualization |

---

# 📦 **INSTALLATION**

```bash
git clone YOUR_REPOSITORY_URL
cd Gene-Expression-By-Patients
pip install numpy pandas matplotlib seaborn
```

---

# ▶️ **HOW TO RUN**

```bash
python gene_expression_by_patients.py
```

The program will:

1. Display patient data.
2. Convert dictionary into a list.
3. Create NumPy 2D array.
4. Calculate mean expression by gene.
5. Calculate mean expression by patient.
6. Create Pandas DataFrame.
7. Perform groupby & aggregation.
8. Find high/low gene expression.
9. Generate 4 visualizations.
10. Complete the analysis.

---

# 📂 **PROJECT STRUCTURE**

```text
Gene-Expression-By-Patients/
│
├── gene_expression_by_patients.py
├── gene_expression_by_patients.png
├── requirements.txt
└── README.md
```

---

# 📄 **REQUIREMENTS**

```text
numpy
pandas
matplotlib
seaborn
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

# 🧠 **PYTHON CONCEPTS PRACTICED**

- **Dictionaries**
- **Nested Dictionaries**
- **Lists**
- **For Loops**
- **Functions**
- **NumPy Arrays**
- **2D Arrays**
- **Array Shape**
- **Mean Calculation**
- **Pandas DataFrames**
- **DataFrame Insert**
- **Groupby**
- **Aggregation**
- **Indexing**
- **Maximum & Minimum**
- **Matplotlib**
- **Seaborn**
- **Heatmaps**
- **Data Visualization**

---

# 🔬 **COMPUTATIONAL BIOLOGY VALUE**

This project demonstrates how biological measurements can be converted into structured computational data.

```text
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
```

This provides a foundation for working with larger gene-expression datasets and more advanced Computational Biology techniques.

---

# 🌟 **KEY FEATURES**

### **🧬 Multi-Gene Analysis**
Analyzes multiple genes across multiple patients.

### **🔢 NumPy Processing**
Converts biological measurements into a numerical 2D array.

### **🐼 Pandas Data Analysis**
Uses DataFrames for structured gene-expression analysis.

### **📊 Automated Comparison**
Automatically identifies highest and lowest expression values.

### **📈 Multiple Visualizations**
Generates four different visual representations of the dataset.

### **🔥 Heatmap Analysis**
Uses Seaborn to visualize patient-gene expression patterns.

### **💻 Computational Biology Workflow**
Combines biological concepts with Python programming and data analysis.

---

# 🚀 **FUTURE IMPROVEMENTS**

- 📁 CSV gene-expression input
- 📊 Excel file support
- 🧬 More genes
- 👥 Larger patient datasets
- 📈 Statistical significance testing
- 🔥 Advanced heatmap analysis
- 📊 Box plots
- 📊 Distribution plots
- 🧪 Expression-data normalization
- 🔬 Differential gene-expression analysis
- 📉 PCA-based analysis
- 🤖 Machine-learning-based classification
- 📊 Interactive dashboards

---

# 🎓 **LEARNING OUTCOME**

```text
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
```

---

# 👨‍💻 **DEVELOPER**

## **Muhammad Maaz**

**Computational Biology | Python | Data Analysis | Machine Learning**

Built with:

🐍 **Python**  
🔢 **NumPy**  
🐼 **Pandas**  
📊 **Matplotlib**  
🎨 **Seaborn**

---

# ⭐ **PROJECT HIGHLIGHT**

> **Turning patient gene-expression data into structured biological insights using Python.**

This project is part of a growing collection of **Computational Biology projects** focused on combining biological knowledge with programming, data analysis, visualization, and machine learning.

---

# 📜 **LICENSE**

This project is available for educational and learning purposes.

---

### ⭐ **If you find this project useful, consider giving the repository a star!**

**#Python #ComputationalBiology #GeneExpression #Genomics #DataScience #NumPy #Pandas #Matplotlib #Seaborn #Bioinformatics #MachineLearning**
