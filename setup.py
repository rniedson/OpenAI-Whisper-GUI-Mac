import os
import subprocess
import sys
import time
from importlib.metadata import distributions

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

# Verificando a existência das pastas necessárias
folders = ["assets"]
missing_folder = [folder for folder in folders if not os.path.exists(folder)]
if missing_folder:
    print("These folder(s) are missing: " + str(missing_folder))
    print("Download them from the repository properly")
    sys.exit()
else:
    print("All folders available!")

# Verificando os módulos necessários
required = {"Pillow==10.1.0", "customtkinter==5.2.1", "packaging==23.2", "openai-whisper==20231117", "pynvml==11.5.0"}
installed = {pkg.metadata['Name'].lower() for pkg in distributions()}
missing = required - installed

# Download dos módulos, se necessário
if missing:
    print("Installing missing modules...")
    for package in missing:
        subprocess.run([sys.executable, '-m', 'pip', 'install', package], check=True)

# Instalação específica do PyTorch de acordo com o sistema operacional
if sys.platform.startswith("darwin"):  # específico para macOS
    print("Installing PyTorch for macOS...")
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'torch', 'torchvision', 'torchaudio'], check=True)

print("Setup Complete!")
time.sleep(5)
sys.exit()
