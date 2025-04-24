# 📄 Extrator de Notas Fiscais

Imagine ter que, todo mês, enfrentar o desafio de coletar manualmente os dados dos clientes a partir de notas fiscais em PDF — um trabalho repetitivo, cansativo e sujeito a erros.

Pensando nisso, desenvolvemos uma aplicação completa e intuitiva para automatizar a extração de informações essenciais de notas fiscais eletrônicas (NF-e) em PDF. Com apenas alguns cliques, você consegue extrair dados como CNPJ, razão social e valor da nota, organizando tudo de forma estruturada e confiável.

Com objetivo de facilitar o processo de análise, organização e integração dessas informações com sistemas contábeis, ERPs ou planilhas de controle, economizando tempo e garantindo mais precisão no seu fluxo de trabalho.


![Captura de tela da interface](docs/screenshots/interface.png)

## 🔍 Funcionalidades

- **Extração automática** de dados de notas fiscais PDF
- **Interface gráfica** intuitiva com Streamlit
- **Processamento em lote** de múltiplos arquivos
- **Validação de dados** para garantir qualidade das informações
- **Exportação** dos dados em formato CSV
- **Relatórios detalhados** por nota fiscal

## 📋 Dados Extraídos

- CNPJ da empresa
- Razão social da empresa
- Valor do serviço
- Número da nota fiscal
- Data de emissão
- Descrição do serviço prestado
- Comissão do vendedor
- Valor do ISS
- Base de cálculo

## 🚀 Como usar

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/paulo-santos-ds/extrator-_notas_fiscais
cd extrator-notas-fiscais
```
2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Execução

Para iniciar a aplicação:
```bash
streamlit run app.py
```

A interface será aberta automaticamente no seu navegador padrão.

## 📱 Modos de Uso

### Processamento de Arquivo Único

1. Selecione o modo "Arquivo único" na barra lateral
2. Faça o upload de um arquivo PDF de nota fiscal
3. Clique em "Processar PDF"
4. Visualize os dados extraídos e baixe-os em formato CSV

### Processamento em Lote

1. Selecione o modo "Processamento em lote" na barra lateral
2. Faça o upload de múltiplos arquivos PDF
3. Clique em "Processar Todos os PDFs"
4. Visualize o resumo dos dados e baixe-os em formato CSV

## 🧰 Tecnologias Utilizadas

- **Python**: Linguagem de programação
- **Streamlit**: Framework para criar interfaces web com Python
- **PyMuPDF (fitz)**: Para manipulação de PDFs
- **Pandas**: Para manipulação de dados
- **Expressões Regulares**: Para extração de padrões de texto

## 📊 Estrutura do Projeto

```
extrator-notas-fiscais/
│
├── app.py                     # Arquivo principal para execução da aplicação Streamlit
│
├── src/                       # Módulos e componentes do núcleo da aplicação
│   ├── extractor.py           # Lógica de extração de dados das notas fiscais (PDF parsing)
│   ├── parser_utils.py        # Funções auxiliares de parsing e tratamento de texto
│   └── interface.py           # Componentes da interface com Streamlit
│
├── tests/                     # Testes unitários e de integração
│   └── test_extractor.py      # Casos de teste para a extração de dados
│
├── temp/                      # Diretório para arquivos temporários e processamentos intermediários
│
├── logs/                      # Armazenamento de logs de execução e eventos do sistema
│   └── app.log                # Log principal da aplicação
│
├── docs/                      # Documentação técnica e guias de uso
│   └── user_guide.md          # Guia do usuário para instalação e utilização da aplicação
│
├── imagens/                   # Imagens utilizadas na interface ou na documentação
│   └── exemplo_nf.png         # Exemplo de nota fiscal usada para teste
│
├── videos/                    # Vídeos demonstrativos e tutoriais
│   └── aplicacao.mp4     # Demonstração em vídeo da aplicação em funcionamento
│
├── README.md                  # Visão geral do projeto, instruções de uso e configuração
│
└── requirements.txt           # Lista de dependências e bibliotecas necessárias

```



Para mais detalhes sobre a estrutura do projeto, consulte a [documentação detalhada](docs/structure.md).

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Reportar bugs
2. Sugerir novas funcionalidades
3. Enviar pull requests

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🔮 Próximos Passos

- [ ] Suporte para reconhecimento de diferentes layouts de notas fiscais
- [ ] Implementação de OCR para melhorar extração de textos em imagens
- [ ] Dashboard para análise de dados extraídos
- [ ] API para integração com outros sistemas

