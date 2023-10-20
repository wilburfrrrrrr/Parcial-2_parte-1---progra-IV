from model import productoControl

lista_productos = []

def verifica_producto(ica):
	for producto in productoControl.lista_productos:
		if producto.ica == ica:
			raise Exception("Ya existe un producto con el nombre indicado.")
		
def create_producto(ica, nombre, frecuencia_aplicacion, valor):
	try:
		if (nombre == ""):
			raise ValueError("El nombre no puede ser vacío.")
		verifica_producto(ica)
		nuevo_producto = productoControl.ProductoControl(ica, nombre, frecuencia_aplicacion, valor)
		productoControl.lista_productos.append(nuevo_producto)
		return nuevo_producto
	except Exception as e:
		raise e
	
def read_producto(ica):
	for producto in productoControl.lista_productos:
		if producto.ica == ica:
			return producto
	raise Exception("No existe un producto con el nombre indicado.")

def update_producto(ica, nombre, frecuencia_aplicacion, valor):
	try:
		producto = read_producto(ica)
		producto.nombre = nombre
		producto.frecuencia_aplicacion = frecuencia_aplicacion
		producto.valor = valor
		return producto
	except Exception as e:
		raise e
	
def delete_producto(ica):
	try:
		producto = read_producto(ica)
		productoControl.lista_productos.remove(producto)
	except Exception as e:
		raise e

