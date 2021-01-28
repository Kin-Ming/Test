from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Test, Document
from .forms import DocumentForm
from django.contrib import messages
import pandas as p
import mysql.connector
from sqlalchemy import types, create_engine
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.

def home(request):
    #return HttpResponse("NIAMA")
    data = Test.objects.all()

    return render(request,'home.html', {'Test_obj' : data})

def click(request):
    #val1 = str(request.POST["Accept"])

    #if val1 == "decline":
      return render(request,'base.html')
    #else:
      # return render(request,'base1.html')


def drop(request):
  val1 = str(request.POST["Cars"])
  return render(request,'base.html',{'Cars': val1})

def pandas(request):
  #convert csv file to database
  #engine = create_engine('mysql+mysqlconnector://'+'root'+':''@'+'localhost'+':'+'3306'+'/'+'django', echo=False)
  #g = request.POST['myfile']
  #chunksize = 1000

 #df=p.read_csv(r"C:\Users\user\Desktop\e.csv")
  #df.to_sql("lol",con=engine, if_exists='append',chunksize = chunksize)
 # df2 = len(df)
  #df3 = len(df.columns)

  #data_html = df.to_html()
 # context = {'loaded_data':data_html}
 # return render(request,'base1.html',context)

 if request.method == 'POST':
   form = DocumentForm(request.POST,request.FILES)
   if form.is_valid():
     form.save() 
     f = Document.objects.all()
     d = Document.objects.get(pk=5)
     df=p.read_csv(d.document)
     data_html = df.to_html()
     context = {'loaded_data':data_html, 'Test': f}
     return render(request,'base1.html',context)
 else:
    form = DocumentForm()
 return render(request,'base.html',{'form':form})

def insert(request):
  val1 = request.GET['name']
  val2 = request.GET['num']
  val3 = request.GET['des']
  db = Test()
  db.name = val1
  db.number = val2
  db.des=val3
  db.save()
   # back to the page
  return redirect('home')

def delete(request, id):
  d = Test.objects.get(pk = id)
  d.delete()
  return redirect('home')