from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request

# Create your views here.

def main(request):

    # списки, первый содержит id валют для api

    list_id=[440,510,441,449,514,450,513,431,512,451,452,508,511,461,453,371,394,462,454,455,448,456,457,421,458,459,460,429,463,464,426]
    names=[]
    values=[]

    for i in list_id:

        # загружает из api названия валют в names и их стоимость в values

        res = urllib.request.urlopen('https://api.nbrb.by/exrates/rates/'+str(i)).read()
        json_data = json.loads(res)
        names.append(str(json_data['Cur_Name']))
        values.append(str(json_data['Cur_OfficialRate']))

    # получает значения из текстовых полей
    try:
        # колличество валюты
        value_0 = request.GET['value_0']
        # имя из которой нужно перевести
        name_v0 = request.GET['name_v0']
        # имя в которую нужно перевести
        name_v1 = request.GET['name_v1']
        answer = int(value_0) * float(values[int(names.index(str(name_v0)))]) / float(values[int(names.index(str(name_v1)))])
    except:
        # если выйдет ошибка или тестовые поля не были заполнены то ничего не выведет
        answer = ''
        name_v1 = ''
    return render(request, 'index.html', {'names': names, 'values': values, 'answer': answer, 'name_v1': name_v1})