import subprocess

# If the cache is gone, type manually: 
# git config credential.helper store
# git config --global credential.helper 'cache --timeout 36000'
# git push https://github.com/dan-tabarca/playbooks.git

#subprocess.call(["git", "config", "credential.helper", "store"])
#subprocess.call(["git", "config", "--global", "credential.helper 'cache --timeout 36000'"])
def git():
    subprocess.call(["git", "add", "."])
    message = raw_input("Commit your message: ")
    subprocess.call(["git", "commit", "-m", message])
    subprocess.Popen(["git", "push"])
    print("\n")

git()
