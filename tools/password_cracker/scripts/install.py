import os
from pathlib import Path
import subprocess

print("---------------------------CD START---------------------------")
print(__file__)
os.chdir(Path(__file__).parent)
print(os.getcwd())  # Affiche le répertoire courant
dir_path = os.path.dirname(os.path.realpath(__file__))
print("check dir_path "+dir_path)
os.chdir(Path(dir_path).parent)
print(os.getcwd())  # Affiche le répertoire courant
print("---------------------------CD END---------------------------")

print("---------------------------VENV START---------------------------")
subprocess.call(["python ","-m", "venv", ".venv"])
print("---------------------------VENV END---------------------------")

print("---------------------------PIP INSTALL -E .---------------------------")
pip = str(Path(__file__).parent.parent)+"\.venv\Scripts\pip.exe"
subprocess.call([pip, "install", "-e", "."])
print("---------------------------PIP INSTALL -E .---------------------------")
