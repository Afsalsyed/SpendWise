from django.http import JsonResponse
from .serializers import CategorySerializer, TransactionSerializer
from rest_framework.views import APIView
from .models import Category, Transaction

# Create your views here.
class CategoryManagementView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many= True)
        return JsonResponse(serializer.data, safe=False)
        
    def post(self, request):
        data = request.data
        serializer =CategorySerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Category created successfully"}, status = 201)
        return JsonResponse({"message" : "Category creation failed"}, status = 400)

class CategoryEditManagementView(APIView):
    def put(self, request, id):
        try:
            category = Category.objects.get(id=id)
            serializer = CategorySerializer(category, data = request.data)
        except Category.DoesNotExist:
            return JsonResponse({"message" : "Category not found"}, status= 404)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message" : "Category edited successfully"}, status = 204)
        return JsonResponse(serializer.errors, status = 400)

    def delete(self, request, id):
        try:
            category = Category.objects.get(id=id)
            category.delete()
            return JsonResponse({"message" : "Category deleted successfully"}, status = 200)
        except Category.DoesNotExist:
            return JsonResponse({"message" : "Category not found"}, status = 404)

class TransactionManagementView(APIView):
    def get(self, request):
        transaction = Transaction.objects.filter(user= request.user).order_by('-id')
        serializer  = TransactionSerializer(transaction, many = True)
        return JsonResponse(serializer .data, safe = False)

    def post(self, request):
        data = request.data
        serializer = TransactionSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "New transaction added successfully"}, status = 201)
        return JsonResponse({"message" : "Failed to add transaction"}, status = 400)

class TransactionEditManagementView(APIView):
    def put(self, request, id):
        try:
            transaction = Transaction.objects.get(id=id)
            serializer = TransactionSerializer(transaction, data = request.data)
        except Transaction.DoesNotExist:
            return JsonResponse({"message" : "Transaction not found"}, status = 404)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message" : "Transaction edited successfully"}, status =204)
        return JsonResponse(serializer.errors, status= 400)

    def delete(self, request, id):
        try:
            transaction = Transaction.objects.get(id = id)
            transaction.delete()
            return JsonResponse({"message" : "Transaction deleted successfully"}, status =200)
        except Transaction.DoesNotExist:
            return JsonResponse({"message" : "Transaction not found"}, status = 404)
