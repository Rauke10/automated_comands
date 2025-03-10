#!/usr/bin/python3
import requests
import urllib3
import subprocess
import os
import signal
import sys
from dotenv import load_dotenv, dotenv_values

load_dotenv()

def objetivo():
	domain = input("Introduzca el objetivo: ")
	return domain

def whatweb(domain: str):
	try:	
		print(subprocess.run(["whatweb","-v", domain]))
	except KeyboardInterrupt:
		print("ffuf detenido por el usuario. Continuando con el programa")

def nmap (domain: str):
	
	try:	
		print(subprocess.run(["nmap","-sSV" ,"-vvv", "-Pn", "-n","-O","-A", domain]))
	except KeyboardInterrupt:
		print("ffuf detenido por el usuario. Continuando con el programa")

def subfinder(domain: str):
	try:	
		print(subprocess.run(["subfinder", "-d", domain]))
	except KeyboardInterrupt:
		print("ffuf detenido por el usuario. Continuando con el programa")
	

def amass(domain: str):
	try:	
		print(subprocess.run(["amass", "enum", "-passive", "-d", domain]))
	except KeyboardInterrupt:
		print("ffuf detenido por el usuario. Continuando con el programa")


def check_connection(domain: str):
	try:
		response = requests.get(domain, timeout=3, allow_redirects=True)
		return response.status_code
	except requests.exceptions.RequestException as e:
		print(f"Error al conectar a {domain}: {e}")
		return None
		


def ffuf(domain: str):
	directorio = os.environ.get('RUTA_DIRECTORIO')
	print(f"{domain}")
	url_https = f"https://{domain}"
	url_http = f"http://{domain}"
	https_status = check_connection(url_https)
	http_status = check_connection(url_http)
	if https_status == 200:
		print(f"Conectado a: {url_https} (Código de estado: 200)")
		domain = url_https
	elif http_status == 200:
		print(f"Conectado a: {url_http} (Código de estado: 200)")
		domain = url_http
	else:
		print("No se pudo conectar ni a HTTP ni a HTTPS")
		
	try:	
		print(subprocess.run(["ffuf","-u", f"{domain}/FUZZ", "-w", f"{directorio}", "-mc", "200", "-recursion", "-recursion-depth", "3" ]))
	except KeyboardInterrupt:
		print("ffuf detenido por el usuario. Continuando con el programa")


def main(domain: str):
	#whatweb(domain)
	#subfinder(domain)
	#ffuf(domain)
	nmap(domain)
	amass(domain)
	print(subprocess.run(["ping","-c1",domain]))




if __name__ == "__main__":
	domain = objetivo()
	main(domain)
