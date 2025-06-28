from app.usuario import Usuario
# tests/test_usuario.py

def test_get_nombre():
    usuario = Usuario("Carlos", 70.0)
    assert usuario.get_nombre() == "Carlos"

def test_get_peso():
    usuario = Usuario("Carlos", 70.0)
    assert usuario.get_peso() == 70.0

def test_actualizar_peso():
    usuario = Usuario("Carlos", 70.0)
    usuario.actualizar_peso(68.5)
    assert usuario.get_peso() == 68.5

def mostrar_informacion(self):
    return f"Usuario: {self.nombre}, Peso Actual: {self.peso} kg"




