import json

# para utilizar la clase Cliente
# para crear el inventario de clientes
from cliente_clase import Cliente

def obtener_inventario_clientes():

    with open('inventario_clientes.json', mode='r') as f:
        datos_crudos_clientes = json.load(f)

    inventario_cliente = {}
    for mi_cliente in datos_crudos_clientes:
        # agregar un cliente al inventario de clientes usando la cedula como llave
        llave = mi_cliente.get('cedula')
        inventario_cliente.update(
            {llave: Cliente(**mi_cliente)}
        )

    return inventario_cliente