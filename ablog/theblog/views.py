# from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post, Product, ProductData, Category2, HomeProductData
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    # model = Post
    model = HomeProductData
    template_name = 'home.html'
    # ordering = ['-publication_date']


    def get_context_data(self, *args, **kwargs): 
        #  cat_menu = Category.objects.all()
         cat_menu2 = Category2.objects.all()
         context = super(HomeView, self).get_context_data(*args, **kwargs)
         context["cat_menu"] = cat_menu2
         return context

    def get_context_data(self, *args, **kwargs): 
         cat_menu = Category.objects.all()
         cat_menu2 = Category2.objects.all()
         #allCats = 
         context = super(HomeView, self).get_context_data(*args, **kwargs)
         context["cat_menu"] = cat_menu
         return context    



class ProductView(ListView):
    model = ProductData
    template_name = 'products.html'
    # ordering = ['-publication_date']

    def get_context_data(self, *args, **kwargs): 
        cat_menu = Category.objects.all()
        context = super(ProductView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs): 
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        
        # likes code
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        return context

class ProductDetailView(DetailView):
    model = ProductData
    template_name = 'productDetail.html'
    

    def get_context_data(self, *args, **kwargs): 
        cat_menu = Category.objects.all()
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class HomeProductDetailView(DetailView):
    model = HomeProductData
    template_name = 'homeProductDetail.html'

    def get_context_data(self, *args, **kwargs): 
        cat_menu = Category.objects.all()
        context = super(HomeProductDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        #context["home_product_data"] = home_product_data
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def get_context_data(self, *args, **kwargs): 
        cat_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddDataView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_data.html'

    def get_context_data(self, *args, **kwargs): 
        cat_menu = Category.objects.all()
        context = super(AddDataView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'   
    fields = '__all__'

    def get_context_data(self, *args, **kwargs): 
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class AddCategory2View(CreateView):
    model = Category2
    template_name = 'add_category2.html'   
    fields = '__all__'

    def get_context_data(self, *args, **kwargs): 
        cat_menu2 = Category2.objects.all()
        context = super(AddCategory2View, self).get_context_data(*args, **kwargs)
        context["cat_menu2"] = cat_menu2
        return context

#def CategoryView(request, cats):
    #category_products = ProductData.objects.filter(category=cats.replace('-', ' '))
    #return render(request, 'categories.html', {'cats': cats.replace('-', ' '), 'category_products': category_products})

def CategoryView(request, cats):
    category_products = ProductData.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.replace('-', ' '), 'category_products': category_products})
  

def Category2View(request, cats2):
    category2_products = ProductData.objects.filter(category2=cats2.replace('-', ' '))
    return render(request, 'category2.html', {'cats2': cats2.replace('-', ' '), 'category2_products': category2_products})
           
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = EditForm
    # form_class = PostForm
    # fields =['title', 'title_tag', 'body']
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

    