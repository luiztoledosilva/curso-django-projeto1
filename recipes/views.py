from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse('''<!doctype>
    <html>
    <head><title>Olá mundo</title></head>                    
    <body>
        <h1>Olá mundo</h1>                    
    </body>
    </html>                    
                        
                        
                        
        ''')

def contato(request):
    return HttpResponse('contato')

def sobre(request):
    return HttpResponse('sobre') 

