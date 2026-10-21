# 📱 Automação de Testes Mobile — Iterasys LearnWorlds

## 📌 Sobre o projeto

Este projeto tem como objetivo aplicar conhecimentos de **Quality Assurance (QA)** e automação de testes na plataforma [Iterasys LearnWorlds](https://iterasys.learnworlds.com/).

Foram elaborados **5 casos de teste e seus critérios de aceitação**, dos quais **3 foram automatizados** utilizando Python e Selenium WebDriver. A automação mobile foi desenvolvida com a emulação de um **iPhone 16 no Google Chrome**.

## 🎯 Objetivos

- Validar funcionalidades importantes da plataforma.
- Automatizar cenários de teste utilizando Selenium WebDriver.
- Verificar o comportamento da aplicação em uma interface mobile.
- Aplicar boas práticas de localização e interação com elementos web.
- Identificar dificuldades de automação e desenvolver soluções técnicas.

## 🧪 Casos de teste

Foram elaborados cinco casos de teste, com seus respectivos critérios de aceitação.

Entre os cenários automatizados estão:

- **Login:** preenchimento das credenciais e validação do acesso à plataforma.
- **Página de cursos:** navegação até a página de cursos e validação do conteúdo apresentado.
- **Contato:** validação do cenário de contato definido no projeto.

**Resultado do planejamento:**
- 5 casos de teste elaborados.
- 3 casos de teste automatizados.

## 🛠️ Tecnologias utilizadas

- **Python** — linguagem utilizada no desenvolvimento dos scripts.
- **Selenium WebDriver** — automação da interação com elementos web.
- **Pytest** — execução e organização dos testes automatizados.
- **Google Chrome** — navegador utilizado na execução.
- **Mobile Emulation** — simulação de um dispositivo iPhone 16.

## 📱 Automação mobile

O teste de login foi adaptado para executar em uma interface mobile, utilizando a emulação de um iPhone 16 no Chrome.

O fluxo automatizado contempla:

1. Acessar a plataforma Iterasys LearnWorlds.
2. Abrir o menu de navegação mobile.
3. Localizar e selecionar a opção de login.
4. Preencher os campos de e-mail e senha.
5. Acionar o botão de entrada.
6. Validar o login bem-sucedido por meio de um elemento da página.

A emulação permite observar como a interface se comporta em um formato de tela semelhante ao de um dispositivo móvel. Ela não representa uma execução em um iPhone físico ou no Safari real.

## ⚠️ Principais desafios encontrados

### 1. Localização dos seletores

Uma das maiores dificuldades durante a automação mobile foi identificar os seletores corretos para interagir com os elementos da página.

Alguns elementos não respondiam aos cliques convencionais do Selenium, exigindo o uso de JavaScript para executar determinadas interações.

Exemplo:

```python
driver.execute_script("arguments[0].click();", elemento)
```

Essa abordagem foi utilizada quando necessário para realizar cliques em elementos específicos da interface.

### 2. Mudança dos elementos entre layouts

Outro desafio foi perceber que alguns seletores e elementos da navegação mudavam conforme o tamanho da tela e o layout apresentado pela aplicação.

Seletores utilizados na versão desktop nem sempre funcionavam na versão mobile. Por isso, foi necessário inspecionar o HTML da página e adaptar os seletores para elementos específicos do menu mobile.

Esse processo reforçou a importância de analisar o DOM e validar os seletores no contexto real de execução do teste.

## ▶️ Como executar os testes

### Pré-requisitos

- Python instalado.
- Google Chrome instalado.
- Selenium e Pytest instalados.
- ChromeDriver compatível com o navegador, conforme o ambiente utilizado.

Instale as dependências:

```bash
pip install selenium pytest
```

Configure as credenciais de teste no PowerShell:

```powershell
$env:ITERASYS_EMAIL="seu-email"
$env:ITERASYS_PASSWORD="sua-senha"
```

Execute o teste de login mobile:

```bash
python -m pytest -v -s tests/test_login_mobile.py
```

Execute o teste de cursos mobile:

```bash
python -m pytest -v -s tests/test_cursos_mobile.py
```

Para executar todos os testes da pasta:

```bash
python -m pytest -v tests/
```

> **Importante:** configure suas credenciais por variáveis de ambiente e não inclua senhas reais nos arquivos do projeto ou no repositório.

## 📚 Aprendizados

O desenvolvimento deste projeto contribuiu para o aprendizado prático de:

- Construção e execução de testes automatizados com Python e Selenium.
- Organização de testes utilizando Pytest.
- Inspeção de elementos HTML e criação de seletores CSS e XPath.
- Interação com menus responsivos e formulários de login.
- Utilização de JavaScript para contornar dificuldades específicas de interação.
- Identificação das diferenças entre layouts desktop e mobile.
- Depuração de falhas por meio da análise de exceções e logs de execução.

## 👨‍💻 Considerações finais

Este projeto representa uma etapa prática da minha formação em Quality Assurance, permitindo aplicar conceitos de testes funcionais e automação web em uma plataforma real.

Durante o desenvolvimento, enfrentei desafios relacionados à localização de elementos e às diferenças entre os layouts desktop e mobile. A investigação do HTML, a adaptação dos seletores e o uso pontual de JavaScript foram importantes para avançar na implementação dos testes.

O projeto também proporcionou experiência na validação de fluxos de navegação e na execução de testes utilizando emulação mobile.

---

**Projeto desenvolvido como parte dos estudos em Quality Assurance (QA).**
