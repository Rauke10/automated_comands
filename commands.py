#!/usr/bin/python3
import requests
import urllib3
print(requests.__file__)
import subprocess
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

def objetivo():
	domain = input("Introduzca el objetivo: ")
	return domain

def whatweb(domain: str):
	print(subprocess.run(["whatweb","-v", domain]))

def nmap (domain: str):
	print(subprocess.run(["nmap", "-vvv", "-sS", "-Pn", "-n", "-p", "--open", domain]))

def subfinder(domain: str):
	print(subprocess.run(["subfinder", "-d", domain]))

def ffuf(domain: str):
	directorio = os.environ.get('RUTA_DIRECTORIO')
	print(f"{domain}")
	url_https = f"https://{domain}"
	url_http = f"http://{domain}"
	response = requests.get(url_http, timeout=5)
	if response.status_code == 200:
		print(f"Conectado a: {url_http}")
		domain = url_http
	else:
		print("Este dominio no contiene http")
	#print(subprocess.run(["ffuf","-u", f"{domain}/FUZZ", "-w", f"{directorio}", "-mc", "200", "-recursion", "-recursion-depth", "3" ]))


def main(domain: str):
	#whatweb(domain)
	#subfinder(domain)
	ffuf(domain)
	print(subprocess.run(["ping","-c1",domain]))









if __name__ == "__main__":
	domain = objetivo()
	main(domain)
