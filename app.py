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

# --- Interface Streamlit ---
st.title("📝 Sistema de Entrevista de Dados")
st.write("Preencha o formulário abaixo para gerar o resumo da entrevista em PDF.")

respostas = {}

with st.form("entrevista_form"):
    st.subheader("Entendimento das Expectativas")
    respostas['Objetivo principal'] = st.text_input("Qual é o objetivo principal deste projeto?")
    respostas['Objetivos secundários'] = st.text_input("Existem objetivos secundários? Se sim, quais?")
    respostas['Resultados esperados'] = st.text_input("Que entregáveis você espera (relatórios, dashboards, insights)?")
    respostas['Critérios de sucesso'] = st.text_input("Como saberemos que o projeto foi bem-sucedido?")
    respostas['Restrições'] = st.text_input("Existem limitações de prazo, orçamento ou recursos?")
    respostas['Público-alvo'] = st.text_input("Quem vai usar os resultados da análise? Qual o nível de familiaridade com dados?")

    st.subheader("Definição do Problema")
    respostas['Descrição do problema'] = st.text_area("Que problema estamos tentando resolver?")
    respostas['Contexto do problema'] = st.text_area("Como esse problema foi identificado e há quanto tempo ele existe?")
    respostas['Impacto do problema'] = st.text_area("Qual é o impacto desse problema no negócio/processos/resultados?")
    respostas['Problemas relacionados'] = st.text_area("Este problema está ligado a outras questões conhecidas?")

    st.subheader("Definição das Perguntas de Análise")
    respostas['Perguntas para análise'] = st.text_area("Que perguntas específicas precisam ser respondidas para resolver o problema?")
    respostas['Métricas/KPIs'] = st.text_input("Existem KPIs ou métricas específicas a acompanhar?")
    respostas['Fontes de dados'] = st.text_input("De onde virão os dados necessários (bancos de dados, planilhas, sistemas)?")
    respostas['Formato dos resultados'] = st.text_input("Como as respostas devem ser apresentadas (relatório, gráfico, tabela)?")

    submitted = st.form_submit_button("Gerar PDF")

if submitted:
    gerar_pdf(respostas)
    st.success("PDF gerado com sucesso! Verifique o arquivo 'resumo_entrevista.pdf' na sua pasta.")

    with open("resumo_entrevista.pdf", "rb") as pdf_file:
        st.download_button("📥 Baixar PDF", pdf_file, file_name="resumo_entrevista.pdf")

