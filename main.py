import os
from modules import run_all_tools
from report import generate_html_report

def main():
    mode = input("Modo [1] Massivo / [2] Single: ")

    if mode == '1':
        target_file = input("Caminho do arquivo com subdomínios: ")
        with open(target_file, 'r') as f:
            targets = f.read().splitlines()
    else:
        single_target = input("Digite o alvo único (ex: site.com): ")
        targets = [single_target]

    all_results = {}
    for target in targets:
        print(f"🔍 Executando recon em {target}")
        results = run_all_tools(target)
        all_results[target] = results

    print("🧾 Gerando relatório HTML...")
    generate_html_report(all_results)
    print("✅ Relatório salvo em: output/target_report.html")

if __name__ == "__main__":
    main()
