from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import BboyForm
from .serializers import BboySerializer, RegisterSerializer, LoginSerializer
from .models import Bboy
from rest_framework import generics, status, views
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import login, logout

# Create your views here.

def index(request):
    return HttpResponse('Hello world!')

def hello(request):
    context = {
        'name':'Dan'
    }
    return render(request, 'hello.html', context)

def form(request):
    # 定義class module為變數
    form =  BboyForm()
    
    # 用if判斷傳送的method是POST
    if request.method == 'POST':
        # 再使用request.POST, 儲存表單內容
        form - BboyForm(request.POST)
        
        # 並且使用is_valid來判斷資料是否有效
        if form.is_valid():
            form.save()
            return redirect('/hello')
    
    context = {
        'form':form,
    }
    
    # 最後用render把context = form，渲染回去
    return render(request, 'form.html', context)

class BboyListAPIView(generics.ListAPIView):
    queryset = Bboy.objects.all()
    serializer_class = BboySerializer
    
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# @api_view(['GET'])
# def Bboy_data(request):
#     if request.method == 'GET':
#         bboy = Bboy.objects.all()
#         serializer = BboySerializer(bboy, many=True)
        
#         return Response(serializer.data)

@api_view(['GET', 'POST'])
def Bboy_data(request):
    
    if request.method == 'GET':
        bboy = Bboy.objects.all()
        serializer = BboySerializer(bboy, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = BboySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GenericAPIView, 是一個可以自定義的api view，寫完必要的serializer_class之後，
# 我們定義使用post method的功能
class RegisterAPIView(generics.GenericAPIView):
    
    serializer_class = RegisterSerializer
    
    def post(self, request):
        # 讓輸入的值成為serializer，可以使用data=request.data方式
        serializer = self.serializer_class(data=request.data)
        # 用is_valid來驗證serializer
        if serializer.is_valid():
            serializer.save()
        
            return Response(
                {'message': 'Account has been created suceessfully.'},
                status=status.HTTP_201_CREATED)
            
        return Response(
            {'message': 'The input content is invalid.'},
            status=status.HTTP_400_BAD_REQUEST
        )

class LoginView(generics.GenericAPIView):
    
    serializer_class = LoginSerializer
    
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data, context={'request':self.request})
        
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            msg = {
                'success':True,
                'messgae':"Validation success"
            }
            return Response(msg, status=status.HTTP_202_ACCEPTED)
        
        return Response({
            'success':False,
            'message':'Wrong username or password.'
        }, status=status.HTTP_400_BAD_REQUEST
                        )

class LogoutAPIView(views.APIView):
    
    def get(self, request):
        logout(request)
        
        return Response({'message':'logout successfully.'}, status=status.HTTP_200_OK)