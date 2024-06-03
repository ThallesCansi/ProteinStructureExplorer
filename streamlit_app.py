import streamlit as st
import requests
import json
from stmol import showmol
import py3Dmol


# Função para fazer a chamada à API do BioLM ESMFold
def predict_protein_structure(sequence):
    url = "https://biolm.ai/api/v2/esmfold-multichain/predict/"
    data = {"items": [{"sequence": sequence}]}
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Token {st.secrets['TOKEN']}",
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


# Função principal do aplicativo Streamlit
def main():
    st.title("Visualizador de Proteínas em 3D")

    # Campo para inserção da sequência de aminoácidos
    sequence = st.text_area("Insira a sequência de aminoácidos:")

    sequence = sequence + ":"

    sequence = sequence.replace("\n", "").replace(" ", "").upper()

    # Botão para gerar a estrutura da proteína
    if st.button("Gerar Estrutura da Proteína"):
        if sequence:
            # Enviar a sequência de aminoácidos para a API do BioLM ESMFold
            structure_data = predict_protein_structure(sequence)

            # Verificar se a resposta contém os dados da estrutura da proteína
            if (
                "pdb" in structure_data["results"][0]
            ):  # Ajuste a chave conforme necessário
                pdb_data = structure_data["results"][0]["pdb"]

                # Exibir a estrutura da proteína em 3D usando stmol e py3Dmol
                xyzview = py3Dmol.view(width=800, height=600)
                xyzview.addModel(pdb_data, "pdb")
                xyzview.setStyle({"cartoon": {"color": "spectrum"}})
                xyzview.zoomTo()
                showmol(xyzview, height=600, width=800)
            else:
                st.error("Não foi possível gerar a estrutura da proteína.")
        else:
            st.warning("Por favor, insira uma sequência de aminoácidos.")


# Executa o aplicativo principal
if __name__ == "__main__":
    main()
