import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def graficoBarraPlotly(data: dict):
    """
    Função para plotar um gráfico de barras usando Plotly.

    Args:
        data (dict): Dicionário com os dados a serem plotados.

    Returns:
        fig: Gráfico de barras Plotly.
    """
    df = pd.DataFrame(list(data.items()), columns=["Aminoacid", "Quantity"])
    fig = px.bar(
        df,
        x="Aminoacid",
        y="Quantity",
        labels={"Aminoacid": "Aminoácido", "Quantity": "Quantidade"},
    )
    fig.update_layout(title="Gráfico de Barras de Aminoácidos")
    return fig


def graficoPizzaPlotly(data: dict):
    """
    Função para plotar um gráfico de pizza em Plotly.

    Args:
        data (dict): Dicionário com os dados a serem plotados.

    Returns:
        fig: Gráfico de pizza Plotly.
    """
    df = pd.DataFrame(list(data.items()), columns=["pH", "Quantity"])
    fig = px.pie(df, values="Quantity", names="pH")

    return fig


def graficoEmpilhadoPlotly(data: dict):
    """
    Função para plotar um gráfico de barras empilhadas em Plotly.

    Args:
        data (dict): Dicionário com os dados a serem plotados.

    Returns:
        fig: Gráfico de barras empilhadas Plotly.
    """
    df = pd.DataFrame(list(data.items()), columns=["Categories", ""])
    df.set_index("Categories", inplace=True)
    df = df.T
    percentages = df.div(df.sum(axis=1), axis=0) * 100

    fig = px.bar(
        df,
        labels=dict(Quantity="", index="", value="Quantidade", Categories="Categorias"),
    )

    for i, col in enumerate(df.columns):
        fig.data[i].text = percentages[col].map("{:.2f}%".format)
        fig.data[i].textposition = "inside"

    return fig
