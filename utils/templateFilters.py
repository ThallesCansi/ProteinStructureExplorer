import json


def formatarSequencia(sequencia: str) -> str:
    """
    Remove espaços e quebras de linha de uma sequência de aminoácidos e a converte para letras maiúsculas.

    Args:
        sequencia (str): Sequência de aminoácidos.

    Returns:
        str: Sequência de aminoácidos formatada.
    """
    sequencia_formatada = sequencia.replace(" ", "").replace("\n", "").upper()

    lista_aminoacidos = [
        "A",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "K",
        "L",
        "M",
        "N",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "V",
        "W",
        "Y",
    ]

    if (
        all(aminoacido in lista_aminoacidos for aminoacido in sequencia)
        or sequencia_formatada == ""
    ):
        return sequencia_formatada
    else:
        return False


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
