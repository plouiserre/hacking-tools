import os 
import sys 
import subprocess
from pathlib import Path

#Chemin vers le bon activate selon l'OS
grand_parent_path = Path(__file__).parent.parent
print(grand_parent_path)
if os.name == "nt" : # Windows
    python = grand_parent_path/".venv"/"Scripts"/"python.exe"
else :
    python = grand_parent_path/".venv"/"bin"/"python"

print(str(python))

# Lance la commande de ton outil via le python du .venv
main_file = grand_parent_path/"src"/"cli"/"main.py"
print(main_file)

subprocess.run([str(python), str(main_file)] )