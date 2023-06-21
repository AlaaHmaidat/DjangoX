from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='Blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='Blog_detail'),
    path('blog/create/', BlogCreateView.as_view(), name='Blog_create'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='Blog_update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='Blog_delete'),
]