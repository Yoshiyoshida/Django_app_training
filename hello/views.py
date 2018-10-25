from django.shortcuts import render
from django.http import HttpResponse#クライアントに返す内容を管理するクラス


def index(request, id, nickname):#requestはHTTPRequestクラスのインスタンス
    #if 'msg' in request.GET:#request.GETは辞書のキー
        #msg = request.GET['msg']#msgはキーに対する値
    result = 'you typed :"' + str(id) + ':' + nickname + '".'
    return HttpResponse(result)
    """ 
    else:
        result = 'please send msg'
        return HttpResponse(result)
    #HttpResponse("返信内容")
    """

def test(request):
    return HttpResponse("TTTTTTTT")