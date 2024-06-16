import streamlit as st

from utils.templateFilters import carregarTraducoes
from utils.languageSelector import selecionarLinguagem
from utils.proteinStructure import criarEstrutura

st.set_page_config(page_title="Início", page_icon="🏠", layout="wide")


def main(nome_pagina: str):
    selecionarLinguagem()

    translations = carregarTraducoes()
    idioma = st.session_state.idioma
    page_data = translations[idioma][nome_pagina]

    st.title(page_data["title"])
    st.write(page_data["body"])

    st.subheader(page_data["example"])

    proteinas = {
        "Hemoglobina": "4HHB",
        "Salmonela": "7AH9",
        "SARS-CoV-2": "3QY1",
        "Ebola": "7D35",
        "Insulina": "1UZ9",
        "Miosina": "1B7T",
    }

    pdb_code = st.selectbox("Selecione uma proteína:", list(proteinas.keys()))

    if pdb_code:
        criarEstrutura(proteinas[pdb_code])

    st.subheader(page_data["advice"])
    st.write(page_data["advices"])

    st.caption(page_data["footer"])


if __name__ == "__main__":
    main(nome_pagina="home")
