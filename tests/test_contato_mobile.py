
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


URL = "https://iterasys.learnworlds.com/"


def test_linkedin_mobile(driver, wait):
    driver.get(URL)

    # Localizar o botão do LinkedIn
    linkedin = wait.until(
        EC.presence_of_element_located(
            (By.ID, "el_1645035537528_322")
        )
    )

    # Rolar até o botão
    driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
        linkedin
    )

    # Aguardar que fique clicável
    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "el_1645035537528_322")
        )
    )

    # Registrar as abas existentes
    abas_antes = driver.window_handles

    # Clicar no LinkedIn
    linkedin.click()

    # Verificar se abriu uma nova aba ou mudou a URL
    try:
        wait.until(EC.new_window_is_opened(abas_antes))

        nova_aba = next(
            aba for aba in driver.window_handles
            if aba not in abas_antes
        )
        driver.switch_to.window(nova_aba)

        wait.until(
            lambda d: "linkedin.com" in d.current_url.lower()
        )

    except Exception:
        # Caso a navegação ocorra na mesma aba
        assert "linkedin.com" in driver.current_url.lower()
