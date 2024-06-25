import streamlit as st

from utils.templateFilters import carregarTraducoes
from utils.languageSelector import selecionarLinguagem
from utils.proteinStructure import criarEstrutura, sequenciaFASTA

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
        "Injectisome": "7AH9",
        "Glicoproteína do envelope do HIV 1": "6E8W",
        "Queratina parcial em Homo sapiens": "6EC0",
        "Colágeno Homo sapiens": "6Q43",
        "Albumina em Homo sapiens": "1AO6",
        "Subunidade Beta da hemoglobina Homo sapiens": "1GZX",
        "Glicoproteína da Membrana M do Sars coronavírus": "ZJ01",
        "Insulina Homo sapiens": "6B3Q",
        "Serotonina N-acetiltransferase Homo sapiens": "1KUV",
        "Receptor do Hormônio 1 concentrador de Melanina Homo sapiens": "7UL4",
        "Alfa-amilase Homo sapiens": "3OLD",
        "Ligante de ligação ao TAR do HIV projetado": "1UTS",
    }

    col1, col2 = st.columns(2)

    with col1:
        codigo_pdb_selecionado = st.selectbox(
            "Selecione uma proteína:", list(proteinas.keys())
        )
        if codigo_pdb_selecionado:
            codigo_pdb = proteinas[codigo_pdb_selecionado]
    with col2:
        codigo_pdb_manual = st.text_input("Ou insira um código PDB manualmente:")
        if codigo_pdb_manual:
            codigo_pdb = codigo_pdb_manual.upper()

    if "codigo_pdb" in locals():
        criarEstrutura(codigo_pdb)
        sequencia_FASTA = sequenciaFASTA(codigo_pdb)

        st.subheader("Sequência FASTA")
        st.code(sequencia_FASTA)

    st.subheader(page_data["advice"])
    st.write(page_data["advices"])

    st.caption(page_data["footer"])


if __name__ == "__main__":
    main(nome_pagina="home")
