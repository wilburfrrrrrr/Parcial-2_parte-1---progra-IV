class Cliente:
    def __init__(self, nombre, cedula):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__pedidos = []

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if not nombre.isalpha():
            raise ValueError("El nombre debe contener solo letras.")
        self.__nombre = nombre
        
    @property
    def cedula(self):
        return self.__cedula
    
    @cedula.setter
    def cedula(self, cedula):
        if not cedula.isdigit():
            raise ValueError("La cédula debe contener solo números.")
        self.__cedula = cedula
        
    @property
    def pedidos(self):
        return self.__pedidos
    
    @pedidos.setter
    def pedidos(self, pedidos):
        self.__pedidos.append(pedidos)
    
    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def historial_compras(self):
        print("\nHistorial de Compras para", self.nombre, " (Cédula:", self.cedula, "):")
        for pedido in self.pedidos:
            print("- Fecha de Compra:", pedido.fecha, "| Total de Compra:", pedido.calcular_total())