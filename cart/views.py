from rest_framework import viewsets
from .models import Cart
from .serializers import CartSerializer
from rest_framework.permissions import IsAuthenticated

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]