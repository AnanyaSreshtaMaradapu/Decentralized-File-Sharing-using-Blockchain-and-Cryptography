

import mimetypes
import os
import pickle

from django.shortcuts import render
from django.http import HttpResponse, request
from .models import *

import matplotlib.pyplot as plt;
import numpy as np
import numpy
from django.shortcuts import render, redirect
from PIL import ImageTk, Image
from PIL import Image

from .DateTime import getdate


account_1 = "0x9d6aE39E79420B51511FE4Fbc24Ed6681f0Aae2f"                               # Ganache account address
private_key = "0x29f5bb068e1ab6b185d02415e5247a5986bb09046bb6a85696c8963163fcd6f4"     # Ganache account private key
from .BlockChain import compile_contract, deploy_contract
compiled_sol = compile_contract()
contract = deploy_contract(compiled_sol)
    



def homepage(request):
    d=files.objects.all()
    for d1 in d:
        contract.functions.addData(d1.recipient_email, str(d1.transaction_id)).transact({"from": account_1})
    return render(request, 'index.html')



def home(request):
    return render(request, 'index.html')

def signuppage(request):
    if request.method == 'POST':
        email = request.POST['email']

        d = users.objects.filter(email__exact=email).count()
        if d > 0:
            return render(request, 'signup.html', {'msg': "email Already Registered"})

        else:

            password = request.POST['password']
            phone = request.POST['phone']
            name = request.POST['name']

            from .HashCode import convert
            hashid=convert(email)

            from .GenerateKeys import generate
            generate(hashid)

            
            d = users(name=name, email=email, password=password, phone=phone)
            d.save()


            return render(request, 'signup.html', {'msg': "Register Success, You can Login.."})

    else:

        return render(request, 'signup.html')



def userloginaction(request):
	if request.method=='POST':
		uid=request.POST['uid']
		pass_word=request.POST['pwd']
		d=users.objects.filter(email__exact=uid).filter(password__exact=pass_word).count()
		
		if d>0:
			d=users.objects.filter(email__exact=uid)
			request.session['email']=uid
			request.session['name']=d[0].name
			return render(request, 'user_home.html',{'data': d[0]})
		else:
			return render(request, 'user.html',{'msg':"Login Fail"})
	else:
		return render(request, 'user.html')


