
class Producto:
    def __init__(self, id, nombre, descripcion, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

class Inventario:
    def __init__(self):
        self.productos = {}

    def crear_producto(self, id, nombre, descripcion, precio, cantidad):
        if id in self.productos:
            raise ValueError("Producto ya existe")
        self.productos[id] = Producto(id, nombre, descripcion, precio, cantidad)

    def leer_producto(self, id):
        return self.productos.get(id)

    def actualizar_producto(self, id, nombre=None, descripcion=None, precio=None, cantidad=None):
        producto = self.productos.get(id)
        if not producto:
            raise ValueError("Producto no existe")
        if nombre: producto.nombre = nombre
        if descripcion: producto.descripcion = descripcion
        if precio: producto.precio = precio
        if cantidad: producto.cantidad = cantidad

    def eliminar_producto(self, id):
        if id not in self.productos:
            raise ValueError("Producto no existe")
        del self.productos[id]
