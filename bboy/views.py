from django.shortcuts import render
from django.http import HttpResponse
from .forms import BboyForm
from django.shortcuts import redirect
from .serializers import BboySerializer
from rest_framework import generics, status
from .models import Bboy
from rest_framework.decorators import api_view
from rest_framework.response import Response

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