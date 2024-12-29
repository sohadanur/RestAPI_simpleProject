from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Message
from .serializers import MessageSerializer

class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = []
    http_method_names = ['post']

class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    http_method_names = ['get']
    