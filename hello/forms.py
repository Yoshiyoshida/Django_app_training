from django import forms

class HelloForm (forms.Form):
    name = forms.CharField(label = 'name')
    mail = forms.CharField(label = 'mail')
    age = forms.IntegerField(label = 'age')
    #CharField:テキスト用フィールド
    #IntergerFiled : 整数用フィールド