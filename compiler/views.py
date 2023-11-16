from django.shortcuts import render,HttpResponse
from django.conf import settings
import json
import requests
import base64
from django.contrib.auth.decorators import login_required
from user.models import User_profile

API_ENDPOINT = "https://api.jdoodle.com/v1/execute"

client_id = "2fa071e557985ea0c83222e82950de59"
client_secret = "bdda69dd30f54355cd5878b26e97d97ad13b2c5cae62fede7010c72b2039ea82"

LANG_CODE = { 'c': 1, 'java': 3, 'cpp14': 3, 'python3': 3,'go': 3,
            'sql': 3,'csharp': 3,'dart': 3,'nodejs': 3,'kotlin': 2,'brainfuck': 0,}


# @login_required(login_url='/accounts/login/')
def code_editor(request):
    return render(request,'code_editor.html')


@login_required(login_url='/accounts/login/')
def result(request):
    if request.method == "POST":
        source = request.POST.get("script")
        lang = request.POST.get("lang")
        stdin = request.POST.get("stdin")
        u_id = request.user.id
        usr = User_profile.objects.get(pk=u_id)
        usr.n_subm += 1
        if check_lang(usr,lang):
            usr.lang +=lang+","
        usr.save()
        data = {'clientId':client_id,
                'clientSecret':client_secret,
                'script':source,
                'stdin':stdin,
                'language':lang,
                'versionIndex':LANG_CODE[lang],
            }
             
        try:
            headers = {'Content-type': 'application/json'}
            r = requests.post(url = API_ENDPOINT, data = json.dumps(data), headers = headers)
            json_data = r.json()
            print(json_data)
            status = r.status_code
            print(status)
            #output = Robject(r.json())
            output = json_data['output']
            if not output:
                output = message.replace("\n","<br>")
        except Exception as e:
            print(e)
            output = settings.ERROR_MESSAGE
        print(output)   
        return HttpResponse(json.dumps({'output': json_data['output']}), content_type="application/json")
    else:
        return render(request,'code_editor.html',locals())


def check_lang(self,lang):
    lang_array = self.lang.split(",")
    for lng in lang_array:
        if lng == lang:
            return False
    return True            


'''
class Robject():
    def __init__(self, result):
        self.output = result['output']
        self.memory = result['memory']
        self.time = result['cpuTime']

'''