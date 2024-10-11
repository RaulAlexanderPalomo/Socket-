import socket

class Servidor:
    def __init__(self, host='localhost', port=8000):
        self.host = host
        self.port = port
        self.servidor_socket = socket.socket()
        self.conexion = None

    def iniciar(self):
        self.servidor_socket.bind((self.host, self.port))
        self.servidor_socket.listen(1)
        print(f"Servidor iniciado en {self.host}:{self.port}, esperando conexiones...")
        self.conexion, direccion = self.servidor_socket.accept()
        print(f"Conectado con: {direccion}")

    def recibir_mensaje(self):
        mensaje = self.conexion.recv(1024).decode('utf-8')
        print(f"Mensaje recibido: {mensaje}")
        return mensaje

    def enviar_respuesta(self, mensaje):
        self.conexion.send(mensaje.encode('utf-8'))

    def cerrar(self):
        self.conexion.close()
        print("Conexión cerrada.")


if __name__ == "__main__":
    servidor = Servidor()
    servidor.iniciar()
    servidor.recibir_mensaje()
    servidor.enviar_respuesta("Hola desde el servidor")
    servidor.cerrar()
