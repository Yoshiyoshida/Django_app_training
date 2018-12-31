from django.shortcuts import render
from django.http import HttpResponse#クライアントに返す内容を管理するクラス
from .forms import  HelloForm

def index(request):#requestはHTTPRequestクラスのインスタンス
    params = {
            'title' : 'Hello/Index',
            'msg' : 'お名前は?',
            'form' : HelloForm()
    }
            #render(httpRequest, テンプレート)
    #if 'msg' in request.GET:#request.GETは辞書のキー
        #msg = request.GET['msg']#msgはキーに対する値

    if (request.method == 'post'):
        params['message'] = '名前' + request.POST['name'] + '<br>メール: ' + request.POST['mail'] + '<br>年齢: ' + request.POST['age']
        params['form'] = HelloForm(request.POST)

    return render(request, 'hello/index.html', params)


def form (request):
    msg = request.POST['msg']
    params = { 
        'title':'Hello/Form',
        'msg' : 'こんにちは' + msg + 'さん',
    }

    return render(request, 'hello/index.html', params)