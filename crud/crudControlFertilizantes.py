from model import controlFertilizantes
from crud.crudProductosControl import create_producto, update_producto, delete_producto

lista_fertilizantes = []

	
def create_fertilizante(ica, nombre, frecuencia_aplicacion, valor, fecha_ultima_aplicacion):
	try:
		producto_base = create_producto(ica, nombre, frecuencia_aplicacion, valor)
		nuevo_fertilizante = controlFertilizantes.ControlFertilizantes(
			producto_base.ica, 
			producto_base.nombre, 
			producto_base.frecuencia_aplicacion, 
			producto_base.valor,
			fecha_ultima_aplicacion)
		lista_fertilizantes.append(nuevo_fertilizante)
		return nuevo_fertilizante
	except Exception as e:
		raise e
	
def read_fertilizante(ica):
	for fertilizante in lista_fertilizantes:
		if fertilizante.ica == ica:
			return fertilizante
	raise Exception("No existe un fertilizante con el nombre indicado.")

def update_fertilizante(ica, nombre, frecuencia_aplicacion, valor, fecha_ultima_aplicacion):
	try:
		fertilizante = read_fertilizante(ica)
		fertilizante.nombre = nombre
		fertilizante.frecuencia_aplicacion = frecuencia_aplicacion
		fertilizante.valor = valor
		fertilizante.fecha_ultima_aplicacion = fecha_ultima_aplicacion
		update_producto(ica, nombre, frecuencia_aplicacion, valor)
		return fertilizante
	except Exception as e:
		raise e
	
def delete_fertilizante(ica):
	try:
		fertilizante = read_fertilizante(ica)
		lista_fertilizantes.remove(fertilizante)
		delete_producto(ica)
	except Exception as e:
		raise e

