from st_pages import Page, add_page_title, show_pages
import streamlit as st


def main():
    pages = [
        Page("pages/home.py", "Início", "🏠"),
        Page("pages/about.py", "Sobre", "📖"),
        Page("pages/protein.py", "Visualização Proteína", "🧬"),
        Page("pages/aminoacids.py", "Tabela de Aminoácidos", "🔬"),
    ]

    show_pages(pages)


if __name__ == "__main__":
    main()
