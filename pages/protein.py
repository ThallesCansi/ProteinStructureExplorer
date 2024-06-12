import py3Dmol
from st_pages import add_page_title
from stmol import showmol
import streamlit as st

from utils.predictStructure import preverEstrutura
from utils.templateFilters import (
    formatarSequencia,
    carregarAminoacidos,
    extrairNomesAminoacidos,
)

add_page_title(layout="wide")


sequencia = st.sidebar.text_area(
    label="Sequência de Aminoácidos",
    placeholder="Insira uma sequência de aminoácidos aqui...",
)

sequencia_formatada = formatarSequencia(sequencia)

aminoacidos = carregarAminoacidos("data/aminoacids.json")
nomes_aminoacidos = extrairNomesAminoacidos(sequencia_formatada, aminoacidos)

estilos = {"Padrão": "cartoon", "Bastão": "stick", "Esfera": "sphere"}
estilo_selecionado = st.sidebar.selectbox("Estilo", list(estilos.keys()))
style = estilos[estilo_selecionado]

bcolor = st.sidebar.color_picker("Cor de fundo", "#FFFFFF")

surf_transp = st.sidebar.slider("Transparência da Superfície", 0.0, 1.0, 0.5)

surf_color = st.sidebar.color_picker("Cor da Superfície", "#EEEEEE")

residuos_selecionados = st.sidebar.multiselect(
    "Resíduos para destacar", options=nomes_aminoacidos
)

hl_color = st.sidebar.color_picker("Cor de Destaque", "#FF0000")

label_residuos = st.sidebar.checkbox("Rotular Resíduos", value=True)

if st.sidebar.button("Gerar Estrutura da Proteína"):
    dados_estrutura = preverEstrutura(sequencia_formatada)
    if "pdb" in dados_estrutura["results"][0]:
        st.session_state.dados_pdb = dados_estrutura["results"][0]["pdb"]
        st.session_state.dados_plddt = dados_estrutura["results"][0]["mean_plddt"]
        st.session_state.render = True
    else:
        st.error("Não foi possível gerar a estrutura da proteína.")
        st.session_state.render = False

if "render" in st.session_state and st.session_state.render:
    xyzview = py3Dmol.view(width=800, height=600)
    xyzview.addModel(st.session_state.dados_pdb, "pdb")
    xyzview.setStyle({style: {"color": "spectrum"}})
    xyzview.addSurface(
        py3Dmol.VDW, {"opacity": surf_transp, "color": surf_color}, {"hetflag": False}
    )
    xyzview.setBackgroundColor(bcolor)
    xyzview.zoomTo()

    for res_nome in residuos_selecionados:
        indices = [
            i + 1 for i, nome in enumerate(nomes_aminoacidos) if nome == res_nome
        ]
        for idx in indices:
            xyzview.addStyle({"resi": str(idx)}, {"stick": {"color": hl_color}})
            if label_residuos:
                xyzview.addResLabels(
                    {"resi": str(idx)},
                    {
                        "backgroundColor": "lightgray",
                        "fontColor": "black",
                        "backgroundOpacity": 0.5,
                    },
                )

    showmol(xyzview, height=600, width=700)
    st.write(f"Nível de Confiança (PLDDT): {st.session_state.dados_plddt:.2f}")
