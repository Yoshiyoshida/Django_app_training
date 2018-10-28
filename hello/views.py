from django.shortcuts import render
from django.http import HttpResponse#クライアントに返す内容を管理するクラス


def index(request):#requestはHTTPRequestクラスのインスタンス
    params = {
            'title' : 'Hello/Index',
            'msg' : 'sample',
            'goto' : 'next',
    }
    return render(request, 'hello/index.html', params)
            #render(httpRequest, テンプレート)
    #if 'msg' in request.GET:#request.GETは辞書のキー
        #msg = request.GET['msg']#msgはキーに対する値

def next(request):
    params = {
            'title' : 'Helo/Next',
            'msg' : 'これはもう一つのページです',
            'goto' : 'index',
    }

    return render(request, 'hello/index.html', params)