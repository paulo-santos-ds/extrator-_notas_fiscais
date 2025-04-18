# app.py
import streamlit as st
import pandas as pd
import os
import time
import sys
from datetime import datetime
import base64

# Adiciona a pasta 'src' ao path para importar os módulos personalizados
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Importa o extrator de notas fiscais
from extrator import ExtractorNotaFiscal, processar_multiplos_pdfs

# Configuração da página
st.set_page_config(
    page_title="Extrator de Notas Fiscais",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Função para criar um link de download para o DataFrame
def get_table_download_link(df, filename, text):
    """Gera um link para download do dataframe como CSV"""
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">📥 {text}</a>'
    return href

# Função para exibir um card com as informações da nota fiscal
def exibir_card_nota(dados, index):
    with st.container():
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.subheader(f"📄 {dados['nome_arquivo']}")
            st.write(f"**Empresa:** {dados['dados_extraidos'].get('Empresa', 'N/A')}")
            st.write(f"**CNPJ:** {dados['dados_extraidos'].get('CNPJ', 'N/A')}")
            
        with col2:
            st.write(f"**Valor:** {dados['dados_extraidos'].get('Valor do Serviço', 'N/A')}")
            st.write(f"**NF:** {dados['dados_extraidos'].get('Número NF', 'N/A')}")
            st.write(f"**Data:** {dados['dados_extraidos'].get('Data de Emissão', 'N/A')}")
            
        if dados['problemas_encontrados']:
            st.warning("⚠️ Problemas encontrados:")
            for problema in dados['problemas_encontrados']:
                st.write(f"- {problema}")
        else:
            st.success("✅ Dados extraídos com sucesso!")
            
        # Botão para mostrar todos os dados
        if st.button(f"Ver detalhes", key=f"btn_detalhe_{index}"):
            st.json(dados['dados_extraidos'])
            
        st.markdown("---")

# Título do app
st.title("📄 Extrator de Notas Fiscais")
st.markdown("Um aplicativo para extrair informações de notas fiscais em arquivos PDF.")

# Sidebar com opções
st.sidebar.header("Opções")
modo = st.sidebar.radio("Selecione o modo:", ["Arquivo único", "Processamento em lote"])

if modo == "Arquivo único":
    st.header("Processamento de Arquivo Único")
    
    # Upload de arquivo
    uploaded_file = st.file_uploader("Escolha um arquivo PDF", type="pdf")
    
    if uploaded_file is not None:
        # Salvar arquivo temporariamente
        temp_file_path = os.path.join("temp", uploaded_file.name)
        os.makedirs("temp", exist_ok=True)
        
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Botão para processar
        if st.button("Processar PDF"):
            with st.spinner("Processando arquivo..."):
                try:
                    # Processar o arquivo
                    extrator = ExtractorNotaFiscal(temp_file_path)
                    dados = extrator.extrair_todos_dados()
                    relatorio = extrator.gerar_relatorio()
                    
                    # Exibir resultados
                    st.success("Arquivo processado com sucesso!")
                    
                    # Exibir dados em colunas
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("Dados Básicos")
                        st.markdown(f"**Empresa:** {dados.get('Empresa', 'N/A')}")
                        st.markdown(f"**CNPJ:** {dados.get('CNPJ', 'N/A')}")
                        st.markdown(f"**Número NF:** {dados.get('Número NF', 'N/A')}")
                        st.markdown(f"**Data de Emissão:** {dados.get('Data de Emissão', 'N/A')}")
                    
                    with col2:
                        st.subheader("Valores")
                        st.markdown(f"**Valor do Serviço:** {dados.get('Valor do Serviço', 'N/A')}")
                        st.markdown(f"**Base de Cálculo:** {dados.get('Base de Cálculo', 'N/A')}")
                        st.markdown(f"**ISS:** {dados.get('ISS', 'N/A')}")
                    
                    # Exibir informações do serviço
                    st.subheader("Detalhes do Serviço")
                    st.markdown(f"**Descrição:** {dados.get('Serviço Prestado', 'N/A')}")
                    
                    # Validar dados
                    problemas = extrator.validar_dados()
                    if problemas:
                        st.warning("⚠️ Atenção: Dados podem estar incompletos")
                        st.write("Problemas encontrados:")
                        for problema in problemas:
                            st.write(f"- {problema}")
                    
                    # Exibir todos os dados como JSON
                    with st.expander("Ver todos os dados extraídos (JSON)"):
                        st.json(dados)
                    
                    # Converter para DataFrame e oferecer download
                    df = pd.DataFrame([dados])
                    st.download_button(
                        label="📥 Baixar dados como CSV",
                        data=df.to_csv(index=False).encode('utf-8'),
                        file_name=f"dados_nf_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                        mime='text/csv'
                    )
                    
                except Exception as e:
                    st.error(f"Erro ao processar o arquivo: {str(e)}")
        
        # Limpeza de arquivos temporários
        if os.path.exists(temp_file_path):
            try:
                os.remove(temp_file_path)
            except:
                pass

else:  # Modo de processamento em lote
    st.header("Processamento em Lote")
    
    # Upload de múltiplos arquivos
    uploaded_files = st.file_uploader("Escolha múltiplos arquivos PDF", type="pdf", accept_multiple_files=True)
    
    if uploaded_files:
        st.write(f"📦 {len(uploaded_files)} arquivos selecionados")
        
        # Pasta temporária para salvar os arquivos
        temp_dir = os.path.join("temp", datetime.now().strftime("%Y%m%d_%H%M%S"))
        os.makedirs(temp_dir, exist_ok=True)
        
        # Salvar todos os arquivos na pasta temporária
        for uploaded_file in uploaded_files:
            temp_file_path = os.path.join(temp_dir, uploaded_file.name)
            with open(temp_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
        
        # Botão para processar
        if st.button("Processar Todos os PDFs"):
            with st.spinner("Processando arquivos..."):
                resultados = processar_multiplos_pdfs(temp_dir)
                
                # Exibir barra de progresso
                progresso = st.progress(0)
                status_text = st.empty()
                
                # Mostrar processamento
                for i, resultado in enumerate(resultados):
                    # Atualizar progresso
                    percentual = (i + 1) / len(resultados)
                    progresso.progress(percentual)
                    status_text.text(f"Processando arquivo {i+1} de {len(resultados)}: {resultado['nome_arquivo']}")
                    time.sleep(0.1)  # Simula algum processamento
                
                status_text.text(f"Concluído! {len(resultados)} arquivos processados.")
                
                # Exibir resultados
                st.success(f"✅ Processamento concluído! {len(resultados)} arquivos processados.")
                
                # Converter resultados para um DataFrame
                dados_lista = []
                for res in resultados:
                    if res['status'] != "Erro":
                        dados_lista.append(res['dados_extraidos'])
                
                if dados_lista:
                    df = pd.DataFrame(dados_lista)
                    
                    # Exibir tabela com dados
                    st.subheader("Resumo dos Dados Extraídos")
                    st.dataframe(df)
                    
                    # Link para download
                    st.markdown(
                        get_table_download_link(
                            df, 
                            f"notas_fiscais_dados_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                            "Baixar dados como CSV"
                        ), 
                        unsafe_allow_html=True
                    )
                
                # Exibir cards para cada resultado
                st.subheader("Detalhes por Arquivo")
                for i, resultado in enumerate(resultados):
                    if resultado['status'] != "Erro":
                        exibir_card_nota(resultado, i)
                    else:
                        st.error(f"❌ Erro ao processar {resultado['nome_arquivo']}: {resultado.get('mensagem_erro', 'Erro desconhecido')}")
            
            # Limpeza de arquivos temporários
            try:
                for arquivo in os.listdir(temp_dir):
                    os.remove(os.path.join(temp_dir, arquivo))
                os.rmdir(temp_dir)
            except:
                pass

# Adicionar informações no footer
st.sidebar.markdown("---")
st.sidebar.markdown("### Sobre")
st.sidebar.info(
    """
    Este aplicativo extrai informações relevantes de notas fiscais em formato PDF,  
    como CNPJ, nome da empresa, valor do serviço e mais.
    
    Desenvolvido com Python, PyMuPDF e Streamlit.
    """
)