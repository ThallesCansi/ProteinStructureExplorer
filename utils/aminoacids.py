import pandas as pd
import matplotlib.pyplot as plt

# ----- DICIONÁRIOS -----

alanina = {
    "Radical": 0,
    "Essencial": False,
    "Polaridade": "Apolar",
    "Carga": 0,
    "pH": "Neutro",
    "Solubilidade": "Solúvel",
    "Função": 0,
}

arginina = {
    "Radical": 0,
    "Essencial": True,
    "Polaridade": "Polar",
    "Carga": 1,
    "pH": "Básico",
    "Solubilidade": "Solúvel",
    "Função": 0,
}

aspartato = {
    "Radical": 0,
    "Essencial": False,
    "Polaridade": "Polar",
    "Carga": -1,
    "pH": "Ácido",
    "Solubilidade": "Solúvel",
    "Função": 0,
}

asparagina = {
    "Radical": 0,
    "Essencial": False,
    "Polaridade": "Polar",
    "Carga": 0,
    "pH": "Neutro",
    "Solubilidade": "Solúvel",
    "Função": 0,
}

cisteina = {
    "Radical": 0,
    "Essencial": True,
    "Polaridade": "Polar",
    "Carga": 0,
    "pH": "Neutro",
    "Solubilidade": "Solúvel",
    "Função": 0,
}

fenilalanina = {
    "Radical": 0,
    "Essencial": True,
    "Polaridade": "Apolar",
    "Carga": 0,
    "pH": "Neutro",
    "Solubilidade": "Pouco solúvel",
    "Função": 0,
}

glicina = {
    "Radical": 0,
    "Essencial": False,
    "Polaridade": "Apolar",
    "Carga": 0,
    "pH": "Neutro",
    "Solubilidade": "Solúvel",
    "Função": 0,
}

glutamato = {
    "Radical": 0,
    "Essencial": False,
    "Polaridade": "Polar",
    "Carga": -1,
    "pH": "Ácido",
    "Solubilidade": "Solúvel",
    "Função": 0,
}

glutamina = {
    "Radical": 0,
    "Essencial": False,
    "Polaridade": "Polar",
    "Carga": -1,
    "pH": "Neutro",
    "Solubilidade": "Solúvel",
    "Função": 0,
}

histidina = {
    "Radical": 0,
    "Essencial": True,
    "Polaridade": "Polar",
    "Carga": 0,
    "pH": "Básico",
    "Solubilidade": "Solúvel",
    "Função": 0,
}

isoleucina = {
    "Radical": 0,
    "Essencial": True,
    "Polaridade": "Neutro",
    "Carga": 0,
    "pH": "Neutro",
    "Solubilidade": "Insolúvel",
    "Função": 0,
}

leucina = {
    "Radical": 0,
    "Essencial": True,
    "Polaridade": "Neutro",
    "Carga": 0,
    "pH": "Neutro",
    "Solubilidade": "Insolúvel",
    "Função": 0,
}

lisina = {
    "Radical": 0,
    "Essencial": True,
    "Polaridade": "Polar",
    "Carga": 1,
    "pH": "Básico",
    "Solubilidade": "Solúvel",
    "Função": 0,
}

metinonina = {
    "Radical": 0,
    "Essencial": True,
    "Polaridade": "Apolar",
    "Carga": 0,
    "pH": "Neutro",
    "Solubilidade": "Pouco solúvel",
    "Função": 0,
}

prolina = {
    "Radical": 0,
    "Essencial": False,
    "Polaridade": "Apolar",
    "Carga": 0,
    "pH": "Neutro",
    "Solubilidade": "Solúvel",
    "Função": 0,
}

serina = {
    "Radical": 0,
    "Essencial": False,
    "Polaridade": "Polar",
    "Carga": 0,
    "pH": "Neutro",
    "Solubilidade": "Solúvel",
    "Função": 0,
}

tirosina = {
    "Radical": 0,
    "Essencial": False,
    "Polaridade": "Polar",
    "Carga": 0,
    "pH": "Neutro",
    "Solubilidade": "Pouco solúvel",
    "Função": 0,
}

treonina = {
    "Radical": 0,
    "Essencial": True,
    "Polaridade": "Polar",
    "Carga": 0,
    "pH": "Neutro",
    "Solubilidade": "Solúvel",
    "Função": 0,
}

triptofano = {
    "Radical": 0,
    "Essencial": True,
    "Polaridade": "Apolar",
    "Carga": 0,
    "pH": "Neutro",
    "Solubilidade": "Pouco solúvel",
    "Função": 0,
}

valina = {
    "Radical": 0,
    "Essencial": True,
    "Polaridade": "Neutro",
    "Carga": 0,
    "pH": "Neutro",
    "Solubilidade": "Insolúvel",
    "Função": 0,
}

aminoacid_dict = {
    "A": alanina,
    "R": arginina,
    "N": asparagina,
    "D": aspartato,
    "C": cisteina,
    "E": glutamato,
    "Q": glutamina,
    "G": glicina,
    "H": histidina,
    "I": isoleucina,
    "L": leucina,
    "K": lisina,
    "M": metinonina,
    "F": fenilalanina,
    "P": prolina,
    "S": serina,
    "T": treonina,
    "W": triptofano,
    "Y": tirosina,
    "V": valina,
}

# ------ FUNÇÕES DE CONTAGEM ------


def count_aminoacids(protein_seq):
    """Retorna um dicionário com a contagem de aminoácidos da proteína."""

    aminoacids = aminoacid_dict.keys()
    count = {
        aminoacid: 0 for aminoacid in aminoacids
    }  # Seta como zero todas as quantidades iniciais
    for aminoacid in protein_seq:
        if aminoacid in aminoacids:
            count[
                aminoacid
            ] += 1  # A cada ocorrência, incrementar a quantidade correspondente

    return count


def count_ph(protein_seq):
    """Retorna um dicionário com a contagem de pH da proteína."""

    count_ph = {"Neutro": 0, "Básico": 0, "Ácido": 0}
    count = count_aminoacids(protein_seq)

    for aminoacid, quantity in count.items():
        ph = aminoacid_dict[aminoacid]["pH"]
        count_ph[ph] += quantity

    return count_ph


def count_essencials(protein_seq):
    """Retorna um dicionário com a contagem de proteínas essenciais."""

    count_essencials = {"Essencial": 0, "Não essencial": 0}
    count = count_aminoacids(protein_seq)

    for aminoacid, quantity in count.items():
        if aminoacid_dict[aminoacid]["Essencial"] is True:
            count_essencials["Essencial"] += quantity
        else:
            count_essencials["Não essencial"] += quantity

    return count_essencials


# ----- FUNÇÕES DE PLOTAGEM


