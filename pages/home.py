import streamlit as st
from st_pages import add_page_title

from utils.templateFilters import carregarTraducoes
from utils.languageSelector import selecionarLinguagem
from utils.proteinStructure import criarEstrutura


def main(nome_pagina: str):
    selecionarLinguagem()

    translations = carregarTraducoes()
    idioma = st.session_state.idioma
    page_data = translations[idioma][nome_pagina]

    st.title(page_data["title"])
    st.write(page_data["body"])

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

    st.write(page_data["learn_more"])
    st.subheader("Examples")
    st.write(page_data["examples"])
    st.caption(page_data["footer"])


if __name__ == "__main__":
    main(nome_pagina="home")
