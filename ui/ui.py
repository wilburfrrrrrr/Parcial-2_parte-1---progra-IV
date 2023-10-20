from tabulate import tabulate


def menu():
	print("\nBienvenido al sistema de gestión de productos agropecuarios\n Seleccione una opción:")
	print("1. Registrar un nuevo usuario")
	print("2. Iniciar sesión")
	print("3. Editar Productos")
	print("4. Salir\n")


def menu_editar():
	print("\nSeleccione una opción de manejo de productos:")
	print("\n1. Agregar producto")
	print("2. Editar producto")
	print("3. Eliminar producto")

def menu_pedidos():
	print("\nQue producto desea agregar?")
	print("\n1. Agregar Producto")
	print("2. Terminar Pedidos\n")
	

def opciones_producto():
	print("\nEl producto creado será ...:")
	print("\n1. Antibioticos")
	print("2. Productos de Control de Fertilizantes")
	print("3. Productos de Control de Plagas\n")



def opciones_cliente():
	print("\nBienvenido al sistema de gestión de clientes\n Seleccione una opción:")
	print("\n1. Agregar cliente")
	print("2. Editar cliente")
	print("3. Eliminar cliente")
	print("4. Salir\n")

def opciones_pedidos():
	print("\nBienvenido al sistema de gestión de pedidos\n Seleccione una opción:")
	print("\n1. Agregar pedido")
	print("2. Editar pedido")
	print("3. Eliminar pedido")
	print("4. Salir\n")

def opciones_sesion():
	print("\nBienvenido al sistema de gestión de pedidos\n Seleccione una opción:")
	print("\n1. Modificar datos de cliente")
	print("2. Nuevo pedido")
	print("3. Mirar historial de pedidos")

def obtener_nombre():
	nombre = input("Ingrese el nombre del usuario: ")
	return nombre

def obtener_cedula():
	cedula = input("Ingrese la cédula del usuario: ")
	return cedula

def obtener_dosis():
	dosis = input("Ingrese la dosis del antibiótico: ")
	return dosis

def obtener_tipo_animal():
	tipo_animal = input("Ingrese el tipo de animal (Bovino, Caprino o Porcino): ")
	return tipo_animal

def obtener_valor():
	valor = input("Ingrese el valor del antibiótico: ")
	return valor

def obtener_ica():
	ica = input("Ingrese el ICA del producto: ")
	return ica

def obtener_frecuencia():
	frecuencia = input("Ingrese la frecuencia de aplicación del producto: ")
	return frecuencia

def obtener_periodo_carencia():
	periodo_carencia = input("Ingrese el periodo de carencia del producto: ")
	return periodo_carencia

def obtener_fecha_ultima_aplicacion():
	fecha_ultima_aplicacion = input("Ingrese la fecha de la última aplicación del producto: ")
	return fecha_ultima_aplicacion

def imprimir_tabla_productos(productos):
	print(tabulate(productos, headers=["Nombre", "ICA", "Frecuencia de aplicación", "Valor"]))

def imprimir_tabla_clientes(clientes):
	print(tabulate(clientes, headers=["Nombre", "Cédula"]))

def imprimir_tabla_pedidos(pedidos):
	print(tabulate(pedidos, headers=["Fecha", "Productos"]))

def imprimir_tabla_antibioticos(antibioticos):
	print(tabulate(antibioticos, headers=["Nombre", "Dosis", "Tipo de animal", "Valor"]))

def imprimir_tabla_productos_control(productos_control):
	print(tabulate(productos_control, headers=["Nombre", "ICA", "Frecuencia de aplicación", "Valor"]))

def imprimir_factura(nombre_cliente, lista_productos):
	print("Factura de compra")
	print("Cliente: ", nombre_cliente)
	print("Productos: ")
	for producto in lista_productos:
		print(producto.nombre, producto.valor)