from st_pages import Page, add_page_title, show_pages

show_pages(
    [
        Page("pages/home.py", "Início", "🏠"),
        Page("pages/about.py", "Sobre", "📖"),
        Page("pages/protein.py", "Visualização Proteína", "🧬"),
        Page("pages/aminoacids.py", "Tabela de Aminoácidos", "🔬"),
    ]
)

add_page_title()
