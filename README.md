# 💰 Dashboard Financeiro

Dashboard interativo desenvolvido em Streamlit para visualização e gestão de contas a pagar e contas a receber.

## 📋 Sobre o Projeto

Este dashboard financeiro oferece uma interface intuitiva para acompanhar o fluxo de caixa da empresa, com visualizações gráficas e métricas importantes para tomada de decisão.

## ✨ Funcionalidades

### Contas a Pagar

- **KPIs principais:**

  - 📅 Previsto no mês
  - ✅ Pago no mês
  - 💳 A pagar no ano
  - 💰 Pago no ano
  - ⚠️ Em atraso
  - 📊 % Atraso

- **Visualizações:**
  - Gráfico de barras por status e categoria
  - Gráfico de pizza por categoria
  - Tabela detalhada de todas as contas

### Contas a Receber

- **KPIs principais:**

  - 📅 Previsto no mês
  - ✅ Recebido no mês
  - 💳 A receber no ano
  - 💰 Recebido no ano
  - ⚠️ Em atraso
  - 📊 % Atraso

- **Visualizações:**
  - Gráfico de barras por status
  - Gráfico de pizza por status
  - Tabela detalhada de todas as contas

### Filtros Disponíveis

- **Período:** Neste mês, Neste ano, Por período específico
- **Status:** Todos, Aberto, Pago

## 🚀 Como Executar

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
cd finance-dashboard
```

2. Crie um ambiente virtual (recomendado):

```bash
python -m venv venv
```

3. Ative o ambiente virtual:

   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     source venv/bin/activate
     ```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

### Executando a Aplicação

Execute o seguinte comando no terminal:

```bash
streamlit run app.py
```

O dashboard será aberto automaticamente no seu navegador padrão em `http://localhost:8501`.

## 📁 Estrutura do Projeto

```
finance-dashboard/
│
├── app.py                      # Aplicação principal Streamlit
├── data.py                     # Módulo de dados e cálculos de KPIs
├── requirements.txt            # Dependências do projeto
├── README.md                   # Este arquivo
│
└── pages/
    ├── contas_a_pagar.py      # Página de contas a pagar
    └── contas_a_receber.py    # Página de contas a receber
```

## 📦 Dependências

- **streamlit** - Framework para criação de aplicações web interativas
- **plotly** - Biblioteca para criação de gráficos interativos
- **pandas** - Manipulação e análise de dados
- **bcrypt** - Criptografia de senhas
- **python-dotenv** - Gerenciamento de variáveis de ambiente

## 🔧 Configuração

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto para configurar variáveis de ambiente, se necessário:

```env
# Exemplo de variáveis de ambiente
DATABASE_URL=your_database_url
API_KEY=your_api_key
```

## 📊 Dados

Atualmente, o projeto utiliza dados de exemplo definidos no módulo `data.py`. Para produção, você pode:

1. Conectar a um banco de dados
2. Integrar com APIs
3. Carregar dados de arquivos CSV/Excel

## 🎨 Personalização

O dashboard pode ser personalizado editando:

- **app.py:** Layout principal e navegação
- **pages/:** Páginas específicas de cada módulo
- **data.py:** Fonte de dados e lógica de cálculo
