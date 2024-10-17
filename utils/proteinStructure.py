import py3Dmol
from stmol import *
import streamlit as st
import requests


import requests


def preverEstrutura(sequencia: str) -> str:
    """
    Faz uma requisição à API da Meta ESMFold para prever a estrutura de uma sequência de aminoácidos.

    Args:
        sequencia (str): Sequência de aminoácidos.

    Returns:
        str: Estrutura prevista no formato PDB.
    """
    url = "https://api.esmatlas.com/foldSequence/v1/pdb/"
    headers = {
        "Content-Type": "text/plain",
    }
    response = requests.post(url, headers=headers, data=sequencia)
    
    print(response.text)
    
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Erro na requisição: {response.status_code} - {response.text}")


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
