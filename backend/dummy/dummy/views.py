""" Cornice services."""
from cornice import Service


my_service = Service(name='example', path='/example')

dummy_data = {
    "id": 1,
    "name": "Yorch",
    "bee": "Colletidae"
}

DATA = [dummy_data]

@my_service.get(operation_id='getExample')
def get_example(request):
    """Obtiene un ejemplo."""
    return {"msg": "ok", "data": DATA}

@my_service.post(operation_id='createExample')
def create_example(request):
    """Crea un ejemplo."""
    new_data = {
        "id": request.json_body.get("id"),
        "name": request.json_body.get("name"),
        "bee": request.json_body.get("bee"),
        "color": request.json_body.get("color")
    }
    DATA.append(new_data)
    return {"msg": "created", "data": new_data}
