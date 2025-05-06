import subprocess
import os

print(os.path.realpath(os.path.dirname(__file__)))

path = os.path.realpath(os.path.dirname(__file__))

subprocess.call(['cd..'], stdout = subprocess.PIPE)

# subprocess.call(["type log.txt"], stdout = subprocess.PIPE)

# subprocess.call(['d:'], stdout=subprocess.PIPE)
# subprocess.call([f'cd {path}'], stdout=subprocess.PIPE)
# subprocess.call(['python aux_script.py'], stdout=subprocess.PIPE)