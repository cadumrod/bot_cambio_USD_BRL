import sys
import os
from cx_Freeze import setup, Executable

arquivos = ['hyperlink.py', 'business.ico']

config = Executable(
    script='app.py',
    icon='business.ico'
)

setup(
    name='Monitoramento de cambio USD_BRL',
    version='1.0',
    description='Este programa realiza o monitoramento da cotação atual do dólar para real, salva as informações juntamente com um print em um arquivo .docx e converte para um arquivo .pdf.',
    author='Carlos Rodrigues',
    options={'build_exe': {'include_files': arquivos}},
    executables=[config]
)
