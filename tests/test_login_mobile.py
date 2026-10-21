
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 


URL = "https://iterasys.learnworlds.com/"


class TestLoginMobile:

    def setup_method(self, method):
        device = {  "deviceName": "iPhone 16"
        }

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(
            "mobileEmulation", device
        )

        self.driver = webdriver.Chrome(chrome_options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 15)

    def teardown_method(self, method):
        self.driver.quit()

    def test_login_mobile(self):
        driver = self.driver
        wait = self.wait

        driver.get(URL)
        time .sleep(2)  # Aguardar a página carregar

        # Abrir o menu mobile
        menu_mobile = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.lw-topbar-hamburger-button")
            )
        )
        menu_mobile.click()
        time .sleep(2)  # Aguardar a animação do menu

        # Clicar em Entrar
        entrar = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
            "//li[contains(@class, 'mobile-nav-menu-item')]"
            "//div[contains(@class, 'mobile-nav-menu-link')]"
            "[.//span[normalize-space()='Entrar']]"
                )
            )
        )
        driver.execute_script("arguments[0].click();", entrar)
        time .sleep(2)  # Aguardar a animação do menu

        # Preencher e-mail
        email = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "signin-email")
            )
        )
        email.send_keys(os.environ["ITERASYS_EMAIL"])
        time .sleep(2)  # Aguardar a digitação do e-mail

        # Preencher senha
        senha = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "signin-password")
            )
        )
        senha.send_keys(os.environ["ITERASYS_PASSWORD"])
        time .sleep(2)  # Aguardar a digitação da senha

        # Aguardar o botão Entrar do formulário
        botao_login = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "button#submitLogin")
            )
        )

        wait.until(
            lambda d: botao_login.is_enabled()
        )

        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            botao_login
        )

        botao_login.click()

        time .sleep(2)  # Aguardar a animação do login

        # Validar login bem-sucedido
        mensagem = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "el_1600856593662_49")
            )
        )

        assert mensagem.text.strip() == (
            "Hi, Swell Henrique da Silva"
        )
        time .sleep(3)  
