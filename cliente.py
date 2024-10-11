import socket

class Cliente:
    def __init__(self, host='localhost', port=8000):
        self.host = host
        self.port = port
        self.cliente_socket = socket.socket()

    def conectar(self):
        self.cliente_socket.connect((self.host, self.port))
        print(f"Conectado al servidor en {self.host}:{self.port}")

    def enviar_mensaje(self, mensaje):
        self.cliente_socket.send(mensaje.encode('utf-8'))

    def recibir_respuesta(self):
        respuesta = self.cliente_socket.recv(1024).decode('utf-8')
        print(f"Respuesta del servidor: {respuesta}")
        return respuesta

    def cerrar(self):
        self.cliente_socket.close()
        print("Conexión cerrada.")


if __name__ == "__main__":
    cliente = Cliente()
    cliente.conectar()
    cliente.enviar_mensaje("Hola desde el cliente")
    cliente.recibir_respuesta()
    cliente.cerrar()