def adminloginaction(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        pwd = request.POST['pwd']

        if uid == 'admin' and pwd == 'admin':
            request.session['adminid'] = 'admin'
            
            return render(request, 'admin_home.html')

        else:
            return render(request, 'admin.html', {'msg': "Login Fail"})

    else:
        return render(request, 'admin.html')



def adminhomedef(request):
    if "adminid" in request.session:
        uid = request.session["adminid"]
        return render(request, 'admin_home.html')

    else:
        return render(request, 'admin.html')

def adminlogoutdef(request):
    try:
        del request.session['adminid']
    except:
        pass
    return render(request, 'admin.html')



def userlogoutdef(request):
    email= request.session["email"]
    del request.session['email']
    return render(request, 'user.html')


def userhomedef(request):
	if "email" in request.session:
		email=request.session["email"]
		d=users.objects.filter(email__exact=email)
	
		return render(request, 'user_home.html',{'data': d[0]})

	else:
		return redirect('n_userlogout')

		
def viewprofilepage(request):
	if "email" in request.session:
		uid=request.session["email"]
		d=users.objects.filter(email__exact=uid)
		return render(request, 'viewpprofile.html',{'data': d[0]})

	else:
		return render(request, 'user.html')

from .HashCode import convert
from .GenerateKeys import getkeys

def fileupload(request):
    if request.method == 'POST':
        
        user = request.POST['user']
        
        remail,rname = user.split('|')
        
        rh=convert(remail)

        pk, sk=getkeys(rh)
              
        
        return render(request, 'uploadfile2.html', {'pk':pk, 'remail':remail, 'rname':rname})
        
    else:
        email = request.session["email"]
        data=users.objects.all().exclude(email=email)
        return render(request, 'uploadfile.html',{'data':data})
    
        
def fileupload2(request):
    if request.method == 'POST':

        from .DateTime import getdate
        ts=getdate()
        
        file = request.POST['file']
        rname = request.POST['rname']
        remail = request.POST['remail']
        import random
        tid=random.randrange(111111,999999)

        
        file2 = 'Data/' + file
        
        title = request.POST['title']
        name = request.session["name"];     
        email = request.session["email"]
        
        f = open(file2, "r")
        dt = f.read()
        rh=convert(remail)
        pk, sk=getkeys(rh)
        from .GenerateKeys import encrypt

        edata=encrypt(pk, dt)

        d=files(transaction_id=tid, sender_email=email, recipient_email=remail, title=title, file=edata)
        d.save()


        

        return render(request, 'user_home.html', {'msg': 'File has shared !! '})
        
    else:
        pass
    
        

def viewfiles(request):
    if "email" in request.session:
        email = request.session["email"]
        d = localfiles.objects.filter(remail=email)
   
        return render(request, 'viewfiles.html', {'data': d})
    
    else:
        return render(request, 'user.html')

def viewfile(request, op):
    if "email" in request.session:
        d = files.objects.filter(id=op)

        return render(request, 'viewfile.html', {'d': d[0]})

    else:
        return render(request, 'user.html')

	   

def updateprofile(request):
    if request.method == 'POST':
        name = request.POST["name"] 
        phone = request.POST['phone']
        email = request.session["email"]
        users.objects.filter(email=email).update(name=name, phone=phone)
        return render(request, 'user_home.html',{'msg':'Profile Updated !!'} )
       
    else:
        email = request.session["email"]
        d = users.objects.filter(email=email)
   
        return render(request, 'updateprofile.html', {'data': d[0]})




def updatepwd(request):
    if request.method == 'POST':
        newpwd = request.POST["newpwd"] 
        old = request.POST['old']
        email = request.session["email"]
        d=users.objects.filter(email=email).filter(password=old).count()
        if d>0:
            users.objects.filter(email=email).update(password=newpwd)
        return render(request, 'user_home.html',{'msg':'Password Updated !!'} )
       
    else:
        return render(request, 'updatepwd.html')




        
def inbox(request):
    if "email" in request.session:
        uid=request.session["email"]


        data = contract.functions.getData(uid).call()
        print(data,'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')

        d=[]

        for d1 in data:
            d2=files.objects.filter(transaction_id=d1)
            d2=d2[0]
            temp={'transaction_id':d2.transaction_id, 'sender_email':d2.sender_email, 'title':d2.title}
            d.append(temp)


        return render(request, 'inbox.html',{'data': d})

    else:
        return render(request, 'user.html')

def inbox2(request, op):
    if "email" in request.session:
        d = files.objects.filter(transaction_id=op)
        remail=request.session['email']
        rh=convert(remail)
        pk, sk=getkeys(rh)
        

        return render(request, 'viewifile.html', {'d': d[0],'sk':sk})

    else:
        return render(request, 'user.html')

def inboxdecrypt(request):
    if "email" in request.session:
        remail=request.session['email']
        id=request.POST['id']

        d = files.objects.filter(id=id)
        encdata=d[0].file

        rh=convert(remail)
        pk, sk=getkeys(rh)

        from .GenerateKeys import decrypt
        text=decrypt(sk, encdata)

        print(text,'*************************')

    

        return render(request, 'viewifile2.html', {'text':text, 'd':d[0]})

    else:
        return render(request, 'user.html')


       

def filesave(request):
    if request.method == 'POST':

        file = request.POST['data']
        name = request.POST['name']
        email = request.POST['email']
        tid = request.POST['id']

        
        title = request.POST['title']
        remail = request.session["email"]
        
    
        
        d=localfiles(transaction_id=tid, title=title, file=file, remail=remail)
        d.save()


        return render(request, 'user_home.html', {'msg': 'File has stored !! '})
        
    else:
        pass
    
      

def lviewfile(request, op):
    if "email" in request.session:
        d = localfiles.objects.filter(id=op)

        return render(request, 'lviewfile.html', {'d': d[0]})

    else:
        return render(request, 'user.html')

	   
def delete(request, op):
    if True:
        d = localfiles.objects.filter(id=op)
        d.delete()
        
        return redirect('viewfiles')
