from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todolist
from .serializers import TodolistSerializer



class TodolistViewSet(viewsets.ModelViewSet):
    # queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer


    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Todolist.objects.all()[:3]

        return Todolist.objects.filter(pk=pk)





#/////////////////////////////////////////////////////////////////////

class TodolistAPIList(generics.ListCreateAPIView):
    queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer

class TodolistAPIUpdate(generics.UpdateAPIView):
    queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer

class TodolistAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer



#/////////////////////////////////////////////////////////////////////

class TodoListView(APIView):
    def get(self, request):
        todolists = Todolist.objects.all()

        return Response({
            'Todolist': TodolistSerializer(todolists, many=True).data
        })
    def post(self, request):
        serializer = TodolistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'Create Todolist': serializer.data
        })
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Todolist.objects.get(pk=pk)
        except:
            return Response({"error": "Objects does not exists"})

        serializer = TodolistSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "todolist update": serializer.data
        })
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        todolist = Todolist.objects.get(pk=pk)
        todolist.delete()
        return Response({"Delete Todolist": f"pk={str(pk)}"})




