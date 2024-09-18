import requests
import json
import logging
import os

# Configuração do Logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Categoria:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

class APIClient:
    def __init__(self):
        self.session = requests.Session()
        self.configurar_cookies()

    def configurar_cookies(self):
        self.session.cookies.update({
            '_vwo_uuid_v2': 'DD949644AE5BE7D500C21658AEC9D867C|1421f3a5b1621a420a1512b34e5a6d73',
            '_gcl_au': '1.1.1410600072.1725880470',
            '_ga': 'GA1.1.481395908.1725880470',
            '_vwo_uuid': 'DD949644AE5BE7D500C21658AEC9D867C',
            '_vwo_ds': '3%241725880501%3A31.80391157%3A%3A',
            '_vis_opt_s': '1%7C',
            '_vis_opt_test_cookie': '1',
            '_pm_id': '478601725880470587',
            '_vis_opt_exp_8_combi': '2',
            '_vis_opt_exp_19_combi': '1',
            '_fbp': 'fb.1.1725880471098.11370717976230501',
            '_vis_opt_exp_44_combi': '2',
            '_tt_enable_cookie': '1',
            '_ttp': '-VhEoWlLePN2BaJZevVKk2Wh69J',
            'nav_id': 'd214cf51-d727-4510-ad66-1c4c60de560f',
            'legacy_p': 'd214cf51-d727-4510-ad66-1c4c60de560f',
            'chaordic_browserId': 'd214cf51-d727-4510-ad66-1c4c60de560f',
            'legacy_c': 'd214cf51-d727-4510-ad66-1c4c60de560f',
            'legacy_s': 'd214cf51-d727-4510-ad66-1c4c60de560f',
            'chaordic_anonymousUserId': 'anon-d214cf51-d727-4510-ad66-1c4c60de560f',
            'chaordic_testGroup': '%7B%22experiment%22%3Anull%2C%22group%22%3Anull%2C%22testCode%22%3Anull%2C%22code%22%3Anull%2C%22session%22%3Anull%7D',
            'lx_sales_channel': '%5B%22default%22%5D',
            'measurement_id': 'G-DNPEEEHPNE',
            'voxusmediamanager_registered_first_page': 'true',
            '_vis_opt_exp_8_goal_1': '1',
            'aceite_politicas_cookie': '2024-09-09%2008:23:41',
            '_ga_5LTWWHFGYX': 'GS1.1.1725880471.1.0.1725881703.60.0.0',
            '_uetsid': 'af88f3d06e9c11ef8826d991dbb6434e',
            '_uetvid': 'af8908f06e9c11ef8e36cd38e57e7dac',
            '_ga_DNPEEEHPNE': 'GS1.1.1725880470.1.1.1725882465.0.0.0',
            '_vwo_sn': '6602%3A%3A%3A%3A1',
            '_pm_m': 'c04502445000120',
            'ccw': '2 3 39 94 147 235 798 831',
            'CPL': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJpbmZyYWNvbW1lcmNlLmNvbS5iciIsInN1YiI6IkluZnJhY29tbWVyY2UiLCJhdWQiOiJjb21wcmEtYWdvcmEuY29tIiwiaWF0IjoxNzI1ODg3MTkxLCJkYXRhIjp7InVpZCI6IndPdmN1dzZDeFNsYlpOWHI3MDFQelE9PSJ9fQ.P5FoOBS5uVhH3--CsR1_R-OWrKjDiMX27ihSUOcUMgRigmGl9rGFWB-NiYsh8c5UnwGacxCHJRi5YYuOKiqmP-xzvdjr2loTuWHy350y7fCWWqQVk7uU9xAXn3e9pb-BvPykjokiUMdP8LBjRjIEosTOXDrAFzSuZ0pxGD-86huBluS-_w5xtAmURaDNtMGRxWMunsQHYcfO4zfFeVyH9HEPGSH4JSfbC3vqxvr3Fl2rHVOL3Jx8GQ1dvKBKaOyrQC0b62x7zfoanCYTaXfeiFFLJnqo18Rwk8MGuHQHOrZ4Utw7I-r6BAS_0wW_2gkf-EWbMk3EBRdVTnQVJROcmw',
            'usrfgpt': '045024450001201725887191',
            'PHPSESSID': 'i6pdc9c9dt41l50iaatanfj8gc',
            'shownModalAprovacaoVendedoresPendentes': 'false',
            'mp_374315cbd6a8184d0bcfdd0f2a579e0e_mixpanel': '%7B%22distinct_id%22%3A%20113953%2C%22%24device_id%22%3A%20%22191d67e0ab152d-00bded612d592f-26001151-e1000-191d67e0ab152d%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24user_id%22%3A%20113953%7D'
        })

    def obter_dados(self, categoria):
        pagina = 1
        dados_completos = []

        while True:
            # Definir a URL para a página atual
            url = f'https://www.compra-agora.com/api/catalogproducts/{categoria.nome}/{categoria.codigo}?ordenacao=0&limit=24&p={pagina}&filtro_principal=p'
            
            # Fazer uma solicitação autenticada para a URL protegida
            response = self.session.get(url)
            
            # Verificar se a solicitação foi bem-sucedida
            if response.status_code != 200:
                logger.error(f"Falha ao acessar a API: {response.status_code}")
                break
            
            dados_pagina = response.json()
            
            # Adicionar os dados da página atual à lista de dados completos
            dados_completos.extend(dados_pagina.get('produtos', []))
            
            # Verificar se há mais páginas para processar
            if pagina >= dados_pagina.get('paginacao', {}).get('PaginasTotal', 1):
                break
            
            # Passar para a próxima página
            pagina += 1
        
        return dados_completos

