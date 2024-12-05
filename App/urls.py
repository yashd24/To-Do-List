from django.urls import path
from .views import RegisterUser, LoginUser, ToDoItemsView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('items/', ToDoItemsView.as_view(), name='items'),
    path('items/<int:pk>/', ToDoItemsView.as_view(), name='items' ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
