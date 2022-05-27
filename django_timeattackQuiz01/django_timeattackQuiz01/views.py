from django.http import HttpResponse
from django.shortcuts import render

# def base_response(request):
#     return HttpResponse("안녕하세요! 장고의 시작입니다!")

def show_index(request):
    return render(request,'index.html')
    def __init__(email,password):
        self.email