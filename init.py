import os;
from os import path
import shutil;
import json;

reply = str(input("[init.py] This will clear existing files from the directory. Continue [y/N]? ")).lower().strip()

if reply[0] != 'y':
    print("Aborted.")
    exit -1;

# Remove existing directories
dirs_to_clear = ["./src","./install","./build","./log"]
for dir in dirs_to_clear:
    if path.exists(dir):
        shutil.rmtree(dir)

os.mkdir("./src")
os.mkdir("./src/external")

def clone(url, branch):
    os.system("git clone {}".format(url))
    os.chdir(url.split('/')[-1])
    os.system("git checkout {}".format(branch))
    os.chdir("..")

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
            clone(repo.get('url'),repo.get('branch'))
            os.chdir('..')
        # Else put directly in /src
        else:
            clone(repo['url'],repo['branch'])



print("[init.py] Done! Luna WS is ready to be built and sourced. 🎉")
print("[init.py] Try running 'colcon build'")
