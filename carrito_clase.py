from funciones_utiles import crear_id
class Carrito(dict):
    contador_de_carrito = 0
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.identificador = crear_id()
        self.lista_articulos = []
        self.incrementar_carrito()


    @classmethod
    def incrementar_carrito(cls):
        cls.contador_de_carrito += 1

    def pagar(self):
        print('pagando')

    def agregar_item(self, item):
        self.lista_articulos.append(item)