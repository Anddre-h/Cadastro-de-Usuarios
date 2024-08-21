import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as condicao_esperada

def iniciar_driver():
    chrome_options = Options()

    arguments = ['--lang=pt-BR', '--window-size=1920, 1080', '--incognito']
    # '--headless' = Roda em segundo plano sem abrir a janela

    for argument in arguments:
        chrome_options.add_argument(argument)

    caminho_padrao_para_download = 'E:\\Storage\\Desktop'

    chrome_options.add_experimental_option("prefs", {
        'download.default_directory': caminho_padrao_para_download,
        'download.directory_upgrade': True,
        'download.prompt_for_download': False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.automatic_downloads": 1,
    })
    driver = webdriver.Chrome(options=chrome_options)

    
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ]
    )

    return driver, wait

tabela = pd.read_csv('dados_usuarios.csv', sep=';')

driver, wait = iniciar_driver()
driver.get('https://forms.gle/wrzVrzJC7z6DiqVj9')
driver.maximize_window()
sleep(2)

for index,row in tabela.iterrows():
    if index is not None:
        campo_nome = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//input[@aria-labelledby="i1"]')))
        campo_nome.send_keys(row['Nome'])
        sleep(2)

        campo_email = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//input[@aria-labelledby="i5"]')))
        campo_email.send_keys(row['Email'])
        sleep(2)

        campo_endereço = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//textarea[@aria-labelledby="i9"]')))
        campo_endereço.send_keys(row['Endereço'])
        sleep(2)

        campo_telefone = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//input[@aria-labelledby="i13"]')))
        campo_telefone.send_keys(row['Telefone'])
        sleep(2)

        botao_enviar = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')))
        botao_enviar.click()
        sleep(2)

        driver.refresh()
        sleep(2)
    else:
        print('Todos os usuários foram cadastrados!')
        input('')
        driver.close()