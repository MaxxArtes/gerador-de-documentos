import streamlit as st
from fpdf import FPDF

def gerar_pdf(respostas, nome_arquivo="resumo_entrevista.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Resumo da Entrevista", ln=True, align='C')
    pdf.ln(10)

    for pergunta, resposta in respostas.items():
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, txt=f"{pergunta}:", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=resposta)
        pdf.ln(5)

    pdf.output(nome_arquivo)

# Perguntas padrão
perguntas_padrao = {
    'objetivo_principal': "Qual é o objetivo principal deste projeto?",
    'objetivos_secundarios': "Existem objetivos secundários? Se sim, quais?",
    'resultados_esperados': "Que entregáveis você espera (relatórios, dashboards, insights)?",
    'criterios_sucesso': "Como saberemos que o projeto foi bem-sucedido?",
    'restricoes': "Existem limitações de prazo, orçamento ou recursos?",
    'publico_alvo': "Quem vai usar os resultados da análise? Qual o nível de familiaridade com dados?",
    'descricao_problema': "Que problema estamos tentando resolver?",
    'contexto_problema': "Como esse problema foi identificado e há quanto tempo ele existe?",
    'impacto_problema': "Qual é o impacto desse problema no negócio/processos/resultados?",
    'problemas_relacionados': "Este problema está ligado a outras questões conhecidas?",
    'perguntas_analise': "Que perguntas específicas precisam ser respondidas para resolver o problema?",
    'metricas_kpis': "Existem KPIs ou métricas específicas a acompanhar?",
    'fontes_dados': "De onde virão os dados necessários (bancos de dados, planilhas, sistemas)?",
    'formato_resultados': "Como as respostas devem ser apresentadas (relatório, gráfico, tabela)?"
}

st.title("📜 Sistema de Entrevista de Dados")
st.write("Preencha o formulário abaixo para gerar o resumo da entrevista em PDF. Você pode editar as perguntas se quiser.")

respostas = {}

with st.form("entrevista_form"):
    st.subheader("Entendimento das Expectativas")
    for key in list(perguntas_padrao.keys())[:6]:
        pergunta_editada = st.text_input(f"Editar pergunta:", value=perguntas_padrao[key], key=f"edit_{key}")
        respostas[pergunta_editada] = st.text_input(f"Resposta:", key=f"resposta_{key}")

    st.subheader("Definição do Problema")
    for key in list(perguntas_padrao.keys())[6:10]:
        pergunta_editada = st.text_input(f"Editar pergunta:", value=perguntas_padrao[key], key=f"edit_{key}")
        respostas[pergunta_editada] = st.text_area(f"Resposta:", key=f"resposta_{key}")

    st.subheader("Definição das Perguntas de Análise")
    for key in list(perguntas_padrao.keys())[10:]:
        pergunta_editada = st.text_input(f"Editar pergunta:", value=perguntas_padrao[key], key=f"edit_{key}")
        respostas[pergunta_editada] = st.text_input(f"Resposta:", key=f"resposta_{key}")

    submitted = st.form_submit_button("Gerar PDF")

if submitted:
    gerar_pdf(respostas)
    st.success("PDF gerado com sucesso! Verifique o arquivo 'resumo_entrevista.pdf' na sua pasta.")

    with open("resumo_entrevista.pdf", "rb") as pdf_file:
        st.download_button("📥 Baixar PDF", pdf_file, file_name="resumo_entrevista.pdf")
