from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.serializers import Serializer
from .serializers import *
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import *

@api_view(['GET'])
def apibase(request):

    return Response(status= status.HTTP_200_OK)


@api_view(['POST'])
def register(request):

    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(user.password)
        user.save()
        token = Token.objects.get(user = user).key
        data['user_id'] = user.id
        data['token'] = token
         
        return Response(data,status=status.HTTP_200_OK)

    else:
        data = serializer.errors
        return Response(data,status= status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((IsAdminUser,))
@csrf_exempt
def create_advisor(request):

    serializer = AdivsorSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    else:
        data = serializer.errors
        return Response(data,status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))

def getlist(request,userid):
    
    advs = Advisor.objects.all()
    serializer  = AdivsorSerializer(advs,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))

def bookcall(request,userid,advid):
   
    calldata = {}
    calldata['userid'] = userid
    calldata['advid'] = advid
    calldata['time'] = request.data['time']
    serializer = CallSerializer(data = calldata)
    
    if serializer.is_valid():
        serializer.save()
        return Response(status= status.HTTP_200_OK)

    else:
        data = serializer.errors
        return Response(data,status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def booking(request,userid):

    bookings = Call.objects.filter(userid = userid)
    allbookings = []
    bkng = {}

    for booking in bookings:
        bkng['adv_name'] = booking.advid.name
        bkng['adv_pic'] = booking.advid.photo
        bkng['adv_id'] = booking.advid.id
        bkng['time'] = booking.time
        bkng['booking_id'] = booking.id

        allbookings.append(bkng)
    
    serializer = BookingSerializer(allbookings,many=True) 
    return Response(serializer.data,status = status.HTTP_200_OK)

    
    

