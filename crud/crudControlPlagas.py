from model import controlPlagas
from crud.crudProductosControl import create_producto, update_producto, delete_producto

lista_control_plagas = []
	
def create_control_plagas(ica, nombre, frecuencia_aplicacion, valor, periodo_carencia):
	try:
		producto_base = create_producto(ica, nombre, frecuencia_aplicacion, valor)
		nuevo_control_plagas = controlPlagas.ControlPlagas(
			producto_base.ica, 
			producto_base.nombre, 
			producto_base.frecuencia_aplicacion, 
			producto_base.valor,
			periodo_carencia)
		lista_control_plagas.append(nuevo_control_plagas)
		return nuevo_control_plagas
	except Exception as e:
		raise e
	
def read_control_plagas(ica):
	for control_plagas in lista_control_plagas:
		if control_plagas.ica == ica:
			return control_plagas
	raise Exception("No existe un control de plagas con el nombre indicado.")

def update_control_plagas(ica, nombre, frecuencia_aplicacion, valor, periodo_carencia):
	try:
		control_plagas = read_control_plagas(ica)
		control_plagas.nombre = nombre
		control_plagas.frecuencia_aplicacion = frecuencia_aplicacion
		control_plagas.valor = valor
		control_plagas.periodo_carencia = periodo_carencia
		update_producto(ica, nombre, frecuencia_aplicacion, valor)
		return control_plagas
	except Exception as e:
		raise e
	
def delete_control_plagas(ica):
	try:
		control_plagas = read_control_plagas(ica)
		lista_control_plagas.remove(control_plagas)
		delete_producto(ica)
	except Exception as e:
		raise e
	
