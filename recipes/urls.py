from django.urls import path

from recipes.views import home, contato, sobre

urlpatterns = [
    ##path('admin/', admin.site.urls),

    path('', home), #HOME
    path('sobre/', sobre), #sobre
    path('contato/', contato), #contato
    
    
]
