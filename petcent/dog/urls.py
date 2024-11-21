from django.urls import path
from . import views


urlpatterns = [
    path("doghome", views.doghome, name='doghome'),
    path('<int:dog_id>', views.dogdetail, name='dogdetail'),
    path('<int:dog_id>/createdogreview',views.createdogreview,name='createdogreview'),
]