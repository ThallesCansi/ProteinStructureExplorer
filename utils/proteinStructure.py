import py3Dmol
from stmol import *
import streamlit as st
import requests


def preverEstrutura(sequencia: str) -> dict:
    """
    Faz uma requisição à API do Biolm para prever a estrutura de uma sequência de aminoácidos.

    Args:
        sequencia (str): Sequência de aminoácidos.

    Returns:
        dict: Dicionário com informações sobre a estrutura prevista.
    """
    url = "https://biolm.ai/api/v2/esmfold-multichain/predict/"
    data = {"items": [{"sequence": sequencia + ":"}]}
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Token " + st.secrets["TOKEN"],
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


def criarEstrutura(codigo_pdb: str, estilo: list = [800, 600]) -> str:
    """
    Cria um visualizador 3D de uma estrutura de proteína a partir de um código PDB.

    Args:
        codigo_pdb (str): Código PDB da estrutura de proteína.

    Returns:
        str: Código HTML para renderizar o visualizador 3D.
    """
    xyzview = py3Dmol.view(query=codigo_pdb)
    xyzview.setStyle({"cartoon": {"color": "spectrum"}})
    xyzview.zoomTo()
    return showmol(xyzview, width=estilo[0], height=estilo[1])
