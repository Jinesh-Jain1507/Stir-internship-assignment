from django.contrib import admin
from django.urls import path
from trends import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('run_script/', views.run_script, name='runscript'),
]
