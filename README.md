# 📂 revisao_py

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/)
[![Package Manager](https://img.shields.io/badge/environment-uv-purple.svg)](https://github.com/astral-sh/uv)
[![Editor](https://img.shields.io/badge/IDE-VSCode%20%2B%20Jupyter-007ACC.svg)](https://code.visualstudio.com/)

Repositório dedicado à revisão prática e consolidação de conceitos essenciais em **Python**, **Ciência de Dados** e **Aprendizado de Máquina**, utilizando um ambiente de desenvolvimento isolado.

---

## 📌 Sobre o Projeto

Este repositório serve como um laboratório pessoal de revisão, estudos e guia prático. O objetivo principal é exercitar desde a sintaxe e manipulação básica de dados até o desenvolvimento e avaliação de modelos de Machine Learning, mantendo um padrão limpo e reprodutível.

---

## 🚀 Configuração do Ambiente de Desenvolvimento

O projeto utiliza o **`uv`** para criação e gerenciamento de ambientes virtuais e dependências.

### 1. Clonar o Repositório
```bash
git clone [https://github.com/seu-usuario/revisao_py.git](https://github.com/seu-usuario/revisao_py.git)
cd revisao_py
```

### 🐳 Opção A: Execução via Docker (Recomendado para Portabilidade)

Esta opção garante que todo o ambiente (Python, Jupyter Server e dependências de Data Science) rode em um container isolado sem necessidade de configurar dependências locais na máquina.

#### 1. Subir o Container com Docker Compose
```bash
# Constrói a imagem (na primeira execução) e inicia o container em segundo plano
docker compose up -d --build
```

#### 2. Conectar o VS Code ao Jupyter do Container
1. Abra a pasta do projeto no VS Code (code .).

2. Abra qualquer arquivo notebook (.ipynb).

3. No canto superior direito, clique em Select Kernel > Existing Jupyter Server....

4. Insira a URL do servidor local: http://localhost:8888.

#### 3. Encerrar os Containers
```bash
docker compose down
```

### 🐍 Opção B: Execução Local via uv (Recomendado para Desenvolvimento Rápido)
Esta opção utiliza o uv para instalar o ambiente virtual e as dependências diretamente no sistema operacional local.

#### 1. Criar e Ativar o Ambiente Virtual

```bash
# Cria o ambiente virtual isolado com a tag (.venv) no terminal
uv venv --prompt .venv

# Ativa o ambiente (no Linux/Ubuntu)
source .venv/bin/activate
```

#### 2. Instalar as Dependências

```bash
# Instala todas as bibliotecas listadas no projeto
uv pip install -r requirements.txt
```

#### 3. Selecionar o Kernel no VS Code
1. Abra a pasta do projeto no VS Code (code .).

2. Abra qualquer arquivo notebook (.ipynb).

3. No canto superior direito, clique em Select Kernel > Python Environments....

4. Selecione o interpretador do ambiente criado em .venv/bin/python.

## 🛠️ Estrutura do Repositório
```
revisao_py/
├── .venv/                      # Ambiente virtual isolado (ignorado pelo Git)
├── 01_python_fundamentals/     # Revisão de fundamentos, OOP, módulos e estruturas
│   ├── files
│   └── img
├── 02_data_analysis/          # Manipulação e EDA com Pandas, NumPy, Seaborn/Matplotlib; pipelines reprodutíveis e ETL
├── 03_machine_learning/        # Modelos supervisionados, não-supervisionados e pipelines com Scikit-Learn
├── notebooks/                  # Experimentos, rascunhos e análises exploratórias rápidas
├── .dockerignore               # Arquivos ignorados no build da imagem
├── .gitignore                  # Arquivos e pastas a serem ignorados pelo versionamento
├── Dockerfile                  # Receita para construir a imagem Python + DS
├── docker-compose.yml          # Subida simplificada do container e do Jupyter
├── README.md                   # Documentação do repositório
└── requirements.txt            # Dependências geradas pelo uv/pip
```