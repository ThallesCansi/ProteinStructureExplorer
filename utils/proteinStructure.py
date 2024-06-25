import py3Dmol
from stmol import *
import streamlit as st
import requests


def preverEstrutura(sequencia: str) -> dict:
    """
    Faz uma requisição à API da NVIDIA para prever a estrutura de uma proteína a partir de uma sequência de aminoácidos.

    Args:
        sequencia (str): Sequência de aminoácidos.

    Returns:
        dict: Dicionário com informações sobre a estrutura prevista.
    """
    invoke_url = "https://health.api.nvidia.com/v1/biology/nvidia/esmfold"

    headers = {
        "Authorization": "Bearer " + st.secrets["TOKEN"],
        "Accept": "application/json",
    }

    payload = {"sequence": sequencia}

    session = requests.Session()

    response = session.post(invoke_url, headers=headers, json=payload)

    response.raise_for_status()

    return response.json()


def criarEstrutura(codigo_pdb: str, estilo: list = [800, 400]) -> str:
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


def sequenciaFASTA(codigo_pdb: str) -> str:
    url = f"https://www.rcsb.org/fasta/entry/{codigo_pdb}"

    response = requests.get(url)

    if response.status_code == 200:
        dados_fasta = response.text

        linhas = dados_fasta.splitlines()

        sequencia_linhas = [linha for linha in linhas if not linha.startswith(">")]

        sequencia = "".join(sequencia_linhas)

        return sequencia
    else:
        return f"Erro ao obter dados: {response.status_code}"
