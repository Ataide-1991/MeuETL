import logging
import pandas as pd
from .make_dir import make_dir

logger = logging.getLogger(__name__)  # contém o nome do módulo


class Writer:
    """
        Por padrão o nome do arquivo ja esta declarado.
        Você pode passar seu proprio nome,
        mas lembre-se: você deve passar o mesmo nome
        no metodo do objeto 'makeGraph', e,
        cada nome diferente, uma nova pasta também será criada.
        """

    HEADER_STATES = ['id','UF', 'Estado', 'Casos confirmados',
                     'Mortes', 'Suspeitos', 'Negativados', 'Monitorado até']
    HEADER_COUNTRY = ['País', 'Casos confirmados', 'Mortes', 'Atualizado até']


    @classmethod
    def write_brstates(cls, file_name='casos_Todos_estados', header=HEADER_STATES, contain=None):
        make_dir(file_name)
        logger.info('Diretório criado...')
        df = pd.DataFrame(contain)
        df.columns = header
        df.to_csv(f'{file_name}.csv', index=False)
        logger.info('Gravado em csv com sucesso!')


    @classmethod
    def write_allcountries(cls, file_name='casos_Todos_paises', header=HEADER_COUNTRY, contain=None):
        make_dir(file_name)
        logger.info('Diretório criado...')
        df = pd.DataFrame(contain)
        df.drop(columns=['cases', 'recovered'],inplace=True) # colunas vazias(None)
        df.columns = header
        df.to_csv(f'{file_name}.csv', index=False)
        logger.info('Gravado em csv com sucesso!')
