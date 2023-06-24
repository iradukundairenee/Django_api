from django.urls import path
from .views import CompanyInfoViews

urlpatterns = [
    path('company-info/', CompanyInfoViews.as_view()),
    path('company-info/<int:id>', CompanyInfoViews.as_view())
]