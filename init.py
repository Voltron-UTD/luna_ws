import os;
from os import path
import shutil;
import json;

reply = str(input("[init.py] This will clear existing files from the directory. Continue [y/N]? ")).lower().strip()

if reply[0] != 'y':
    print("Aborted.")
    exit -1;

# Delete ./src recursively if it exists
if path.exists("./src"):
    shutil.rmtree("./src")
os.mkdir("./src")
os.mkdir("./src/external")

# Load JSON data from file
with open('luna_repos.json') as json_file:
    json_data = json.load(json_file)
    os.chdir("./src")
    print("[init.py] Cloning git repos...")
    for repo in json_data['repos']:
        # Get repo name from URL
        name = repo['url'].split('/')[-1][:-4]

        # If repo is marked external, send to /src/external
        if repo['type'] == 'external':
            os.chdir('./external')
            os.system("git clone {}".format(repo['url']))
            os.chdir('..')
        # Else put directly in /src
        else:
            os.system("git clone {}".format(repo['url']))

print("[init.py] Done! Luna WS is ready to be built and sourced. 🎉")