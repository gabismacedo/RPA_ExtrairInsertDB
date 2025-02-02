import os
import shutil
import glob
import zipfile

def mover_arquivo_baixado():
    # PASTA QUE O DOWNLOAD É FEITO
    pasta_baixado = os.path.expanduser('~/Downloads')

    # NOME INICIAL DO ARQUIVO E SUA EXTENSÃO
    nome_pasta = 'InfoB2B_*.zip'

    # ENCONTRA TODOS OS ARQUIVOS NA PASTA DOWNLOAD COM O NOME "InfoB2B_"
    encontrar_arquivos = glob.glob(os.path.join(pasta_baixado, nome_pasta))

    # SE NÃO ENCONTRAR O ARQUIVO RETORNA ESSE PRINT
    if not encontrar_arquivos:
        print('não encontrado')

    # CASO ENCONTRE...
    else:
        # SELECIONA O ARQUIVO MAIS RECENTE
        arquivo_recente = max(encontrar_arquivos, key=os.path.getctime)
        # PASTA ONDE O ARQUIVO SERÁ MOVIDO
        pasta_destino = 'C:/Users/40417495/OneDrive - Telefonica/projetos/RPA/RPA_EXTRACAO_INFOB2B'
        nome_arquivo = os.path.basename(arquivo_recente)
        destino = os.path.join(pasta_destino, nome_arquivo)
        # MOVE ARQUIVO PARA O NOVO DIRETÓRIO
        shutil.move(arquivo_recente, destino)

        # ABRIR E EXTRAIR ARQUIVO ZIPADO
        with zipfile.ZipFile(destino, 'r') as zip_ref:
            zip_ref.extractall(pasta_destino)
            # REMOVE A PASTA ZIPADA E DEIXA APENAS O ARQUIVO
        os.remove(destino)
