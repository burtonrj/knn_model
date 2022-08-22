import plotly.express as px
import pandas as pd

DATA = pd.read_csv("knn_data.csv")
DATA = DATA.reset_index().rename(columns={"index": "Subject ID"})
DATA['Gram-negative sepsis'] = DATA['Gram-negative sepsis'].replace(
    {0: "Gram-positive sepsis", 1: "Gram-negative sepsis"}
)
DATA = DATA.rename(columns={"Gram-negative sepsis": "Causative pathogen"})

fig = px.scatter_3d(
    DATA,
    x='MAIT cells activation cluster 4',
    y='CD8 T cell CD25 MFI',
    z='CD4 T cell CD161 MFI',
    color='Causative pathogen',
    hover_name="Subject ID"
)
fig.write_html("knn_model.html")
fig.show()

DATA = pd.read_csv("svm_data.csv")
DATA = DATA.reset_index().rename(columns={"index": "Subject ID"})
DATA['Gram-negative sepsis'] = DATA['Gram-negative sepsis'].replace(
    {0: "Gram-positive sepsis", 1: "Gram-negative sepsis"}
)
DATA = DATA.rename(columns={"Gram-negative sepsis": "Causative pathogen"})

fig = px.scatter_3d(
    DATA,
    x="Sodium plasma conc.",
    y="CD4+ CD8- MAIT cell cluster",
    z="Neutrophil count",
    color='Causative pathogen',
    hover_name="Subject ID"
)
fig.write_html("svm_model.html")
fig.show()
