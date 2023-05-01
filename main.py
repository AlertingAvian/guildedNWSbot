import subprocess

subprocess.run("pip3 install -U --prefix .local -r requirements.txt", shell=True)

subprocess.run("python3 /home/container/bot.py")
