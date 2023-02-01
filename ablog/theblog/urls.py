from django.urls import path
# from . import views 
from . views import  HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, LikeView, ProductView, ProductDetailView,HomeProductDetailView, AddDataView, Category2View, AddCategory2View  

urlpatterns = [
    # path('', views.home, name = "home"),
    path('', HomeView.as_view(), name = 'home'),
    path('products/', ProductView.as_view(), name = 'product'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name= 'article-detail'),
    path('home-product-detail/<int:pk>', HomeProductDetailView.as_view(), name= 'home-product-detail'),
    path('product-detail/<int:pk>', ProductDetailView.as_view(), name= 'product-detail'),
    path('add_post/',  AddPostView.as_view(), name= 'add_post'),
    path('add_data/',  AddDataView.as_view(), name= 'add_data'),
    path('add_category/',  AddCategoryView.as_view(), name= 'add_category'),
    path('add_category2/',  AddCategory2View.as_view(), name= 'add_category2'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name= 'update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name= 'delete_post'),
    path('category/<str:cats>/', CategoryView, name= 'category'),
    path('category2/<str:cats2>/', Category2View, name= 'category2'),
    path('like/<int:pk>', LikeView, name='like_post'), 
]
