import scrapy
import json

class RaspagemSpider(scrapy.Spider):
    name = "Raspagem"
    start_urls = ['https://pedidoeletronico.servimed.com.br/login']

    def start_requests(self):
        url = 'https://peapi.servimed.com.br/api/usuario/login'

        body = {
            'usuario': 'juliano@farmaprevonline.com.br',
            'senha': 'a007299A'
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        yield scrapy.Request(
            url,
            method='POST',
            body=json.dumps(body),
            headers=headers,
            callback=self.after_login,
            meta={'dont_merge_cookies': True}  # Não mescla cookies
        )

    def after_login(self, response):
        # Verifique se o login foi bem-sucedido
        if response.status == 200:
            self.log('Login bem-sucedido!')
            
            # Armazene os cookies da resposta
            cookies = response.headers.getlist('Set-Cookie')

            self.log('\n'*4)
            self.log('Dados de headers')
            self.log(response.headers)
            self.log('\n'*4)
            self.log('Dados de body')
            self.log(response.body)
            self.log('\n'*4)
            self.log('Dados de meta')
            self.log(response.meta)
            self.log('\n'*4)
            self.log('Dados de request')
            self.log(response.request)
            self.log('\n'*4)

            url = 'https://peapi.servimed.com.br/api/Pedido'

            # falta localizar aonde posso pegar essa info
            access_token = '4faaaf60-7116-11ef-b91a-a34a4ef4d85b'

            body =  {
                "dataInicio":"",
                "dataFim":"",
                "filtro":"",
                "pagina":1,
                "registrosPorPagina":10,
                "codigoExterno":response.json()['usuario']['codigoExterno'],
                "codigoUsuario":response.json()['usuario']['codigoUsuario'],
                "kindSeller":0,
                "users":[response.json()['usuario']['users'][0],response.json()['usuario']['users'][0]]
            }

            headers = {
                'loggedUser':  response.json()['usuario']['codigoUsuario'],
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json',
                'contentType': 'application/json',
                'Accept': 'application/json, text/plain, */*',
            }

            yield scrapy.Request(
                url,
                method='POST',
                headers=headers,
                body=json.dumps(body),
                cookies=self.convert_cookies(cookies),
                callback=self.parse_data)
            
        else:
            self.log('Falha no login.')

    def parse_data(self,response):
        tokennn= response.css('script::text')#.re_first(r'"accessToken":"(\w+)"')

        self.log(tokennn)        
        self.log(response.text)  
    
    def convert_cookies(self, cookies_list):
        # Converta a lista de cookies em um dicionário
        cookies_dict = {}
        for cookie in cookies_list:
            cookie_str = cookie.decode('utf-8')
            cookie_parts = cookie_str.split(';')[0].split('=')
            cookies_dict[cookie_parts[0]] = cookie_parts[1]
        return cookies_dict
    def parse_pedidos(self, response):
        # Lógica para processar a resposta dos pedidos
        pass