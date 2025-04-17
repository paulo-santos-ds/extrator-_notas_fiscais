# 📄 Extrator de Notas Fiscais

Desenvolvemos uma aplicação completa e intuitiva para realizar a extração automatizada de informações essenciais de notas fiscais eletrônicas (NF-e) em formato PDF. O objetivo é facilitar o processo de análise, organização e integração dos dados fiscais com sistemas contábeis, ERPs ou planilhas de controle interno.

![Captura de tela da interface](docs/screenshots/interface_example.png)

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
├── app.py                     # Aplicativo principal Streamlit
├── src/                       # Código fonte
├── tests/                     # Testes automatizados
├── temp/                      # Pasta temporária 
├── logs/                      # Logs da aplicação
├── docs/                      # Documentação
├── README.md                  # Este arquivo
└── requirements.txt           # Dependências do projeto
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

