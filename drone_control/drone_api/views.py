# from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from djitellopy import Tello
from .serializers import CommandSerializer

# Create your views here.

drone_tello = Tello()
drone_tello.connect()

class DroneControlView(APIView):
    def post(self, request):
        serializer = CommandSerializer(data=request.data)
        
        # valida el tipo de instrucción enviada en la solicitud
        if serializer.is_valid():
            command_to_exec = serializer.validated_data['command']
            if command_to_exec == "takeoff":
                drone_tello.takeoff()
                drone_tello.move_up(20)
                drone_tello.move_left(10)
                drone_tello.move_forward(10)
                drone_tello.stream_on()
                frame_read = drone_tello.get_frame_read()
                # aquí debe ir el código que envía la fotografía a otra API
                drone_tello.streamoff()

                drone_tello.move_back(10)
                drone_tello.move_right(20)
                drone_tello.move_down(20)
                drone_tello.land()
            else:
                return Response(
                    {"error": "Comando no válido"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            return Response(
                {"status": "Comando ejecutado correctamente"},
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )