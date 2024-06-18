import pandas as pd
import matplotlib.pyplot as plt
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


def graficoBarra(data: dict):
    """
    Função para plotar um gráfico de barras.

    Args:
        data (dict): Dicionário com os dados a serem plotados.

    Returns:
        plt.show(): Exibe o gráfico de barras.
    """
    df = pd.DataFrame(list(data.items()), columns=["Aminoacid", "Quantity"])
    ax = df.plot(kind="bar", x="Aminoacid", xlabel="Aminoácido", ylabel="Quantidade")
    ax.legend().set_visible(False)

    return plt.show()


def graficoPizzaPloty(data: dict):
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


def graficoPizza(data: dict):
    """
    Função para plotar um gráfico de pizza.

    Args:
        data (dict): Dicionário com os dados a serem plotados.

    Returns:
        plt.show(): Exibe o gráfico de pizza.
    """
    df = pd.DataFrame(list(data.items()), columns=["pH", "Quantity"])
    ax = df.plot(
        kind="pie", y="Quantity", autopct="%1.1f%%", labels=[""] * len(df), ylabel=""
    )
    plt.legend(labels=df["pH"])

    return plt.show()


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
    
    fig = px.bar(df, labels=dict(Quantity="", index="", value="Quantidade", Categories="Categorias"))
    
    for i, col in enumerate(df.columns):
        fig.data[i].text = percentages[col].map('{:.2f}%'.format)
        fig.data[i].textposition = 'inside'
    
    return fig


def graficoEmpilhado(data: dict):
    """
    Função para plotar um gráfico de barras empilhadas.

    Args:
        data (dict): Dicionário com os dados a serem plotados.

    Returns:
        plt.show(): Exibe o gráfico de barras empilhadas.
    """
    df = pd.DataFrame(list(data.items()), columns=["Categories", "Quantity"])
    df.set_index("Categories", inplace=True)
    df = df.T

    ax = df.plot(kind="bar", stacked=True, width=0.1, ylabel="Quantidade")
    ax.set_xticklabels([])
    ax.legend(title="")

    for i, col in enumerate(df.columns):
        value = df[col].iloc[0]
        percentage = f"{(value / df.sum(axis=1)[0] * 100):.1f}%"
        if i == 0:
            y_pos = value / 2
        else:
            y_pos = df.iloc[0, i - 1] + value / 2
        ax.text(0, y_pos, percentage, ha="center", va="center")

    return plt.show()
