# app/usuario.py

class Usuario:
    def __init__(self, nombre: str, peso: float):
        self.nombre = nombre
        self.peso = peso

    def get_nombre(self) -> str:
        return self.nombre

    def get_peso(self) -> float:
        return self.peso

    def actualizar_peso(self, nuevo_peso: float):
       
        self.peso = nuevo_peso

    def mostrar_informacion(self):
        print(f"Usuario: {self.nombre}, Peso Actual: {self.peso} kg")
