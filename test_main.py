import unittest
from main import Inventario

class TestInventario(unittest.TestCase):
    def setUp(self):
        self.inv = Inventario()

    def test_crear_producto(self):
        self.inv.crear_producto('1', 'Mouse', 'Mouse óptico', 40.0, 10)
        self.assertIsNotNone(self.inv.leer_producto('1'))

    def test_actualizar_producto(self):
        self.inv.crear_producto('2', 'Teclado', 'Teclado mecánico', 70.0, 5)
        self.inv.actualizar_producto('2', cantidad=8)
        self.assertEqual(self.inv.leer_producto('2').cantidad, 8)

    def test_eliminar_producto(self):
        self.inv.crear_producto('3', 'Monitor', 'Monitor LED', 400.0, 2)
        self.inv.eliminar_producto('3')
        self.assertIsNone(self.inv.leer_producto('3'))

    def test_error_actualizar(self):
        with self.assertRaises(ValueError):
            self.inv.actualizar_producto('99', nombre='Tablet')

    def test_error_eliminar(self):
        with self.assertRaises(ValueError):
            self.inv.eliminar_producto('99')

if __name__ == '__main__':
    unittest.main()
