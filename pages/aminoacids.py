import streamlit as st
from st_pages import add_page_title
import pandas as pd
import json

add_page_title(layout="wide")

file_path = "data/aminoacids.json"

with open(file_path, "r", encoding="utf-8") as file:
    amino_acidos = json.load(file)

df = pd.DataFrame(amino_acidos)

df.reset_index(drop=True, inplace=True)
df.index += 1

st.table(df)
