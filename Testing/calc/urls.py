from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name ="home"),
    path('click', views.click, name = "click"),
    path('drop',views.drop, name = 'drop'),
    path('h', views.home, name = "h"),
    path('pandas',views.pandas, name="pandas"),
    #path('pandas2',views.pandas2, name="pandas2"),
    path('insert', views.insert, name="insert"),
    path('delete/<int:id>/', views.delete, name="delete")
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)