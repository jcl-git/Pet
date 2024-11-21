from django.urls import path
from . import views

urlpatterns = [
    path("cathome", views.cathome, name='cathome'),
    path('<int:cat_id>',views.catdetail,name='catdetail'),
    path('<int:cat_id>/createcatreview',views.createcatreview,name='createcatreview'),
    path('review/<int:review_id>', views.updatecatreview, name='updatecatreview'),
    path('review/<int:review_id>/delete', views.deletecatreview, name='deletecatreview'),
]
