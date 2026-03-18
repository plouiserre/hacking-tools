import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.requests import Requests


# req = Requests("http://localhost:5074/Identity/Connexion")
# req.post("Admin", "admin")

print("hello world")
print("args "+sys.argv[1])