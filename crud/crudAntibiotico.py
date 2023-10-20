# import sys
# import os
# myDir = os.getcwd()
# sys.path.append(myDir)

from model.antibiotico import Antibiotico

lista_antibioticos = []

def verifica_antibiotico(nombre):
	for antibiotico in lista_antibioticos:
		if antibiotico.nombre == nombre:
			raise Exception("Ya existe un antibiotico con el nombre indicado.")


def create_antibiotico(nombre, dosis, tipo_animal, valor):
	try:
		if (nombre == ""):
			raise ValueError("El nombre no puede ser vacío.")
		verifica_antibiotico(nombre)
		nuevo_antibiotico = Antibiotico(nombre, dosis, tipo_animal, valor)
		lista_antibioticos.append(nuevo_antibiotico)
		return nuevo_antibiotico
	except Exception as e:
		raise e

def read_antibiotico(nombre):
	for antibiotico in lista_antibioticos:
		if antibiotico.nombre == nombre:
			return antibiotico
	raise Exception("No existe un antibiotico con el nombre indicado.")

def update_antibiotico(nombre, dosis, tipo_animal, valor):
	try:	
		antibiotico = read_antibiotico(nombre)
		antibiotico.dosis = dosis
		antibiotico.tipo_animal = tipo_animal
		antibiotico.valor = valor
		return antibiotico
	except Exception as e:
		raise e

def delete_antibiotico(nombre):
	try:	
		antibiotico = read_antibiotico(nombre)
		lista_antibioticos.remove(antibiotico)
		return antibiotico
	except Exception as e:
		raise e
