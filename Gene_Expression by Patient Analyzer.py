import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("." * 30)

print("GENE EXPRESSION BY PATIENTS")

print("." * 30)


patients = {

    "Ali": {"BRCA1": 45, "TP53": 67, "EGFR": 32},

    "Sara": {"BRCA1": 78, "TP53": 54, "EGFR": 81},

    "Ahmad": {"BRCA1": 56, "TP53": 72, "EGFR": 44},

    "Ayesha": {"BRCA1": 89, "TP53": 61, "EGFR": 76}

}


# ============================================================
# PATIENT DATA
# ============================================================

print("\n", "." * 10, "PATIENTS DATA", "." * 10)


def show_patients(data):

    for patient, gene in data.items():

        print(patient, gene)


show_patients(patients)


# ============================================================
# CONVERT DICTIONARY INTO LIST
# ============================================================

gene_expression = []


def gene_list(data):

    for patient, gene in data.items():

        gene_expression.append(list(gene.values()))

    return gene_expression


result = gene_list(patients)


print("\nGENE EXPRESSION LIST IS:\n", result)


# ============================================================
# CONVERT LIST INTO NUMPY 2D ARRAY
# ============================================================

print(
    "\n",
    "." * 10,
    "CONVERT LIST INTO NUMPY 2D ARRAY",
    "." * 10
)


gene_array = np.array(result)


print("GENE EXPRESSION 2D ARRAY IS:\n", gene_array)


print("\nGENE EXPRESSION SHAPE IS:\n", gene_array.shape)


# ============================================================
# MEAN BY GENE
# ============================================================

mean_by_gene = np.mean(gene_array, axis=0)

print("\nMEAN BY GENE:\n", mean_by_gene)


# ============================================================
# MEAN BY PATIENT
# ============================================================

patient_mean = np.mean(gene_array, axis=1)

print("\nMEAN BY PATIENT:\n", np.round(patient_mean, 2))


# ============================================================
# PATIENT DATAFRAME
# ============================================================

print(
    "\n",
    "." * 10,
    "PATIENT DATAFRAME",
    "." * 10
)


dataframe = pd.DataFrame(

    gene_array,

    columns=["BRCA1", "TP53", "EGFR"]

)


print("PATIENT DATAFRAME IS:\n", dataframe)


# ============================================================
# ADD PATIENT NAMES
# ============================================================

dataframe.insert(0, "patients", patients.keys())


print(
    "\nPATIENT DATAFRAME AFTER ADDING NAMES:\n",
    dataframe
)


# ============================================================
# GENE ANALYSIS USING GROUPBY AND AGG
# ============================================================

gene_analysis = dataframe.groupby(
    "patients"
)[["BRCA1", "TP53", "EGFR"]].agg(
    ["mean", "min", "max"]
)


print(
    "\nGENE ANALYSIS SUMMARY IS:\n",
    gene_analysis
)


# ============================================================
# PATIENTS GENE ANALYSIS
# ============================================================

print("\nPATIENTS GENE ANALYSIS:")


genes = ["BRCA1", "TP53", "EGFR"]


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

    print(
        f"{gene} ANALYSIS | "
        f"HIGH EXPRESSION {high_patients}={high_values} | "
        f"LOW EXPRESSION {low_patients}={low_values}"
    )


# ============================================================
# VISUALIZATION
# ============================================================

print(
    "\n",
    "." * 10,
    "DATA VISUALIZATION",
    "." * 10
)


# ============================================================
# 1. GENE EXPRESSION BY PATIENT
# ============================================================

plt.figure(figsize=(10, 6))

x = np.arange(len(dataframe["patients"]))

width = 0.25


plt.bar(
    x - width,
    dataframe["BRCA1"],
    width,
    label="BRCA1"
)


plt.bar(
    x,
    dataframe["TP53"],
    width,
    label="TP53"
)


plt.bar(
    x + width,
    dataframe["EGFR"],
    width,
    label="EGFR"
)


plt.xticks(
    x,
    dataframe["patients"]
)

plt.xlabel("Patients")

plt.ylabel("Gene Expression")

plt.title("Gene Expression by Patient")

plt.legend()

plt.tight_layout()

plt.show()


# ============================================================
# 2. MEAN EXPRESSION BY GENE
# ============================================================

mean_gene_data = pd.Series(

    mean_by_gene,

    index=["BRCA1", "TP53", "EGFR"]

)


plt.figure(figsize=(8, 5))

plt.bar(
    mean_gene_data.index,
    mean_gene_data.values
)

plt.xlabel("Genes")

plt.ylabel("Mean Expression")

plt.title("Mean Gene Expression")

plt.tight_layout()

plt.show()


# ============================================================
# 3. MEAN EXPRESSION BY PATIENT
# ============================================================

plt.figure(figsize=(9, 5))

plt.bar(
    dataframe["patients"],
    patient_mean
)

plt.xlabel("Patients")

plt.ylabel("Mean Expression")

plt.title("Mean Gene Expression by Patient")

plt.tight_layout()

plt.show()


# ============================================================
# 4. GENE EXPRESSION HEATMAP
# ============================================================

heatmap_data = dataframe.set_index("patients")[
    ["BRCA1", "TP53", "EGFR"]
]


plt.figure(figsize=(8, 5))

sns.heatmap(
    heatmap_data,
    annot=True,
    fmt=".0f",
    cmap="viridis"
)

plt.title("Gene Expression Heatmap")

plt.xlabel("Genes")

plt.ylabel("Patients")

plt.tight_layout()

plt.show()


# ============================================================
# FINAL MESSAGE
# ============================================================

print(
    "\n",
    "." * 10,
    "ANALYSIS COMPLETED SUCCESSFULLY",
    "." * 10
)
