from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView

urlpatterns = [
    path('items/', PostListView.as_view(), name='item_list'),
    path('items/<int:pk>/', PostDetailView.as_view(), name='item_detail'),
    path('items/create/', PostCreateView.as_view(), name='item_create'),
    path('items/<int:pk>/update/', PostUpdateView.as_view(), name='item_update'),
    path('items/<int:pk>/delete/', PostDeleteView.as_view(), name='item_delete')
]