from django.http import JsonResponse
from .serializers import CategorySerializer, TransactionSerializer
from rest_framework.views import APIView
from .models import Category, Transaction

# Create your views here.
