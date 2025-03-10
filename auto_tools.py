import requests
import urllib3
import subprocess
import os
import signal
import sys
import asyncio
from dotenv import load_dotenv, dotenv_values

load_dotenv()

class Auto_Tools():
	
	def __init__(self, domain: str):
		self.domain = domain
		
		self.directorio_dns = os.environ.get('RUTA_DNS')
		self.directorio = os.environ.get('RUTA_DIRECTORIO')
		
		self.url_https = f"https://{self.domain}"
		self.url_http = f"http://{self.domain}"
		
		self.https_status = self.__check_connection(self.url_https)
		self.http_status = self.__check_connection(self.url_http)
		
		
	@staticmethod
	def __check_connection(url):
		try:
			response = requests.get(url, timeout=3, allow_redirects=True)
			return response.status_code
		except requests.exceptions.RequestException as e:
			print(f"Error al conectar a {url}: {e}")
			return None

	def __whatweb(self):
		try:	
			print(subprocess.run(["whatweb","-v", self.domain]))
		except KeyboardInterrupt:
			print("whatweb detenido por el usuario. Continuando con el programa")

	def __nmap (self):
		
		try:	
			print(subprocess.run(["nmap","-sSV" ,"-vvv", "-Pn", "-n","-O","-A", self.domain]))
		except KeyboardInterrupt:
			print("nmap detenido por el usuario. Continuando con el programa")

	def __wafw00f(self):
	
		if self.https_status == 200:
			print(f"Conectado a: {self.url_https} (Código de estado: 200)")
			domain = self.url_https
		elif self.http_status == 200:
			print(f"Conectado a: {self.url_http} (Código de estado: 200)")
			domain = self.url_http
		else:
			print("No se pudo conectar ni a HTTP ni a HTTPS")
			
		try:	
			print(subprocess.run(["wafw00f", domain]))
		except KeyboardInterrupt:
			print("wafw00f detenido por el usuario. Continuando con el programa")
			
	def __whois (self):
		
		try:	
			ping = subprocess.run(["ping","-c1",self.domain],capture_output=True, text=True)
			for i in ping.stdout.split('\n'):
				if "bytes from" in i:
					ip = i.split()[4].strip(":").strip('()')
			print(subprocess.run(["whois", '-d', ip]))
		except KeyboardInterrupt:
			print("whois detenido por el usuario. Continuando con el programa")

	def __sslscan(self):
		try:	
			print(subprocess.run(["sslscan", self.domain]))
		except KeyboardInterrupt:
			print("sslscan detenido por el usuario. Continuando con el programa")


	def __subfinder(self):
		try:	
			print(subprocess.run(["subfinder", "-d", self.domain]))
		except KeyboardInterrupt:
			print("subfinder detenido por el usuario. Continuando con el programa")
		

	def __nikto(self):
		try:	
			print(subprocess.run(["nikto", "-h", self.domain]))
		except KeyboardInterrupt:
			print("nikto detenido por el usuario. Continuando con el programa")


	def __gobuster(self):
		
		try:	
			print(subprocess.run(["gobuster","dns","-d", self.domain, "-w", self.directorio_dns]))
		except KeyboardInterrupt:
			print("gobuster detenido por el usuario. Continuando con el programa")


	def __theHarvester(self):
		try:	
			print(subprocess.run(["theHarvester", "-d", self.domain, "-b", "all", "-l", "200"]))
		except KeyboardInterrupt:
			print("theHarvester detenido por el usuario. Continuando con el programa")
		


	def __ffuf(self):
		
		if self.https_status == 200:
			print(f"Conectado a: {self.url_https} (Código de estado: 200)")
			domain = self.url_https
		elif self.http_status == 200:
			print(f"Conectado a: {self.url_http} (Código de estado: 200)")
			domain = self.url_http
		else:
			print("No se pudo conectar ni a HTTP ni a HTTPS")
			
		try:	
			print(subprocess.run(["ffuf","-u", f"{domain}/FUZZ", "-w", f"{self.directorio}", "-mc", "200", "-recursion", "-recursion-depth", "3" ]))
		except KeyboardInterrupt:
			print("ffuf detenido por el usuario. Continuando con el programa")


	def run_tools(self):
		
		self.__whatweb()
		self.__nmap()
		self.__wafw00f()
		self.__subfinder()
		self.__sslscan()
		self.__gobuster()
		self.__whois()
		self.__nikto()
		self.__ffuf()
		self.__theHarvester()
		
		

