import os


def make_dir(file_name):
    os.makedirs(f'{os.getcwd()}/{file_name}', exist_ok=True)
    return os.chdir(f'{os.getcwd()}/{file_name}')
