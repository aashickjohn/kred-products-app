from oshop.models import Product, Orders
from .serializers import ProductSerializer, OrderSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.

# to validate product is available or not
def productValidator(pid):
    try:
        product = Product.objects.get(id=pid)
        return product
    except:
        return False

# To update the quantity of products after successful orders.
def updateProductQuantity(data, prod_obj):
    prod_obj.quantity = prod_obj.quantity - data['buy_quantity']
    prod_obj.save()


class CustomAuthTokenLogin(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)  
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username,
            'FirstName': user.first_name,
            'LastName': user.last_name,
            'Created': created
        })


class ProductMaintain(APIView):
    def get(self, request, pid=None, format=None):

        if pid is not None:
            prod = productValidator(pid)
            if prod:
                serializer = ProductSerializer(prod)
                return Response(serializer.data)
            else:
                return Response({'Alert': 'Product Not Found'}, status=status.HTTP_404_NOT_FOUND)

        prod = Product.objects.all()
        serializer = ProductSerializer(prod, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message': 'Product add to inventory successfully'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class maintainOrders(APIView):
    def get(self, request, format=None):
        order = Orders.objects.filter(buyer_id=request.user.pk)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request, pid, format=None):
        prod_obj = productValidator(pid)
        order_data = request.data

        if prod_obj:
            serializer = OrderSerializer(data=request.data)
            user_id = request.user.pk
            if serializer.is_valid():
                serializer.save(buyer_id_id=user_id, prod_name=prod_obj.prod_name)
                updateProductQuantity(order_data, prod_obj)
                return Response({'Message': 'order placed successfully'}, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Alert': 'Product Not Found'}, status=status.HTTP_404_NOT_FOUND)
