from funcoes.wait_for_element import *
from variables import *
import time
import random 

# LOGIN NO INFO

def digitar_devagar(element, texto):
    for digitacao in texto:
        element.send_keys(digitacao)
        time.sleep(random.uniform(0.05, 0.2))  # Atraso aleatório entre 50ms e 200ms

def login_portal():
    # MAXIMIZAR JANELA QUE ESTÁ ABERTA

    # INPUT DE LOGIN
    login_input = wait_for_element(driver, '/html/body/div[2]/div/main/div/form/fieldset/input[2]')
    digitar_devagar(login_input, login)
    time.sleep(random.uniform(1, 5))
    
    # INPUT DE SENHA
    senha_input = wait_for_element(driver, '/html/body/div[2]/div/main/div/form/fieldset/input[3]')
    digitar_devagar(senha_input, senha)
    
    # BOTÃO ENTRAR
    botao = wait_for_element(driver, '/html/body/div[2]/div/main/div/form/fieldset/input[4]')
    botao.click()
    print("fez o login")
    time.sleep(random.uniform(3, 7))

    # CLICA NO MENU
def entrar_relatorio():
    # ENTRAR NO MENU
    menu_hamburger = wait_for_element(driver, '/html/body/app-root/div/div/div/app-header/nav/label')
    menu_hamburger.click()
    time.sleep(random.uniform(1, 5))

    opcao_relatorio = wait_for_element(driver, '/html/body/app-root/div/div/div/app-header/nav/ol/div/div/div[1]/li[3]/ol[8]/li[1]/a')
    opcao_relatorio.click()
    
    print("clicou no menu")
    time.sleep(5)
    
def preencher_campos():
    print("entrou na função")
    # PREENCHER CAMPO TIPO RELATORIO
    tipo_relatorio = wait_for_element(driver, '/html/body/app-root/div/div/div/div/div/div/app-relatorio-flow/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div/div/div[1]/div/ng-select/div')
    tipo_relatorio.click()
    time.sleep(random.uniform(1, 5))

    opcao_dashboard = wait_for_element(driver, '/html/body/app-root/div/div/div/div/div/div/app-relatorio-flow/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div/div/div[1]/div/ng-select/ng-dropdown-panel/div/div[2]/div[2]')
    opcao_dashboard.click()
    time.sleep(random.uniform(1, 5))

    # PREENCHER CAMPO FUNCIONALIDADE
    funcionalidade = wait_for_element(driver, '/html/body/app-root/div/div/div/div/div/div/app-relatorio-flow/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div/div/div[2]/div/ng-select/div')
    funcionalidade.click()
    time.sleep(random.uniform(1, 5))

    opcao_qualidade = wait_for_element(driver, '/html/body/app-root/div/div/div/div/div/div/app-relatorio-flow/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div/div/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]/div[3]')
    opcao_qualidade.click()
    time.sleep(random.uniform(1, 5))

    # PREENCHER CAMPO RELATÓRIO
    relatorio = wait_for_element(driver, '/html/body/app-root/div/div/div/div/div/div/app-relatorio-flow/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div/div/div[3]/div/ng-select/div')
    relatorio.click()
    time.sleep(random.uniform(1, 5))

    opcao_fraude = wait_for_element(driver, '/html/body/app-root/div/div/div/div/div/div/app-relatorio-flow/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div/div/div[3]/div/ng-select/ng-dropdown-panel/div/div[2]/div[3]')
    opcao_fraude.click()
    time.sleep(random.uniform(1, 5))

    # PREENCHER CAMPO DATA
    selecionar_data = wait_for_element(driver, '/html/body/app-root/div/div/div/div/div/div/app-relatorio-flow/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div/div/div[5]/div/ng-select/div')
    selecionar_data.click()
    time.sleep(random.uniform(1, 5))

    periodo_relatorio = wait_for_element(driver, '/html/body/app-root/div/div/div/div/div/div/app-relatorio-flow/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div/div/div[5]/div/ng-select/ng-dropdown-panel/div/div[2]/div')
    periodo_relatorio.click()
    time.sleep(random.uniform(1, 5))

    # PREENCHER CAMPO MÊS
    opcao_mes = wait_for_element(driver, '/html/body/app-root/div/div/div/div/div/div/app-relatorio-flow/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div/div/div[6]/div/div/ng-select/div')
    opcao_mes.click()
    time.sleep(random.uniform(1, 5))

    mes_atual = wait_for_element(driver, '/html/body/app-root/div/div/div/div/div/div/app-relatorio-flow/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div/div/div[6]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[2]')
    mes_atual.click()
    time.sleep(random.uniform(1, 5))

    print("preencheu os campos")

