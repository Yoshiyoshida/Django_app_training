from django.shortcuts import render
from django.http import HttpResponse#クライアントに返す内容を管理するクラス


def index(request):#requestはHTTPRequestクラスのインスタンス
    #if 'msg' in request.GET:#request.GETは辞書のキー
        #msg = request.GET['msg']#msgはキーに対する値
    return render(request, 'hello/index.html')

def test(request):
    return HttpResponse("TTTTTTTT")