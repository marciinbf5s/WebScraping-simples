# Downloader e Compactador de PDFs - ANS

Este projeto automatiza o download dos arquivos PDF dos Anexos I e II da página da ANS (Agência Nacional de Saúde Suplementar) e os compacta em um arquivo ZIP localmente.

---

## Índice

- [Descrição](#descrição)  
- [Funcionalidades](#funcionalidades)  
- [Requisitos](#requisitos)  
- [Instalação](#instalação)  
- [Como usar](#como-usar)  
- [Detalhes do Código](#detalhes-do-código)  
- [Contribuições](#contribuições)  
- [Licença](#licença)

---

## Descrição

Este script em Python acessa uma página da ANS que contém documentos importantes em PDF, busca automaticamente pelos links referentes aos Anexos I e II, baixa os arquivos PDF encontrados e os compacta em um arquivo ZIP local para facilitar o armazenamento e compartilhamento.

---

## Funcionalidades

- Acessa a página oficial da ANS para obtenção dos links dos documentos PDF dos Anexos I e II.  
- Download automático dos arquivos PDF relacionados.  
- Compactação dos arquivos baixados em um único arquivo ZIP.  
- Criação automática da pasta de destino caso não exista.  
- Tratamento básico de erros durante o download e compactação.

---

## Requisitos

- Python 3.x  
- Bibliotecas Python:
  - `requests`
  - `beautifulsoup4`

---

## Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

pip install requests beautifulsoup4

python app.py

