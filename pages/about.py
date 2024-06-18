import streamlit as st

from utils.languageSelector import selecionarLinguagem
from utils.templateFilters import carregarTraducoes

st.set_page_config(page_title="Sobre", page_icon="📚", layout="wide")


st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """,
    unsafe_allow_html=True,
)


def main(nome_pagina: str):
    selecionarLinguagem()

    translations = carregarTraducoes()
    idioma = st.session_state.idioma
    page_data = translations[idioma][nome_pagina]

    st.title(page_data["title"])
    st.write(page_data["body"])

    col1, col2 = st.columns([1, 3])

    with col1:
        st.image(
            "images/Imagem de Perfil - Leandro.png", width=200, use_column_width=True
        )

    with col2:
        st.subheader("Leandro Lemos")
        st.write(
            "Professor Doutor na ILUM - Escola de Ciência. Pós-doutor em Bioinformática pelo Laboratório Nacional de Computação Científica (LNCC/MCTI) e em Ecologia Molecular pela Universidade Estadual de Campinas (UNICAMP). Realizou a concepção e coordenação do projeto."
        )
        st.markdown(
            """
            <a style='all: unset; cursor: pointer' href='https://www.github.com/ThallesCansi'>
                <i class='fa-brands fa-github-square fa-2xl'></i>
            </a>
            
            <a style='all: unset; cursor: pointer' href='https://www.linkedin.com/in/ThallesCansi'>
                <i class='fa-brands fa-linkedin fa-2xl'></i>
            </a>""",
            unsafe_allow_html=True,
        )

    col1, col2 = st.columns([3, 1])

    with col2:
        st.image(
            "images/Imagem de Perfil - Thalles.png", width=200, use_column_width=True
        )

    with col1:
        st.subheader("Thalles Cansi")
        st.write(
            "Estudante de Ciência e Tecnologia na ILUM e apaixonado por programação. Realizou o desenvolvimento do site e as visualizações das proteínas."
        )
        st.markdown(
            """
            <a style='all: unset; cursor: pointer' href='https://www.github.com/ThallesCansi'>
                <i class='fa-brands fa-github-square fa-2xl'></i>
            </a>
            
            <a style='all: unset; cursor: pointer' href='https://www.linkedin.com/in/ThallesCansi'>
                <i class='fa-brands fa-linkedin fa-2xl'></i>
            </a>""",
            unsafe_allow_html=True,
        )

    st.caption(page_data["footer"])


if __name__ == "__main__":
    main(nome_pagina="about")
