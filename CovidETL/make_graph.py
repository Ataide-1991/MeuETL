import pandas as pd
import matplotlib.pyplot as plt
import logging

logger = logging.getLogger(__name__)


class MakeGraph:
    """
    Por padrão o nome do arquivo ja esta declarado. Caso você
    altere o nome na variavel no método write, deverá
    passar o mesmo nome ao instânciar esse objeto
    
    MakeGraph.process_state(file_name = 'meu_nome_alterado')
    ou
    MakeGraph.process_country(file_name = 'meu_nome_alterado')
    """

    @staticmethod
    def data(df, key: str, column):
        data=dict()
        df = df.sort_values(by=column, ascending=False).head(10)
        data['process'] = df[f'{key}'].values.tolist()
        data['dados'] = df[column].values.tolist()
        return data

    @classmethod
    def process_state(cls, file_name: str = 'casos_Todos_estados'):
        if file_name is None or not isinstance(file_name, str):
            raise TypeError('File name must be string!')
        df = pd.read_csv(f'{file_name}.csv')
        use_graph = list()
        use_graph = [column for column in df.columns[3:7]]

        for column in use_graph:
            # data
            data = cls.data(df, key='UF', column=column)

            # graph details
            window = plt.figure(figsize=(15, 7))
            plt.title(
                f'Os 10 estados com mais {column}', weight='bold', fontsize='30')
            plt.ylabel('Escala', weight='bold')
            plt.xticks(rotation=20)
            result = plt.bar(x=data['process'], height=data['dados'], label=column, color='red')
            plt.bar_label(result, padding=2)
            plt.grid()
            plt.savefig(f'grafico_estado_{column}.png')
        logger.info('Gráficos gerados!')


    @classmethod
    def process_country(cls,file_name: str = 'casos_Todos_paises'):
        if file_name is None or not isinstance(file_name, str):
            raise TypeError('File name must be string!')
        df = pd.read_csv(f'{file_name}.csv')
        use_graph = list()
        use_graph = [column for column in df.columns[1:3]]
        
        for column in use_graph:
            # data
            data = cls.data(df, key='País', column=column)

            # graph details
            window = plt.figure(figsize=(15, 7))
            plt.title(
                f'Os 10 países com mais {column}', weight='bold', fontsize='30')
            plt.ylabel('Escala', weight='bold')
            plt.xticks(rotation=20)
            result = plt.bar(x=data['process'], height=data['dados'], label=column, color='purple')
            plt.bar_label(result, padding=2)
            plt.grid()
            plt.savefig(f'grafico_pais_{column}.png')
        logger.info('Gráficos gerados!')
