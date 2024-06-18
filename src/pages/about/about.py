import streamlit as st
from src.partials.sidebar_image import sidebar_image
from src.partials.sidebar_title import sidebar_title
from src.partials.sidebar_spacer import sidebar_spacer

def app():
    st.title("Sobre")

    sidebar_spacer()
    sidebar_title()
    sidebar_image()

    st.write("Capiren é um sistema desenvolvido para reconhecer entidades nomeadas em textos na língua portuguesa. Compreende as temáticas geral, jurídica e geológica, oferecendo uma ferramenta para análise e rotulação de informações específicas em documentos e textos.")

    st.header("Funcionalidades Principais:")
    st.write("- Identificação automática de entidades nomeadas (nomes de pessoas, organizações, locais, etc.) em textos escritos em português.")
    st.write("- Suporte para diferentes categorias temáticas: geral, jurídica e geológica.")
    st.write("- Visualização de resultados através de texto anotado e gráfico.")

    st.header("Categorias de Rótulos")

    st.subheader("Geral:")
    st.write("- **ORG**: Organização")
    st.write("- **ABS**: Abstrato")
    st.write("- **TMP**: Tempo")
    st.write("- **LOC**: Localização")
    st.write("- **VAL**: Valor")
    st.write("- **PER**: Pessoa")
    st.write("- **ACO**: Ação")
    st.write("- **OBR**: Obra")
    st.write("- **OTR**: Outro")
    st.write("- **COI**: Coisa")

    st.subheader("Geologia:")
    st.write("- **OTR**: Outro")
    st.write("- **uniESTG**: Unidade Litoestratigráfica")
    st.write("- **EPC**: Época")
    st.write("- **bacSED**: Bacia Sedimentar")
    st.write("- **IDA**: Idade")
    st.write("- **PRD**: Período")
    st.write("- **ctxGBAC**: Contexto Geológico de Bacia")
    st.write("- **ERA**: Era")
    st.write("- **EON**: Éon")
    st.write("- **sedSLCT**:  Rocha sedimentar Siliciclástica")
    st.write("- **sedCARB**: Rocha Sedimentar Carbonática")
    st.write("- **sedORGN**: Rocha Sedimentar Orgânica")
    st.write("- **sedQUIM**: Rocha Sedimentar Química")

    st.subheader("Jurídico:")
    st.write("- **ORGANIZACAO**: Organização")
    st.write("- **PESSOA**: Pessoa")
    st.write("- **TEMPO**: Tempo")
    st.write("- **LOCAL**: Localização")
    st.write("- **LEGISLACAO**: Legislação")
    st.write("- **JURISPRUDENCIA**: Jurisprudência")

    st.write("")
    st.write("Desenvolvido por **Guilherme Tapajós**.")

if __name__ == "__main__":
    app()
