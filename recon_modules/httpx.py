import subprocess

def run(target):
    try:
        result = subprocess.check_output(f"echo {target} | httpx -title -tech-detect -status-code", shell=True, text=True)
        return result.strip()
    except Exception as e:
        return f"Erro na execução do httpx: {e}"
