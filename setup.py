import sys
import os
from cx_Freeze import setup, Executable

# Definir o que deve ser incluido na pasta final
arquivos = ['exe.ico', 'dados_usuarios.csv']
# Saída de arquivos
configuracao = Executable(
    script='app.py',
    icon='exe.ico'
)
# Configurar o CX-Freeze (detalhes do programa)
setup(
    name='Automatizador de Cadastro de Usuarios',
    version='1.0',
    description='Este programa automatiza o cadastro de usuarios em um formulario',
    author='Anddre Henrique',
    options={'build_exe': {'include_files': arquivos, 'include_msvcr': True}},
    executables=[configuracao]
)