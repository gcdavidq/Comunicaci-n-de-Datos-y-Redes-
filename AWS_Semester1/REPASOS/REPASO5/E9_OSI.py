'''
Ejercicio 9: Implementacion completa del MODELO OSI con simulacion de trafico de red

Crear una simulación detallada del modelo OSI que incluya todas las capas y permita el
seguimiento de un paquete de datos a través de cada capa. 
'''

class OSIModel:
    def __init__(self):
        self.packet_log = []  # Registro del estado del paquete en cada capa

    def capa_aplicacion(self, data):
        """
        Capa de Aplicación: Prepara los datos para su transmisión.
        
        :param data: Datos originales.
        :return: Datos preparados para la capa de presentación.
        """
        self.packet_log.append(f"Capa de Aplicación: {data}")
        print(f"Capa de Aplicación: Preparando datos -> {data}")
        return data

    def capa_presentacion(self, data):
        """
        Capa de Presentación: Realiza la traducción de datos y la encriptación.
        
        :param data: Datos de la capa de aplicación.
        :return: Datos traducidos y encriptados.
        """
        translated_data = data.encode('utf-8')  # Simula la traducción a un formato binario.
        self.packet_log.append(f"Capa de Presentación: {translated_data}")
        print(f"Capa de Presentación: Traduciendo y encriptando -> {translated_data}")
        return translated_data

    def capa_sesion(self, data):
        """
        Capa de Sesión: Establece, gestiona y termina las sesiones entre aplicaciones.
        
        :param data: Datos de la capa de presentación.
        :return: Datos con información de sesión.
        """
        session_data = b'SESSION_START' + data + b'SESSION_END'  # Simula el manejo de sesión.
        self.packet_log.append(f"Capa de Sesión: {session_data}")
        print(f"Capa de Sesión: Manejo de sesión -> {session_data}")
        return session_data

    def capa_transporte(self, data):
        """
        Capa de Transporte: Segmenta y reensambla los datos, maneja el control de flujo y errores.
        
        :param data: Datos de la capa de sesión.
        :return: Segmentos de datos.
        """
        segments = [data[i:i+10] for i in range(0, len(data), 10)]  # Segmentación simulada.
        self.packet_log.append(f"Capa de Transporte: {segments}")
        print(f"Capa de Transporte: Segmentando -> {segments}")
        return segments

    def capa_red(self, segments):
        """
        Capa de Red: Realiza el enrutamiento de los segmentos de datos.
        
        :param segments: Segmentos de datos de la capa de transporte.
        :return: Paquetes con direcciones de red.
        """
        packets = [b'HEADER' + segment + b'FOOTER' for segment in segments]  # Simula la adición de encabezados y pies de página.
        self.packet_log.append(f"Capa de Red: {packets}")
        print(f"Capa de Red: Enrutando -> {packets}")
        return packets

    def capa_enlace_de_datos(self, packets):
        """
        Capa de Enlace de Datos: Asegura la transferencia de datos libre de errores entre dos nodos adyacentes.
        
        :param packets: Paquetes de la capa de red.
        :return: Tramas con control de errores.
        """
        frames = [b'FRAME_START' + packet + b'FRAME_END' for packet in packets]  # Simula la creación de tramas.
        self.packet_log.append(f"Capa de Enlace de Datos: {frames}")
        print(f"Capa de Enlace de Datos: Creando tramas -> {frames}")
        return frames

    def capa_fisica(self, frames):
        """
        Capa Física: Transmite los bits a través del medio físico.
        
        :param frames: Tramas de la capa de enlace de datos.
        """
        for frame in frames:
            self.packet_log.append(f"Capa Física: {frame}")
            print(f"Capa Física: Transmitiendo -> {frame}")

# Función para simular la transmisión de datos a través del modelo OSI
def simular_transmision_datos():
    """
    Simula la transmisión de datos desde la capa de aplicación hasta la capa física.
    """
    osi_model = OSIModel()  # Crea una instancia del modelo OSI.
    
    datos_originales = "Mensaje de prueba"  # Datos originales en la capa de aplicación.
    data_presentation = osi_model.capa_aplicacion(datos_originales)
    data_session = osi_model.capa_presentacion(data_presentation)
    data_transport = osi_model.capa_sesion(data_session)
    segments = osi_model.capa_transporte(data_transport)
    packets = osi_model.capa_red(segments)
    frames = osi_model.capa_enlace_de_datos(packets)
    osi_model.capa_fisica(frames)

    # Imprime el registro del estado del paquete en cada capa
    print("\nRegistro del estado del paquete en cada capa:")
    for log_entry in osi_model.packet_log:
        print(log_entry)

# Ejecuta la simulación
simular_transmision_datos()
