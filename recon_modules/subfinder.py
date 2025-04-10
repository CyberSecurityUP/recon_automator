import subprocess

def run(target):
    try:
        result = subprocess.check_output(f"subfinder -d {target} -silent", shell=True, text=True)
        return result.strip()
    except Exception as e:
        return f"Erro na execução do subfinder: {e}"
