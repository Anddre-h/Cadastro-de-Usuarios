import sys
import os
from cx_Freeze import setup, Executable

# Definir o que deve ser incluido na pasta final
arquivos = ['exe.ico', 'dados_usuarios.csv']

# Comando para esconder console em aplicações onde não quer que o console seja exibido
base = None
if sys.plataform == 'Win32':
    base = 'Win32GUI'

# Saída de arquivos
configuracao = Executable(
    script='app.py',
    icon='exe.ico',
    base=base
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