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
        st.write(page_data["Leandro"])
        st.markdown(
            """            
            <a style='all: unset; cursor: pointer' href='https://www.linkedin.com/in/llemosbr/'>
                <i class='fa-brands fa-linkedin fa-2xl'></i>
            </a>""",
            unsafe_allow_html=True,
        )

    col1, col2 = st.columns([3, 1])

    with col2:
        st.image(
            "images/Imagem de Perfil - Izabel.png", width=200, use_column_width=True
        )

    with col1:
        st.subheader("Izabel Carvalho")
        st.write(page_data["Izabel"])
        st.markdown(
            """
            <a style='all: unset; cursor: pointer;' href='https://github.com/IzabelCarvalho'>
                <i class='fa-brands fa-github-square fa-2xl'></i>
            </a>""",
            unsafe_allow_html=True,
        )

    col1, col2 = st.columns([1, 3])

    with col1:
        st.image("images/Imagem de Perfil - João.png", width=200, use_column_width=True)

    with col2:
        st.subheader("João Pedro Lima")
        st.write(page_data["João"])
        st.markdown(
            """
            <a style='all: unset; cursor: pointer' href='https://github.com/SpiderUntidy'>
                <i class='fa-brands fa-github-square fa-2xl'></i>
            </a>""",
            unsafe_allow_html=True,
        )

    col1, col2 = st.columns([3, 1])

    with col2:
        st.image(
            "images/Imagem de Perfil - Giovana.png", width=200, use_column_width=True
        )

    with col1:
        st.subheader("Giovana Coelho")
        st.write(page_data["Giovana"])
        st.markdown(
            """
            <a style='all: unset; cursor: pointer' href='https://github.com/giovana2005'>
                <i class='fa-brands fa-github-square fa-2xl'></i>
            </a>""",
            unsafe_allow_html=True,
        )

    col1, col2 = st.columns([1, 3])

    with col1:
        st.image(
            "images/Imagem de Perfil - Thalles.png", width=200, use_column_width=True
        )

    with col2:
        st.subheader("Thalles Cansi")
        st.write(page_data["Thalles"])
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
