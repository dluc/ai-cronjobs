import subprocess

bash_script = "macos/notify.sh"


def notify(parameter):
    try:
        subprocess.run([bash_script, parameter], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running script: {e}")
        return False
    return True
