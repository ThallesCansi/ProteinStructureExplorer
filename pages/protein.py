import py3Dmol
from stmol import showmol
import streamlit as st

from utils.aminoData import *
from utils.graphPlot import *
from utils.languageSelector import selecionarLinguagem
from utils.proteinStructure import preverEstrutura
from utils.templateFilters import formatarSequencia, carregarTraducoes


st.set_page_config(page_title="Estrutura de Proteínas", page_icon="🧬", layout="wide")

st.set_option("deprecation.showPyplotGlobalUse", False)


def main(nome_pagina: str):
    selecionarLinguagem()

    translations = carregarTraducoes()
    idioma = st.session_state.idioma
    page_data = translations[idioma][nome_pagina]

    st.title(page_data["title"])

    sequencia = st.sidebar.text_area(
        label="Sequência de Aminoácidos",
        placeholder="Insira uma sequência de aminoácidos aqui...",
    )

    sequencia_formatada = formatarSequencia(sequencia)
    print(sequencia_formatada)

    if sequencia_formatada != False:
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

    if (
        st.sidebar.button("Gerar Estrutura da Proteína")
        and sequencia_formatada != False
    ):
        dados_estrutura = preverEstrutura(sequencia_formatada)
        if (
            "pdbs" in dados_estrutura
            and len(dados_estrutura["pdbs"]) > 0
            and sequencia_formatada != False
        ):
            st.session_state.dados_pdb = dados_estrutura["pdbs"][0]
            st.session_state.render = True
        elif sequencia_formatada == False or sequencia_formatada == "":
            st.error("Sequência de aminoácidos inválida. Sua sequência deve conter apenas os caracteres 'ACDEFGHIKLMNPQRSTVWY' que estão na tabela de aminoácidos.")
            st.markdown("""<a href='/aminoacids.py'>🔬""")
            st.session_state.render = False
        else:
            st.error(
                "Não foi possível gerar a estrutura da proteína. A chave 'pdbs' não foi encontrada ou está vazia."
            )
            st.session_state.render = False

    if "render" in st.session_state and st.session_state.render:
        xyzview = py3Dmol.view(width=800, height=600)
        xyzview.addModel(st.session_state.dados_pdb, "pdb")
        xyzview.setStyle({style: {"color": "spectrum"}})
        xyzview.addSurface(
            py3Dmol.VDW,
            {"opacity": surf_transp, "color": surf_color},
            {"hetflag": False},
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

        st.plotly_chart(
            graficoBarraPlotly(contarAminoacidos(sequencia_formatada, aminoacidos))
        )

        st.plotly_chart(graficoPizzaPlotly(contarPh(sequencia_formatada, aminoacidos)))

        st.plotly_chart(
            graficoEmpilhadoPlotly(contagemEssenciais(sequencia_formatada, aminoacidos))
        )

        st.plotly_chart(
            graficoBarraPlotly(contagemEssenciais(sequencia_formatada, aminoacidos))
        )


if __name__ == "__main__":
    main("protein")
