import pandas as pd
import os

pasta_destino = 'C:/Users/40417495/Telefonica/GERENCIA DE PROJETOS E EXPERIÊNCIA COMERCIAL - Documentos/001. ' \
                       'Eficiência Jurídica e Ecossistemas/008. BASE PBI/Relatórios gerados portal InfoB2B'

def tranformar_texto_numero(caminho_pasta, nome_coluna):
    df = pd.read_excel(caminho_pasta)
    if nome_coluna in df.columns:
        df[nome_coluna] = df[nome_coluna].astype(str)
        df.to_excel(caminho_pasta, index=False)

arquivo = os.listdir(pasta_destino)

for nome_arquivo in arquivo:
    if nome_arquivo.endswith('.xlsx'):
        caminho_pasta = os.path.join(pasta_destino, nome_arquivo)
        tranformar_texto_numero(caminho_pasta, '')

