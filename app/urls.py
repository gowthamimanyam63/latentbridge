from django.urls import path,include
from app import views
app_name='gowthami'
from rest_framework import routers



router=routers.DefaultRouter()
router.register('Studentviewset',views.StudentViewset,basename="Studentviewset")

urlpatterns = [
    path('hello',views.Student_detail.as_view(),name='Student_detail'),
    path('hi',include(router.urls)),
]
