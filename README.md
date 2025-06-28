# ⚙️ Engenharia de Dados com AWS S3 · Bronze → Silver → Gold

Projeto didático voltado à construção de uma arquitetura de dados em camadas utilizando Python e AWS S3. Ideal para aprender conceitos como ingestão de dados, organização em buckets e boas práticas de repositório.

---

## 🧱 Estrutura de Camadas (Lakehouse)

| Camada | Bucket S3           | Descrição                                      |
|--------|---------------------|-----------------------------------------------|
| Bronze | `welldata-bronze`   | Dados crus, direto da fonte                   |
| Silver | `welldata-silver`   | Dados tratados e validados                    |
| Gold   | `welldata-gold`     | Dados prontos para consumo analítico e BI     |

---

## 📁 Estrutura do Projeto

---

## 🧪 Pré-requisitos

- Python 3.9+
- Conta AWS e chaves de acesso
- Git instalado

---

## 🚀 Como usar

```bash
# Clone o repositório
git clone git@github.com:wellingtonpawlino/engenharia-de-dados.git
cd engenharia-de-dados

# Crie e ative a virtualenv
python -m venv .venv
source .venv/Scripts/activate  # ou .venv/bin/activate no Linux/macOS

# Instale as dependências
pip install -r requirements.txt

# Crie o arquivo .env a partir do modelo
cp .env.template .env
# (edite e insira suas credenciais AWS)

# Crie os buckets S3
python aws_utils/criar_buckets.py
