
from generador_inventario_clientes import obtener_inventario_clientes
from carrito_clase import Carrito
from funciones_utiles import crear_id

# inventario de carritos
inventario_de_carritos = {}

def obtener_carritos(cedula_cliente):
    lista_carritos = []
    for carrito in inventario_de_carritos.values():
        cedula = carrito.get('cliente').get('cedula')
        if cedula_cliente == cedula:
            lista_carritos.append(carrito)
    return lista_carritos

def agregar_carrito_al_inventario(cedula_cliente):
    id_nuevo_carrito = crear_id()
    # quien es el cliente?
    # buscar el cliente -> en el inventario de clientes
    inventario_clientes = obtener_inventario_clientes()
    el_cliente = inventario_clientes.get(cedula_cliente)
    inventario_de_carritos.update(
        {
            id_nuevo_carrito: Carrito(cliente=el_cliente) # aqui va los parametros de la calse carrito
        }
    )

def obtener_id_productos_carritos(lista_carritos):
    lista_ids_productos = []
    for carrito in lista_carritos:
        # falta agregar los nombres de los productos
        lista_ids_productos.append(carrito.identificador)
    return lista_ids_productos

def obtener_carrito__por_id(id):
    mi_carrito = None
    for carrito in inventario_de_carritos.values():
        if id == carrito.identificador:
            mi_carrito = carrito
    return mi_carrito


def control_flujo():
    # coloque aqui la logica
    # por ejemplo el control de flujo

    # tengo el inventario de clientes
    inventario_clientes = obtener_inventario_clientes()

    # necesito el inventario de productos...