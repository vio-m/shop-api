from rest_framework import views, viewsets, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from .models import *
from fashionStore.serializers import *
from django.views.decorators.csrf import csrf_exempt


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.values_list('id', 'size')
    serializer_class = SizeSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.prefetch_related('size').all() #objects.all()
    serializer_class = ProductSerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    @classmethod
    def get_extra_actions(cls):
        return []

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @classmethod
    def get_extra_actions(cls):
        return []

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        # Check if the email is already subscribed
        if Subscription.objects.filter(email=email).exists():
            return Response({'success': False, 'message': 'Email already subscribed.'})
        # Subscribe the email
        subscriber = Subscription(email=email)
        subscriber.save()
        # Return a success response
        return Response({'success': True, 'message': 'Thank you for subscribing.'})

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    #@csrf_exempt
    def post(self, request):
        print("request: ", request)
        return Response({'success': True, 'message': 'this is the ORDER post/response message.'})



'''
    
shipping_name = request.data.get('name')
shipping_address = request.data.get('address')
shipping_city = request.data.get('city')
shipping_state = request.data.get('state')
shipping_zip = request.data.get('zip')
payment_method = request.data.get('paymentMethod')


print("request: ", shipping_name, shipping_address)
return Response({'success': True, 'message': 'this is the ORDER post/response message.'})
        
        

        
'''