# APLICAR OS FILTROS
def filtro_hierarquia():

    # FILTRO HIERARQUIA
    filtro_hierarquia = wait_for_element(driver,
                                    '/html/body/app-root/div/div/div/div/div/div/app-relatorio-flow/div/div/div[1]/div[2]/div[2]')
    filtro_hierarquia.click()
    time.sleep(random.uniform(1, 5))

    print("clicou no filtro")
    # ADICIONAR O FILTRO
    adicionar_filtro = wait_for_element(driver,
                                    '/html/body/app-root/div/div/div/div/div/div/app-relatorio-flow/div/div/div['
                                     '1]/div[2]/div[2]/div/app-filtro-hierarquia/form/ul/li[1]/span/i')
    adicionar_filtro.click()
    print("clicou no mais")
    time.sleep(random.uniform(1, 5))

    # TIPO DE SEGMENTO
    segmento = wait_for_element(driver, '/html/body/app-root/div/div/div/div/div/div/app-relatorio-flow/div/div/div['
                                     '1]/div[2]/div[2]/div/app-filtro-hierarquia/form/ul/li[2]/div/ng-select/div')
    segmento.click()
    print("colocou o segmento")
    time.sleep(random.uniform(1, 5))

    # SELECIONAR OPÇÃO VENDA INDIRETA
    venda_indireta = wait_for_element(driver,
                                    '/html/body/app-root/div/div/div/div/div/div/app-relatorio-flow/div/div/div[1]/div[2]/div[2]/div/app-filtro-hierarquia/form/ul/li[2]/div/ng-select/ng-dropdown-panel/div/div[2]/div[2]')
    venda_indireta.click()
    print("clicou em vendas indiretas")
    time.sleep(random.uniform(1, 5))

    # SELECIONAR O DIRETOR
    diretor_regional = wait_for_element(driver, '/html/body/app-root/div/div/div/div/div/div/app-relatorio-flow/div/div/div[1]/div[2]/div[2]/div/app-filtro-hierarquia/form/ul/li[4]/div/ng-select/div')
    diretor_regional.click()
    print("clicou no diretor regional")
    time.sleep(random.uniform(1, 5))

    diretor = wait_for_element(driver, '/html/body/app-root/div/div/div/div/div/div/app-relatorio-flow/div/div/div[1]/div[2]/div[2]/div/app-filtro-hierarquia/form/ul/li[4]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]') #'/html/body/app-root/div/div/div/div/div/div/app-relatorio-flow/div/div/div[1]/div[2]/div[2]/div/app-filtro-hierarquia/form/ul/li[4]/div/ng-select/ng-dropdown-panel/div/div[2]/div[1]')
    diretor.click()
    print("clicou no diretor")
    time.sleep(random.uniform(1, 5))

    # BOTÃO PARA APLICAR O FILTRO
    botao_aplicar_filtro = wait_for_element(driver, '/html/body/app-root/div/div/div/div/div/div/app-relatorio-flow/div/div/div[1]/div[2]/div[2]/div/div/ul/li[2]/button[1]')
    botao_aplicar_filtro.click()
    print("clicou botao do aplicar filtro")
    time.sleep(random.uniform(1, 5))

    # BOTÃO PARA GERAR O RELATÓRIO
    botao_gerar_relatorio = wait_for_element(driver, '/html/body/app-root/div/div/div/div/div/div/app-relatorio-flow/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div/div/div[8]/div/button')
    botao_gerar_relatorio.click()
    time.sleep(random.uniform(1, 5))
    print("fez os filtros")
    time.sleep(20)










