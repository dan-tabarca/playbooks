import subprocess

# git config credential.helper store
# git config --global credential.helper 'cache --timeout 36000'
# git push https://github.com/dan-tabarca/playbooks.git
# 
# Download all repos
# curl https://api.github.com/users/dan-tabarca/repos?per_page=1000 | grep -o 'git@[^"]*' | xargs -L1 git clone)]

# Get the name of all repos
# curl https://api.github.com/users/dan-tabarca/repos?per_page=1000 |  grep -o 'git@[^\"]*' | cut -d '/' -f 2 | rev | cut -c 5- | rev

def download_repos():
#     download = os.system("curl https://api.github.com/users/dan-tabarca/repos?per_page=1000 | grep -o 'git@[^\"]*' | xargs -L1 git clone") 
     p1=subprocess.call(["curl", "https://api.github.com/users/dan-tabarca/repos?per_page=1000"], stdout=subprocess.PIPE)
     p2=subprocess.Popen(["grep", "-o 'git@[^\"]*'"], stdin=p1.stdout, shell=True, stdout=subprocess.PIPE)
     p1.stdout.close()
     result = p2.communicate()[0]
     print(result)

def prereq():
    req = subprocess.Popen(["git", "config", "--global", "credential.helper"], stdout=subprocess.PIPE)
    if not 'cache --timeout' in req.communicate()[0]:
        pwd = subprocess.Popen(["pwd"], stdout=subprocess.PIPE)
        full_path = pwd.communicate()[0].split("/")
        repo = full_path[len(full_path)-1]
        subprocess.call(["git", "config", "--global", "credential.helper", "cache"])
        subprocess.call(["git", "config", "--global", "credential.helper", "cache --timeout 36000"])
        subprocess.call(["git", "push", "https://github.com/dan-tabarca/" + repo + ".git"])

def git():
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "reset", "git.py"])
    message = raw_input("Commit your message: ")
    subprocess.call(["git", "commit", "-m", message])
    subprocess.call(["git", "push"])

download_repos()
#prereq()
#git()

