import subprocess
import os
import sys
import platform

def run_command(cmd):
    subprocess.run(cmd, shell=True, check=True)

def main():
    venv_dir = "venv"

    # Crear entorno virtual
    if not os.path.isdir(venv_dir):
        run_command(f"{sys.executable} -m venv {venv_dir}")

    # Activar entorno y instalar dependencias
    if platform.system() == "Windows":
        activate = f"{venv_dir}\\Scripts\\activate.bat &&"
    else:
        activate = f"source {venv_dir}/bin/activate &&"

    pip_install = f"{activate} pip install -r requirements.txt"
    run_command(pip_install)

    # Abrir Jupyter Notebook directamente en el análisis exploratorio
    launch_notebook = f"{activate} jupyter notebook notebooks/exploratory_analysis.ipynb"
    run_command(launch_notebook)

if __name__ == "__main__":
    main()
