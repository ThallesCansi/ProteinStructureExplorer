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
