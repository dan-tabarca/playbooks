import subprocess
import getpass
import os
from glob import glob
from github import Github

# git config credential.helper store
# git config --global credential.helper 'cache --timeout 36000'
# git push https://github.com/dan-tabarca/playbooks.git
# 
# Download all repos
# curl https://api.github.com/users/dan-tabarca/repos?per_page=1000 | grep -o 'git@[^"]*' | xargs -L1 git clone)]

# Get the name of all repos
# curl https://api.github.com/users/dan-tabarca/repos?per_page=1000 |  grep -o 'git@[^\"]*' | cut -d '/' -f 2 | rev | cut -c 5- | rev

def download_repos():
    dirs=[]
    repos=[]
    password = getpass.getpass("Insert your password for your GIT account: ")
    g = Github("dan-tabarca", password) 
    path=(os.getcwd())
    full_path_of_dir=glob(path+"/*/")
    for index in full_path_of_dir: 
        dirs.append(index.split("/")[-2])
    for repo in g.get_user().get_repos():
        repos.append(repo.name)
    if len(dirs)>0:
        for directory in dirs:
           for repo_value in repos:
               if not repo_value in directory: 
#                  print("Directory is:" + directory + "Repo is:" + repo_value)
                   os.system("curl https://api.github.com/users/dan-tabarca/repos?per_page=1000 | grep -o 'git@github.com:dan-tabarca/'" + directory + ".git | xargs -L1 git clone")
    else:
        os.system("curl https://api.github.com/users/dan-tabarca/repos?per_page=1000 | grep -o 'git@[^\"]*' | xargs -L1 git clone")

def prereq():
    req = subprocess.Popen(["git", "config", "--global", "credential.helper"], stdout=subprocess.PIPE)
    if not 'cache --timeout' in req.communicate()[0]:
        pwd = subprocess.Popen(["pwd"], stdout=subprocess.PIPE)
        full_path = pwd.communicate()[0].split("/")
        repository = full_path[len(full_path)-1]
        subprocess.call(["git", "config", "--global", "credential.helper", "cache"])
        subprocess.call(["git", "config", "--global", "credential.helper", "cache --timeout 36000"])
        subprocess.call(["git", "push", "https://github.com/dan-tabarca/" + repository + ".git"])

def git():
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "reset", "git.py"])
    message = raw_input("Commit your message: ")
    subprocess.call(["git", "commit", "-m", message])
    subprocess.call(["git", "push"])

#download_repos()
prereq()
git()

