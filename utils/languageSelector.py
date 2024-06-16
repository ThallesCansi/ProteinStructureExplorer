import streamlit as st


def selecionarLinguagem():
    """
    Adiciona um seletor de idiomas ao sidebar e atualiza o idioma selecionado no estado da sessão.
    
    Returns:
        str: Idioma selecionado.
    """
    if "idioma" not in st.session_state:
        st.session_state.idioma = "Português"

    if st.session_state.idioma == "Português":
        label = "Selecione o Idioma"
    else:
        label = "Select Language"

    idiomas = ["Inglês", "Português"]
    idioma_selecionado = st.sidebar.selectbox(
        label=label,
        options=idiomas,
        index=idiomas.index(st.session_state.idioma),
    )
    
    st.session_state.idioma = idioma_selecionado
    
    return idioma_selecionado
