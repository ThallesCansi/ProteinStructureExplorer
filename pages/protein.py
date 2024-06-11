import streamlit as st
from st_pages import add_page_title
from stmol import showmol
import py3Dmol

from utils.templateFilters import formatarSequencia
from utils.predictStructure import preverEstrutura

add_page_title(layout="wide")

st.write(
    "Nesta página, você pode inserir uma sequência de aminoácidos e visualizar a estrutura da proteína correspondente. Para mais informações, acesse [biolm.ai](https://biolm.ai/)."
)

sequencia = st.text_area(
    label="Sequência de Aminoácidos",
    placeholder="Insira uma sequência de aminoácidos aqui...",
)

sequencia_formatada = formatarSequencia(sequencia)
st.session_state.sequencia = sequencia_formatada

bcolor = st.color_picker("Escolha uma cor", "#89cff0")

estilos = {
    "Padrão": "cartoon",
    "Bastão": "stick",
    "Esfera": "sphere",
}
estilo_selecionado = st.selectbox("Estilo", list(estilos.keys()))
style = estilos[estilo_selecionado]

if st.button("Gerar Estrutura da Proteína") and "sequencia" in st.session_state:
    dados_estrutura = preverEstrutura(st.session_state.sequencia)
    if "pdb" in dados_estrutura["results"][0]:
        st.session_state.dados_pdb = dados_estrutura["results"][0]["pdb"]
        st.session_state.render = True
    else:
        st.error("Não foi possível gerar a estrutura da proteína.")
        st.session_state.render = False

if "render" in st.session_state and st.session_state.render:
    xyzview = py3Dmol.view(width=800, height=600)
    xyzview.addModel(st.session_state.dados_pdb, "pdb")
    xyzview.setStyle({style: {"color": "spectrum"}})
    xyzview.setBackgroundColor(bcolor)
    xyzview.zoomTo()
    showmol(xyzview, height=600, width=700)

st.write(
    "Para saber mais sobre as sequências de aminoácidos e suas respectivas letras, acesse:"
)
st.page_link("pages/aminoacids.py", label="Tabela de Aminoácidos", icon="🔬")
