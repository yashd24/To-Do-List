from django.urls import path
from .views import RegisterUser, LoginUser, ToDoItemsView

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('items/', ToDoItemsView.as_view(), name='items'),
    path('items/<int:pk>/', ToDoItemsView.as_view(), name='items' ),
]
