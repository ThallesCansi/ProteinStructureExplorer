import json


def formatarSequencia(sequencia: str) -> str:
    """
    Remove espaços e quebras de linha de uma sequência de aminoácidos e a converte para letras maiúsculas.

    Args:
        sequencia (str): Sequência de aminoácidos.

    Returns:
        str: Sequência de aminoácidos formatada.
    """
    return sequencia.replace(" ", "").replace("\n", "").upper()


def carregarAminoacidos(filepath: str) -> dict:
    """
    Carrega informações sobre aminoácidos de um arquivo JSON.

    Args:
        filepath (str): Caminho para o arquivo JSON.

    Returns:
        dict: Dicionário com informações sobre aminoácidos.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)
    

def carregarTraducoes(filepath: str = "data/translations.json") -> dict:
    """
    Carrega traduções de aminoácidos de um arquivo JSON.

    Args:
        filepath (str, optional): Caminho para o arquivo JSON. Default para "data/translations.json".

    Returns:
        dict: Dicionário com traduções de aminoácidos.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def extrairNomesAminoacidos(sequencia: str, aminoacids_info: dict) -> list[str]:
    """
    Extrai os nomes dos aminoácidos de uma sequência formatada.

    Args:
        sequencia (str): Sequência de aminoácidos formatada.
        aminoacids_info (dict): Dicionário com informações sobre aminoácidos.

    Returns:
        List[str]: Lista com os nomes dos aminoácidos.
    """
    mapeamento = {
        aa["Código de uma letra"]: aa["Código de três letras"] for aa in aminoacids_info
    }
    return [mapeamento.get(s, "") for s in sequencia]
