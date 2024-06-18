import streamlit as st

from utils.aminoData import *
from utils.graphPlot import *
from utils.languageSelector import selecionarLinguagem
from utils.templateFilters import carregarTraducoes

st.set_page_config(page_title="Aminoácidos", page_icon="🧬", layout="wide")


def main(nome_pagina: str):
    selecionarLinguagem()

    translations = carregarTraducoes()
    idioma = st.session_state.idioma
    page_data = translations[idioma][nome_pagina]

    st.title(page_data["title"])
    st.write(page_data["body"])

    amino_acids = carregarAminoacidos("data/aminoacids.json")
    st.table(tabelaAminoacidos(amino_acids))


if __name__ == "__main__":
    main("aminoacids")