class ProdutoProcessor:
    def __init__(self, produtos):
        self.produtos = produtos

    def processar(self):
        produtos_list = []
        
        for produto in self.produtos:
            produto_info = {
                'Descricao': produto.get('Nome', 'N/A'),
                'Descricao_fabricante': produto.get('Fabricante', 'N/A'),
                'imagem_url': produto.get('Foto', 'N/A')
            }
            produtos_list.append(produto_info)
        
        return produtos_list

class DadosSalvador:
    def __init__(self, resultado, nome_arquivo):
        self.resultado = resultado
        self.nome_arquivo = nome_arquivo

    def salvar(self):
        with open(self.nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(self.resultado, f, ensure_ascii=False, indent=4)
        logger.info(f"Dados salvos em {self.nome_arquivo}")

def main():
    # Criar a pasta 'json'
    os.makedirs('json', exist_ok=True)
    
    # Definindo diretamente uma lista de categorias
    categorias_codigos = [
        Categoria('destaques', '1458'),
        Categoria('alimentos', '800'),
        Categoria('bazar', '344'),
        Categoria('bebidas', '778'),
        Categoria('bomboniere', '183'),
        Categoria('cuidados-pessoais', '180'),
        Categoria('pet', '215'),
        Categoria('roupa-e-casa', '179'),
        Categoria('sorvetes', '258')
    ]

    api_client = APIClient()
    
    for categoria in categorias_codigos:
        logger.info(f"Obtendo dados para a categoria {categoria.nome} ({categoria.codigo})")
        
        # Obter todos os dados paginados
        produtos = api_client.obter_dados(categoria)
        
        # Processar os produtos
        processor = ProdutoProcessor(produtos)
        produtos_list = processor.processar()
        
        # Criar um dicionário com a lista de produtos
        resultado = {categoria.nome: produtos_list}
        
        # Salvar os dados em um arquivo JSON
        salvador = DadosSalvador(resultado, f'json/{categoria.nome}.json')
        salvador.salvar()
        
        logger.info(f"Dados da categoria {categoria.nome} foram processados e salvos com sucesso")

if __name__ == "__main__":
    main()
