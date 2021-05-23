
from django.contrib.auth import authenticate

from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny



class LoginAPIView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        if email and password:
            user = authenticate(email=email, password=password)  
            if user:
                update_last_login(None, user)   
                return Response({"token": user.auth_token.key, 'user_id':user.id})
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"error": "Email or Password is missing!!"}, status=status.HTTP_400_BAD_REQUEST)


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response({'token': token.key,'user_id': serializer.instance.id}, status=status.HTTP_201_CREATED)


class UserViewSet(viewsets.ModelViewSet):

    queryset = Account.objects.all()
    serializer_class = UserRegistrationSerializer




# class AdvisorList(generics.ListCreateAPIView):

#     def get_queryset(self):
#         queryset = Advisor.objects.filter(user_id=self.kwargs['pk'])
#         print(queryset)
#         return queryset
#     serializer_class = AdvisorSerializer

class AdvisorList(generics.ListAPIView):
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer



class AdvisorAdd(generics.CreateAPIView):
    serializer_class =AdvisorSerializer




class CreateBooking(APIView):
    def post(self, request, advisor_pk, pk):
        booking_time = request.data.get("booking_time")

        data = {
            'booking_time': booking_time,
            'advisor': advisor_pk,
        }
        serializer = AdvisorBookingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdvisorListBooking(generics.ListAPIView):
    serializer_class =AdvisorSerializerDate
    # queryset = Advisor.objects.all()
    def get_queryset(self):
        queryset = Advisor.objects.filter()
        print(queryset)
        return queryset
    





#     def get_queryset(self):
#         queryset = Advisor.objects.filter(user_id=self.kwargs['pk'])
#         print(queryset)
#         return queryset
#     serializer_class = AdvisorSerializer





    
