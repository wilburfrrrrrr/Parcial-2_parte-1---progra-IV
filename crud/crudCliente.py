from model.cliente import Cliente

lista_clientes = []

def verifica_cliente(cedula):
	for cliente in lista_clientes:
		if cliente.cedula == cedula:
			raise Exception("Ya existe un cliente con la cedula indicada.")
		
def create_cliente(nombre, cedula):
	try:
		nuevo_cliente = Cliente(nombre, cedula)
		lista_clientes.append(nuevo_cliente)
		return nuevo_cliente
	except Exception as e:
		raise e

def read_cliente(cedula):
	for cliente in lista_clientes:
		if cliente.cedula == cedula:
			return cliente
	raise Exception("No existe un cliente con la cédula indicada.")

def update_cliente(nombre, cedula):
	try:
		cliente = read_cliente(cedula)
		cliente.nombre = nombre
		return cliente
	except Exception as e:
		raise e

def delete_cliente(cedula):
	try:
		cliente = read_cliente(cedula)
		lista_clientes.remove(cliente)
		return cliente
	except Exception as e:
		raise e

def read_pedidos_cliente(cliente, fecha):
	for pedido in cliente.pedidos:
		if pedido.fecha == fecha:
			return pedido
	raise Exception("No existe un pedido con la fecha indicada.")


def update_pedido_cliente(cliente, fecha, productos):
	try:
		pedido = read_pedidos_cliente(cliente, fecha)
		pedido.productos = productos
		return pedido
	except Exception as e:
		raise e

def delete_pedido_cliente(cliente, fecha):
	try:
		pedido = read_pedidos_cliente(cliente, fecha)
		cliente.pedidos.remove(pedido)
		return pedido	
	except Exception as e:
		raise e	
	
def read_historial(cedula):
	cliente = read_cliente(cedula)	
	cliente.historial_compras()
