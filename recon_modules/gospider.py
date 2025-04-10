import subprocess

def run(target):
    try:
        result = subprocess.check_output(f"gospider -s https://{target} -t 10 -c 10 --no-redirect -q", shell=True, text=True)
        return result.strip()
    except Exception as e:
        return f"Erro na execução do gospider: {e}"
