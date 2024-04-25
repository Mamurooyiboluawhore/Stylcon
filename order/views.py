from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Order
from .serializers import OrderSerializers, OrderCreateSerializer
from rest_framework import status



class OrderList(APIView):
    """
    Retrieve all orders from the database.
    """

    def get(self, request, format=None):
        """
        Get all orders from the database.
        """
        try:
            orders = Order.objects.all()
            serializer = OrderSerializers(orders, many=True)
            response = {
                'message': 'list of all orders',
                'status': status.HTTP_200_OK,
                'data': serializer.data
                }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'error': str(e),
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class OrderDetailViews(APIView):
    def get_order_by_id(self, id):
        '''
        Function to fetch order by its ID
        '''
        try:
            order = Order.objects.get(pk=id)
            serializer = OrderSerializers(order)
            response = {
                'message': 'Order for on product',
                'status': status.HTTP_200_OK,
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            response = {
                "Error": "Order does not exist",
                "Status": status.HTTP_404_NOT_FOUND
                }, status.HTTP_404_NOT_FOUND
            return Response(response)
        except Exception as e:
            response = {
                'message': 'Internal Server Error',
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def post(self, request, format=None):
        '''
            Create a new order with the given data
        '''
        serializer = OrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.filter(user__username=serializer.validated_data['buyer']).first()
            product = Product.objects.filter(productId=serializer.validated_data['product'], seller=user).first()
            if user is None or user != request.user:
                response = {'error':'User does not exists'}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            item = Product.objects.filter(item_name=serializer.validated_data['product'], seller=user).first()
            if item is None:
                response={'error':'Item Does Not Exists.'}
                return  Response(response, status=status.HTTP_400_BAD_REQUEST)
            order = serializer.save(seller=user, buyer=request.user, item=item)
            data = OrderSerializers(order).data
            response = {
                'message': 'Order created successfully',
                'status': status.HTTP_201_CREATED,
                'data': data
                }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            print(serializer._errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        



    






    def post(self, request):
        pass

    def update(self, request, pk):
        pass

    def delete(self, request, pk):
        pass




