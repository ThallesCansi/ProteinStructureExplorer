import json
import pandas as pd


def carregarAminoacidos(filepath: str) -> dict:
    """
    Carrega informações sobre aminoácidos de um arquivo JSON.

    Args:
        filepath (str): Caminho para o arquivo JSON.

    Returns:
        dict: Dicionário com informações sobre aminoácidos.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)
        return {aa["Código de uma letra"]: aa for aa in data}


def tabelaAminoacidos(aminoacids_info: dict) -> pd.DataFrame:
    """
    Retorna uma tabela com informações sobre aminoácidos.

    Args:
        aminoacids_info (dict): Dicionário com informações sobre aminoácidos.

    Returns:
        pd.DataFrame: Tabela com informações sobre aminoácidos.
    """
    return pd.DataFrame(aminoacids_info.values())


def extrairNomesAminoacidos(sequencia: str, aminoacids_info: dict) -> list[str]:
    """
    Extrai os nomes dos aminoácidos de uma sequência formatada.

    Args:
        sequencia (str): Sequência de aminoácidos formatada.
        aminoacids_info (dict): Dicionário com informações sobre aminoácidos.

    Returns:
        List[str]: Lista com os nomes dos aminoácidos.
    """
    mapeamento = {k: v["Código de três letras"] for k, v in aminoacids_info.items()}
    return [mapeamento.get(s, "") for s in sequencia]


def contarAminoacidos(sequencia: str, aminoacid_dict: dict) -> dict:
    """
    Retorna um dicionário com a contagem de aminoácidos da proteína.

    Args:
        sequencia (str): Sequência de aminoácidos.
        aminoacid_dict (dict): Dicionário com informações sobre aminoácidos.

    Returns:
        dict: Dicionário com a contagem de aminoácidos.
    """
    count = {aminoacid: 0 for aminoacid in aminoacid_dict.keys()}
    for aminoacid in sequencia:
        if aminoacid in aminoacid_dict:
            count[aminoacid] += 1

    return count


def contarPh(sequencia: str, aminoacid_dict: dict) -> dict:
    """
    Retorna um dicionário com a contagem de pH da proteína.

    Args:
        sequencia (str): Sequência de aminoácidos.
        aminoacid_dict (dict): Dicionário com informações sobre aminoácidos.

    Returns:
        dict: Dicionário com a contagem de pH.
    """
    count_ph = {"Neutro": 0, "Básico": 0, "Ácido": 0}
    count = contarAminoacidos(sequencia, aminoacid_dict)

    for aminoacid, quantity in count.items():
        ph = aminoacid_dict[aminoacid]["pH"]
        count_ph[ph] += quantity

    return count_ph


def contagemEssenciais(sequencia: str, aminoacid_dict: dict) -> dict:
    """
    Retorna um dicionário com a contagem de proteínas essenciais.

    Args:
        sequencia (str): Sequência de aminoácidos.
        aminoacid_dict (dict): Dicionário com informações sobre aminoácidos.

    Returns:
        dict: Dicionário com a contagem de proteínas essenciais.
    """
    count_essenciais = {"Essencial": 0, "Não essencial": 0}
    count = contarAminoacidos(sequencia, aminoacid_dict)

    for aminoacid, quantity in count.items():
        if aminoacid_dict[aminoacid]["Essencial"]:
            count_essenciais["Essencial"] += quantity
        else:
            count_essenciais["Não essencial"] += quantity

    return count_essenciais
