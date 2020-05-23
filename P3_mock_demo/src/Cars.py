import requests

class Cars:

    def __init__(self, codigo, marca, sitio_recogida, dias, precio):
        self.Codigo_coche = codigo
        self.Direccion=sitio_recogida
        self.Marca=marca
        self.Dias=dias
        self.Precio=precio

    def informacionCoche(self):
        print(self.Codigo_coche)
        print(self.marca)
        print(self.sitio_recogida)
        print(self.dias)

    @staticmethod

    def download_seat_leon_specifications():
        r = requests.get('http://localhost/dummy_url')
        if r.status_code == 200:
            return r.json()
        return None