from django.urls import path
from .views import WorkList

urlpatterns = [
    path('', WorkList.as_view(), name='work-list'),
]