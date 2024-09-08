import subprocess


def ping_ip(ip):
    try:
        # subprocess.run(["ping", "-c", "1", ip] for linux
        output = subprocess.run(["ping", "-n", "1", ip], capture_output=True)
        return output.returncode == 0
    except Exception as e:
        return False