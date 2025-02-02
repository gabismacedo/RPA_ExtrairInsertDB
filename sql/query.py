import pyodbc
import os
from sql.config import sql_driver, server, database, sql_user, sql_password
import pandas as pd

# conecta no sql
def conectar29():
    conexao29 = f"""DRIVER={sql_driver};
                SERVER={server};
                DATABASE={database};
                UID={sql_user};
                PWD={sql_password}"""
    conexao = pyodbc.connect(conexao29)
    return conexao

cursor = conectar29().cursor()

def manipulacaoExcel():
    # encontrar pasta que está o excel
    caminho_pasta = "C:/Users/40417495/OneDrive - Telefonica/projetos/RPA/RPA_EXTRACAO_INFOB2B"
    lista_arquivos = os.listdir(caminho_pasta) # lista todos os arquivos dentro da pasta

    # cria uma lista com todos os arquivos que contém o nome RelatorioInfoB2B_
    arquivos = [file for file in lista_arquivos if file.startswith("RelatorioInfoB2B_")]
    
    for arquivo in arquivos:
        caminho_completo_arquivo = os.path.join(caminho_pasta, arquivo) # uni o caminho da pasta, com o nome completo do arquivo
        df = pd.read_csv(caminho_completo_arquivo, encoding='iso-8859-1', sep=';', dtype=str)
        df = df.where(pd.notnull(df), '') # trocar os valores NaN para '' (vazio)
       
        df['DOCUMENTO'] = df['DOCUMENTO'].apply(lambda x: '{:.0f}'.format(float(x.replace(',', '.'))) if 'E+' in x else x)
          
        leitura = "SELECT * FROM FSUB.BLOQUEIOS_FSUB"
        sql_data = pd.read_sql(leitura, conectar29())

        sql_data = sql_data.astype(str)

        diff_data = df.merge(sql_data, on=list(df.columns), how='left', indicator=True)
        inserir_dados = diff_data[diff_data['_merge']== 'left_only']

        for row in  inserir_dados.itertuples():
            cursor.execute("""
                INSERT INTO FSUB.BLOQUEIOS_FSUB (
                ANOMES_ATIVACAO,
                DT_HABILITACAO_SUBSCRICAO,
                DOCUMENTO,
                CONTA,
                LINHA,
                MES_BLOQUEIO,
                DT_BLOQUEIO,
                ADABAS_ATIVACAO,
                PLANO,
                LOGIN_ALTA,
                STATUS_LINHA,
                UF_LINHA,
                PRODUTO,
                FL_APARELHOS,
                NM_APARELHOS,
                VALOR_APARELHO,
                FL_DESBLOQUEIO,
                STATUS_LINHA_FINAL,
                STATUS_ENTREGA_FINAL,
                STATUS_PORTADILIDADE)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, 
                row.ANOMES_ATIVACAO,
                row.DT_HABILITACAO_SUBSCRICAO,
                row.DOCUMENTO,
                row.CONTA,
                row.LINHA,
                row.MES_BLOQUEIO,
                row.DT_BLOQUEIO,
                row.ADABAS_ATIVACAO,
                row.PLANO,
                row.LOGIN_ALTA,
                row.STATUS_LINHA,
                row.UF_LINHA,
                row.PRODUTO,
                row.FL_APARELHOS,
                row.NM_APARELHOS,
                row.VALOR_APARELHO,
                row.FL_DESBLOQUEIO,
                row.STATUS_LINHA_FINAL,
                row.STATUS_ENTREGA_FINAL,
                row.STATUS_PORTADILIDADE
            )
        cursor.commit()
        print("dados inseridos")
   
    for arquivo in arquivos:
        os.remove(os.path.join(caminho_pasta, arquivo))
        
