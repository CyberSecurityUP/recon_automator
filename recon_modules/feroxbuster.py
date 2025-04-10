import subprocess

def run(target):
    try:
        result = subprocess.check_output(f"feroxbuster -u https://{target} -w /usr/share/wordlists/dirb/common.txt -q", shell=True, text=True)
        return result.strip()
    except Exception as e:
        return f"Erro na execução do feroxbuster: {e}"
