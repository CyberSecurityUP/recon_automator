from recon_modules import (
    assetfinder, subfinder, httpx, gospider,
    paramspider, feroxbuster, sslscan, tlsx,
    whatweb, trufflehog
)

def run_all_tools(target):
    return {
        "assetfinder": assetfinder.run(target),
        "subfinder": subfinder.run(target),
        "httpx": httpx.run(target),
        "gospider": gospider.run(target),
        "paramspider": paramspider.run(target),
        "feroxbuster": feroxbuster.run(target),
        "sslscan": sslscan.run(target),
        "tlsx": tlsx.run(target),
        "whatweb": whatweb.run(target),
        "trufflehog": trufflehog.run(target),
    }
