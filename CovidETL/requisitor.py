import requests
import logging


logger = logging.getLogger(__name__)  # contém o nome do módulo

# seta mensagens de info (erros, warnings, critical)
logger.setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO)


class Check:
    @classmethod
    def check_api(cls, url=None):
        url = url or 'https://covid19-brazil-api.now.sh/api/status/v1'
        request = requests.get(url)
        if request.status_code != 200:
            logger.warning('API fora do ar.')
            return False
        logger.info('API ON!')
        return True


class CovidBrasil():
    def __init__(self):
        self.__url = 'https://covid19-brazil-api.now.sh/api/report/v1'
        self.requested_list = []

    def requisita_estados(self):
        if Check.check_api():
            # Lista casos por estado
            request = requests.get(self.__url).json()
            self.requested_list = request['data']
            return self.requested_list



class CovidMundo():
    def __init__(self):
        self.__url = 'https://covid19-brazil-api.now.sh/api/report/v1/countries'
        self.requested_list = list()

    def requisita_paises(self):
        if Check.check_api():
            # Lista de todos os países
            request = requests.get(self.__url).json()
            self.requested_list = request['data']
            return self.requested_list
