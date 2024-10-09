import os
import subprocess

bash_script = "notify.sh"
bash_script = os.path.join(os.path.dirname(os.path.realpath(__file__)), "notify.sh")


def notify(parameter):
    try:
        subprocess.run([bash_script, parameter], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running script: {e}")
        return False
    return True
