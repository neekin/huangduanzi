from django.shortcuts import render

# Create your views here.
def index(res):
   return render(res,'huangduanzi/index.html')