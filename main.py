import crud
import ui


def crear_cliente():
	nombre = ui.obtener_nombre()
	cedula = ui.obtener_cedula()
	cliente = crud.crear_cliente(nombre, cedula)
	return cliente

def crear_antibiotico():
	nombre = ui.obtener_nombre()
	dosis = ui.obtener_dosis()
	tipo_animal = ui.obtener_tipo_animal()
	valor = ui.obtener_valor()
	antibiotico = crud.crear_antibiotico(nombre, dosis, tipo_animal, valor)
	return antibiotico

def crear_fertilizante():
	nombre = ui.obtener_nombre()
	ica = ui.obtnener_ica()
	frecuencia = ui.obtener_frecuencia()
	valor = ui.obtener_valor()
	fecha = ui.obtener_fecha_ultima_aplicacion()
	fertilizante = crud.crear_fertilizante(nombre, ica, frecuencia, valor, fecha)
	return fertilizante

def crear_control_plagas():
	nombre = ui.obtener_nombre()
	ica = ui.obtnener_ica()
	frecuencia = ui.obtener_frecuencia()
	valor = ui.obtener_valor()
	periodo = ui.obtener_periodo_carencia()
	control_plagas = crud.crear_control_plagas(nombre, ica, frecuencia, valor, periodo)
	return control_plagas

def crear_productos():
	opcion = int(input("Ingrese una opción: "))
	if (opcion == 1):
		antibiotico = crear_antibiotico()
		crud.agregar_productos(antibiotico)
	elif (opcion == 2):
		fertilizante = crear_fertilizante()
		crud.agregar_productos(fertilizante)
	elif (opcion == 3):
		control_plagas = crear_control_plagas()
		crud.agregar_productos(control_plagas)
	else:
		raise ValueError("Opción inválida.")
	
def buscar_productos(ica):
	ica = ui.obtener_ica()
	producto = crud.crudProductosControl.read_productos(ica)
	return producto

def buscar_cliente(cedula):
	cedula = ui.obtener_cedula()
	cliente = crud.crudClientes.read_cliente(cedula)
	return cliente

def agrega_producto_carro():
	ica = ui.obtener_ica()
	producto = buscar_productos(ica)
	crud.crudPedidos.agregar_productos(producto)

def agregar_productos():
	opcion = int(input("Ingrese una opción: "))
	if (opcion == 1):
		antibiotico = crear_antibiotico()
		crud.agregar_productos(antibiotico)
	elif (opcion == 2):
		fertilizante = crear_fertilizante()
		crud.agregar_productos(fertilizante)
	elif (opcion == 3):
		control_plagas = crear_control_plagas()
		crud.agregar_productos(control_plagas)
	else:
		raise ValueError("Opción inválida.")


def menu_pedidos(cliente):
	opcion = 0
	productos = crud.crudPedidos
	while(opcion != 2):
		ui.opciones_pedidos()
		opcion = int(input("Ingrese una opción: "))
		if (opcion == 1):
			agrega_producto_carro()
		elif (opcion == 2):
			producto_agregado = productos.create_pedido(productos.carro_productos)
			crud.crudPedidos.registro_pedido(cliente, producto_agregado.fecha)
			factura(cliente, producto_agregado.fecha)
		else:
			raise ValueError("Opción inválida.")

def factura(cliente, fecha):
	print("Compra finalizada. La factura es: ")
	pedido = crud.crudPedidos.read_pedido(fecha)
	ui.imprimir_factura(cliente.nombre, pedido)


def main():
	while True:
		ui.menu()
		opcion = int(input("Ingrese una opción: "))
		if (opcion == 1):
			try:
				cliente = crear_cliente()
				crud.crudClientes.agregar_cliente(cliente)
			except:
				raise ValueError("Opción inválida.")
		elif (opcion == 2):
			try:
				cedula = ui.obtener_cedula()
				cliente = buscar_cliente(cedula)
				menu_pedidos(cliente)
			except Exception as e:
				raise e
		elif (opcion == 3):
			break
		else:
			raise ValueError("Opción inválida.")
	
