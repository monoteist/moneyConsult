from django.urls import path

from dashboard.views import HomePageView, CategoryAddView, category_detail

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('category_add/', CategoryAddView.as_view(), name='category_add'),
    path('category_detail/<int:pk>', category_detail, name='category_detail')
]