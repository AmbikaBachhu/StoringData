from django.shortcuts import render,redirect
from store.models import Storing
from store.forms import StoringForm
from django.contrib import messages
import gspread
import json
import requests
import base64

gc = gspread.service_account(filename='test.json')
sh = gc.open_by_key('1g2daLwurjj6XihtsRtmSgM5FGm0i3o8fDSjxdTAAW80')
worksheet = sh.sheet1



def showIndex(request):
    return render(request, "home.html", {'form': StoringForm})


def index(request):
    name = request.POST.get("Name")
    email = request.POST.get("Email")
    mobile= request.POST.get("Contactno")
    message = request.POST.get("Message")
    attach = request.FILES.get("Attachment")
    user = [name,email,mobile,message]
    worksheet.append_row(user)
    headers = {
        "Authorization": "Bearer ya29.a0AfH6SMDicMcor5qmBnaTFo_2BLOlxRIPcGTaLjKUGK2wkXQJjTFvglgUzD107dxZDK842EbrizbsrsEvT0SnlXpX1axbnu-9zHgizrfMeQBOHLpS_qUnk5bkSgPVwwS18Oo_da-5ZK4XHRdoQOTr8uKpJdJ7aTWJYZ0"}
    para = {
        "name": "Image.png",
        "parents": ["1JbIdSS_ThYAwVANCdjTtYKIrs6LR9XN_"]
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open("./car.png", "rb")
    }
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )
    print(r.text)
    Storing(Name=name,Email=email,Contactno=mobile,Message=message,Attachment=attach).save()
    messages.success(request, "Thanks for Registration")
    return redirect('home')
