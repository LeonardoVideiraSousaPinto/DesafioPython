# settings.py
DOWNLOADER_CLIENT_TLS_METHOD = 'TLS'
DOWNLOADER_CLIENT_TLS_VERBOSE_LOGGING = True
BOT_NAME = "RaspagemScrapy"
SPIDER_MODULES = ["RaspagemScrapy.spiders"]
NEWSPIDER_MODULE = "RaspagemScrapy.spiders"
#DOWNLOAD_DELAY = 10  # Atraso de 3 segundos entre solicitações
ROBOTSTXT_OBEY = True
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

DOWNLOADER_MIDDLEWARES = {
    'RaspagemScrapy.middlewares.RaspagemscrapyDownloaderMiddleware': 543,
    'RaspagemScrapy.middlewares.RequestLoggingMiddleware': 544,  # Adicione o middleware de logging aqui
}
LOG_LEVEL = 'DEBUG'  # Ou 'DEBUG' para informações mais detalhadas
