import os
import requests
from bs4 import BeautifulSoup
import zipfile
from urllib.parse import urljoin

def criar_pasta(pasta):
    """Cria a pasta se não existir"""
    if not os.path.exists(pasta):
        os.makedirs(pasta)

def baixar_pdf(url, pasta_destino):
    """Baixa um arquivo PDF e salva na pasta de destino"""
    nome_arquivo = os.path.join(pasta_destino, url.split('/')[-1])
    
    try:
        resposta = requests.get(url, stream=True)
        resposta.raise_for_status()
        
        with open(nome_arquivo, 'wb') as arquivo:
            for chunk in resposta.iter_content(chunk_size=8192):
                arquivo.write(chunk)
        
        print(f"Arquivo baixado: {nome_arquivo}")
        return nome_arquivo
    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")
        return None

def compactar_arquivos(pasta, arquivos, nome_zip):
    """Compacta os arquivos em um ZIP"""
    caminho_zip = os.path.join(pasta, nome_zip)
    
    with zipfile.ZipFile(caminho_zip, 'w') as zipf:
        for arquivo in arquivos:
            if arquivo and os.path.exists(arquivo):
                zipf.write(arquivo, os.path.basename(arquivo))
    
    print(f"Arquivos compactados em: {caminho_zip}")
    return caminho_zip

def main():
    url_base = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    pasta_downloads = "downloads_ans"
    nome_zip = "anexos_ans.zip"
    
    criar_pasta(pasta_downloads)
    
    try:
        print(f"Acessando a página: {url_base}")
        resposta = requests.get(url_base)
        resposta.raise_for_status()
        
        soup = BeautifulSoup(resposta.text, 'html.parser')   
        links_pdf = []
        for link in soup.find_all('a', href=True):
            href = link['href'].lower()
            if href.endswith('.pdf') and ('anexo i' in link.text.lower() or 'anexo ii' in link.text.lower()):
                url_completa = urljoin(url_base, link['href'])
                links_pdf.append(url_completa)
                print(f"Encontrado PDF: {link.text.strip()} - {url_completa}")       
        arquivos_baixados = []
        for url_pdf in links_pdf[:2]:  # Pegar apenas os 2 primeiros (Anexo I e II)
            arquivo = baixar_pdf(url_pdf, pasta_downloads)
            if arquivo:
                arquivos_baixados.append(arquivo)
                       
        if arquivos_baixados:
            caminho_zip = compactar_arquivos(pasta_downloads, arquivos_baixados, nome_zip)
            print("Processo concluído com sucesso!")
            print(f"Arquivo ZIP criado em: {os.path.abspath(caminho_zip)}")
        else:
            print("Nenhum arquivo PDF foi baixado.")
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
    