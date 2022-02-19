from django.urls import path, include
from rest_framework import routers

from .views import TodoListView, TodolistAPIList, TodolistAPIUpdate, TodolistAPIDetail, TodolistViewSet

router = routers.SimpleRouter()
router.register(r'todolist', TodolistViewSet, basename='todolist')

urlpatterns = [
    # path('', TodoListView.as_view()),
    # path('<int:pk>/', TodoListView.as_view()),

    # path('', TodolistAPIList.as_view()),
    # path('<int:pk>/', TodolistAPIUpdate.as_view()),
    # path('detail/<int:pk>/', TodolistAPIDetail.as_view()),

    # path('', TodolistViewSet.as_view({'get': 'list'})),
    # path('<int:pk>/', TodolistViewSet.as_view({'put': 'update'})),

    path('', include(router.urls)),
]
