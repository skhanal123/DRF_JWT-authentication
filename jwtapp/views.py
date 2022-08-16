from django.shortcuts import render
from rest_framework.response import Response
from .models import Brand
from .serializers import BrandSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, DjangoModelPermissions

class BrandModelViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    authentication_classes =[JWTAuthentication]
    permission_classes = [DjangoModelPermissions]
