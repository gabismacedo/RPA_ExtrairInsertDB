# IMPORTAR TODAS AS FUNÇÕES CRIADAS
from captcha.utils.captcha_breaker import *
from variables import *
from funcoes.entrar_portal import *
from funcoes.mover_arquivo_baixado import *
from crack_reCaptcha.reCaptcha import *
from sql.query import *


def rpa_extracao_info_b2b():
    solve_text_captcha(driver, url_portal)
    login_portal()
    entrar_relatorio()
    reCaptcha_solver()
    preencher_campos()
    filtro_hierarquia()
    mover_arquivo_baixado()
    conectar29()
    manipulacaoExcel()



