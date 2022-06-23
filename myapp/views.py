from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth  import authenticate,  login, logout
from django.http import HttpResponse
import requests
from django.contrib.auth.decorators import login_required

from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import permission_classes,authentication_classes,api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from datetime import datetime,date





def format_dat(data):
    data= data[:4]+"-"+data[4:6]+"-"+data[6:]
    data= datetime.strptime(data,"%Y-%m-%d")

    return data.date()


@login_required
def index(request):
    return render(request, 'myapp/index.html')



login_required
@api_view(http_method_names=['GET'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def read_json_data(request):
    f = open('/home/ra_d2/sample_proj/data/gst_json.txt', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="application/json")


@login_required
def create_db(request):
    try:
        print(request.user)
        key  =  Token.objects.get(user=request.user)

        print("-------------------in db     ",key)
        url = 'http://127.0.0.1:8000/read_json_data/'
        print(f'Token {key}')
        headers = {'Authorization': f'Token {key}'}
        r = requests.get(url,headers=headers)
        print(r.text)


        data = r.json()
        obj_list = []
        l = []
        for dict1 in data:
            for i in dict1:
                dict1['InvoiceDate']  = format_dat(dict1['InvoiceDate'])
                p = date.isoformat(dict1['InvoiceDate'])
                k=[dict1['SiteCode'],p,dict1['InvoiceNo'],int(float(dict1['Quantity'])),dict1['TotalInvAmt']]
                l.append(k)

                data_obj = StoreDatabse(
                    store_code=dict1['SiteCode'],
                    bill_date = dict1['InvoiceDate'],
                    bill_no = dict1['InvoiceNo'],
                    item_count=int(float(dict1['Quantity'])),
                    sale_amount=float(dict1['TotalInvAmt'])
                )
                obj_list.append(data_obj)
                
                break
        StoreDatabse.objects.all().delete()

        StoreDatabse.objects.bulk_create(obj_list)
        
        for i in l:
            print(i)
        print(len(l))
        context = {'db_data':l}
        return render(request,"myapp/show_table.html",context)
        
    except:
        html = "<html><body>Requested user is not authenticated</body></html>"

        return HttpResponse(html)





def create_user(request):
    print("in sign up111")
    print(request)

    if request.method == 'POST':
        print("in sign up")
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        myuser = User.objects.create_user(username, password=password)
        myuser.save()
        return redirect('myapp:index')
    return render(request,'myapp/signup.html')

def login_view(request):
    print(request)
    if request.method=="POST":
        # Get the post parameters
        print(request.POST['username'])
        loginusername=request.POST['username']
        loginpassword=request.POST['password']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            # messages.success(request, "Successfully Logged In")
            return redirect("myapp:index")
        # else:
        #     print("*************invalid credeentials")
        #     return render(request,'bus_data_app/errors.html')

    return render(request,'myapp/logins.html')

def logout_view(request):
    print("in logout")
    print(request)
    logout(request)
    return redirect('myapp:login_view')