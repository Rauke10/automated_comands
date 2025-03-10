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
	

def check_connection(domain: str):
	try:
		response = requests.get(domain, timeout=3, allow_redirects=True)
		return response.status_code
	except requests.exceptions.RequestException as e:
		print(f"Error al conectar a {domain}: {e}")
		return None



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

def wafw00f(domain: str):
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
		print(subprocess.run(["wafw00f", domain]))
	except KeyboardInterrupt:
		print("wafw00f detenido por el usuario. Continuando con el programa")
		
def whois (domain: str):
	
	try:	
		prueba = subprocess.run(["ping","-c1",domain],capture_output=True, text=True)
		for i in prueba.stdout.split('\n'):
			if "bytes from" in i:
			        ip = i.split()[4].strip(":").strip('()')
		print(subprocess.run(["whois", '-d', ip]))
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
	#nmap(domain)
	#whois(domain)
	wafw00f(domain)




if __name__ == "__main__":
	domain = objetivo()
	main(domain)
