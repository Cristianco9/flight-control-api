# from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from djitellopy import Tello
from .serializers import CommandSerializer

# Create your views here.

# Importa la clase Tello desde la biblioteca djitellopy para controlar el dron.
from djitellopy import Tello

# Importa la clase APIView de Django REST framework para manejar
# vistas basadas en clases.
from rest_framework.views import APIView

# Importa Response y status desde Django REST framework para manejar
# las respuestas HTTP.
from rest_framework.response import Response
from rest_framework import status

# Importa el serializador CommandSerializer para validar y deserializar
# los datos de entrada.
from .serializers import CommandSerializer

# Crea una instancia del dron Tello y se conecta a él.
drone_tello = Tello()
drone_tello.connect()

# Define una vista para el control del dron, utilizando la API
# de Django REST framework.
class DroneControlView(APIView):
    def post(self, request):
        # Serializa y valida los datos de la solicitud.
        serializer = CommandSerializer(data=request.data)
        
        # Verifica si los datos son válidos.
        if serializer.is_valid():
            # Obtiene el comando validado de los datos serializados.
            command_to_exec = serializer.validated_data['command']
            
            # Ejecuta el comando 'takeoff'.
            if command_to_exec == "takeoff":

                # Imprime el nivel de batería del dron
                print(f"Batería: {drone_tello.get_battery()}%")

                """
                # El dron despega.
                drone_tello.takeoff()
                # El dron se mueve hacia arriba 20 cm.
                drone_tello.move_up(20)
                # El dron se mueve hacia la izquierda 10 cm.
                drone_tello.move_left(10)
                # El dron se mueve hacia adelante 10 cm.
                drone_tello.move_forward(10)
                # Enciende la transmisión de video.
                drone_tello.streamon()
                
                # Obtiene el cuadro de la transmisión de video.
                frame_read = drone_tello.get_frame_read()
                
                # Aquí debe ir el código que envía la fotografía a otra API.
                # Apaga la transmisión de video.
                drone_tello.streamoff()

                # El dron vuelve a la posición inicial.

                # El dron se mueve hacia atrás 10 cm.
                drone_tello.move_back(10)
                # El dron se mueve hacia la derecha 20 cm.
                drone_tello.move_right(20)
                # El dron se mueve hacia abajo 20 cm.
                drone_tello.move_down(20)
                # El dron aterriza.
                drone_tello.land()
                """

                # El dron despega.
                drone_tello.takeoff()
                    
                # El dron se eleva 1 metro (100 cm).
                drone_tello.move_up(100)
                    
                # Realiza un cuadrado de 1 metro por 1 metro.

                # El dron avanza 1 metro.
                drone_tello.move_forward(20)
                # El dron gira 90 grados a la derecha.
                drone_tello.rotate_clockwise(90)

                drone_tello.move_forward(20)
                # El dron gira 90 grados a la derecha.
                drone_tello.rotate_clockwise(90)

                drone_tello.move_forward(20)
                # El dron gira 90 grados a la derecha.
                drone_tello.rotate_clockwise(90)

                drone_tello.move_forward(20)
                # El dron gira 90 grados a la derecha.
                drone_tello.rotate_clockwise(90)
                    
                # El dron aterriza.
                drone_tello.land()

            else:
                # Devuelve una respuesta de error si el comando no es válido.
                return Response(
                    {"error": "Comando no válido"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Devuelve una respuesta de éxito si el comando
            # se ejecuta correctamente.
            return Response(
                {"status": "Comando ejecutado correctamente"},
                status=status.HTTP_200_OK
            )
        
        # Devuelve una respuesta de error si los datos de la
        # solicitud no son válidos.
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )