#!/usr/bin/python3
from auto_tools import Auto_Tools

if __name__ == "__main__":
	domain = input("Introduzca el objetivo: ")
	auto_tools = Auto_Tools(domain)
	auto_tools.run_tools()
