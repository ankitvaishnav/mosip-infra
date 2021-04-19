import os

# Maven local repo
from pathlib import Path

home = str(Path.home())

# Env file path
envPath = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), './', '.env')
)

rootPath = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
)

logPath = os.path.abspath(
    os.path.join(rootPath, 'out.log')
)

generatedDataFolderPath = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), './', 'generatedData')
)

# result paths
dmlPath = os.path.join(generatedDataFolderPath, 'dml.csv')