base_de_datos = [
    {"nombre": "Juan", "id": 1, "edad": 20},
    {"nombre": "María", "id": 2, "edad": 22},
    {"nombre": "Carlos", "id": 3, "edad": 21}
]


def buscar_estudiante_id(base_de_datos,id):
    #un for para buscar en cada elemento de la base de datos y el if para comprar el id
    for estudiante in base_de_datos:
        if estudiante['id'] == id:
            return estudiante
        else:
            return None

        
type(buscar_estudiante_id(base_de_datos,id=4))

suma = 1+1
perra = 'a'

suma, perra