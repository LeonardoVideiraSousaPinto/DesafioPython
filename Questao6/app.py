import logging
import json
import time 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class QuoteScraper:
    def __init__(self, base_url='http://quotes.toscrape.com/'):
        """
        Inicializa o objeto QuoteScraper.

        :param base_url: URL base do site a ser raspado.
        """
        logging.basicConfig(level=logging.INFO)
        logging.info('Inicializando o WebDriver e acessando o site.')
        time.sleep(60)
        # Configuração do Selenium Grid
        selenium_grid_url = 'http://selenium:4444/wd/hub'

        options = Options()
        options.add_argument("--headless")  # Opcional: rodar sem interface gráfica
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        try:
            # Inicializa o WebDriver com as opções do Chrome e URL do Selenium Grid
            self.driver = webdriver.Remote(
                command_executor=selenium_grid_url,
                options=options
            )
            self.base_url = base_url
            self.driver.get(self.base_url)
            self.driver.implicitly_wait(5)  # Espera implícita de 5 segundos
            logging.info(f'Acessando a URL base: {self.base_url}')
        except Exception as e:
            logging.error(f'Erro ao inicializar o WebDriver: {e}')
            raise
    
    def __del__(self):
        """
        Fecha o navegador ao destruir o objeto.
        """
        logging.info('Fechando o WebDriver.')
        self.driver.quit()

    def find_author(self, author_name, output_file='output.json'):
        """
        Encontra as citações e dados de um autor específico e salva em um arquivo JSON.

        :param author_name: Nome do autor a ser pesquisado.
        :param output_file: Nome do arquivo JSON onde os dados serão salvos.
        """
        logging.info(f'Iniciando a busca pelo autor: {author_name}')
        author_data = {
            'Author': {
                'Name': author_name,
                'Birth_date': None,
                'Birth_location': None,
                'Description': None
            },
            'Quotes': []
        }

        while True:
            try:
                elements = self.driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[1]/div')
                logging.debug(f'Encontrados {len(elements)} elementos na página.')

                for element in elements:
                    if author_name.upper() in element.text.upper():
                        logging.info(f'Autor encontrado: {author_name}')
                        if not author_data['Author']['Birth_date']:
                            self.collect_author_data(author_data, element)
                        
                        self.collect_quote_data(author_data, element)
            except Exception as e:
                logging.error(f"Erro ao processar o elemento: {e}")
                continue

            if not self.click_next_page():
                logging.info('Não há mais páginas para acessar.')
                break

        self.save_to_json(output_file, author_data)

    def collect_author_data(self, author_data, element):
        """
        Coleta dados sobre o autor e atualiza o dicionário author_data.

        :param author_data: Dicionário contendo os dados do autor e citações.
        :param element: Elemento da página contendo as informações do autor.
        """
        try:
            logging.info('Coletando dados do autor.')
            element.find_element(By.TAG_NAME, 'a').click()
            author_data['Author']['Birth_date'] = self.driver.find_element(By.CLASS_NAME, 'author-born-date').text
            author_data['Author']['Birth_location'] = self.driver.find_element(By.CLASS_NAME, 'author-born-location').text.replace('in ', '')
            author_data['Author']['Description'] = self.driver.find_element(By.CLASS_NAME, 'author-description').text
            self.driver.back()
        except NoSuchElementException as e:
            logging.error(f"Erro ao encontrar informações do autor: {e}")

    def collect_quote_data(self, author_data, element):
        """
        Coleta dados sobre uma citação e adiciona ao dicionário author_data.

        :param author_data: Dicionário contendo os dados do autor e citações.
        :param element: Elemento da página contendo a citação.
        """
        try:
            logging.info('Coletando dados da citação.')
            quote = {
                'Text': element.find_element(By.CLASS_NAME, 'text').text,
                'Tags': [tag.text for tag in element.find_elements(By.TAG_NAME, 'a') if 'about' not in tag.text]
            }
            author_data['Quotes'].append(quote)
        except NoSuchElementException as e:
            logging.error(f"Erro ao encontrar informações da citação: {e}")

    def click_next_page(self):
        """
        Clica no botão de próxima página se ele existir.
        
        :return: True se a página foi mudada, False caso contrário.
        """
        try:
            next_button = self.driver.find_element(By.XPATH, './/a[contains(text(), "Next")]')
            next_button.click()
            logging.info('Clicando na próxima página.')
            return True
        except NoSuchElementException:
            logging.info('Botão de próxima página não encontrado.')
            return False

    def save_to_json(self, filename, data):
        """
        Salva os dados coletados em um arquivo JSON.

        :param filename: Nome do arquivo JSON.
        :param data: Dados a serem salvos no arquivo.
        """
        logging.info(f'Salvando dados no arquivo {filename}.')
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        logging.info('\n\nDados do json:\n')
        logging.info(data)

if __name__ == "__main__":
    scraper = QuoteScraper()
    scraper.find_author('J.K. Rowling')
