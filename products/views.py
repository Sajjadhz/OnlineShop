import itertools

from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

from order.forms import UserNewOrderForm
from .models import Product, ProductGallery
from tags.models import Tag
from categories.models import ProductCategory


# in the case of function-based views we need to import Paginator from django.core.paginator to implement pagination

# Create your views here.

# here we implement products view as function-based view

def products(request):
    context = {}
    return render(request, 'product/products_list.html', context)


# here we implement products view as class-based view by inhering from ListView
class ProductsList(ListView):
    template_name = 'product/products_list.html'  # this is a built-in parameter and must be as it is
    paginate_by = 2  # this line of code is related to the pagination which shows 2 element in each page

    def get_queryset(self):  # this is a built-in method and must be as it is
        return Product.objects.get_active_products()  # here we filter-out non-active products


# we will use the following class to get products by their categories
class ProductsListByCategory(ListView):
    template_name = 'product/products_list.html'  # this is a built-in parameter and must be as it is
    paginate_by = 6  # this line of code is related to the pagination which shows 2 element in each page

    def get_queryset(self):  # this is a built-in method and must be as it is
        print(self.kwargs)  # this is a dictionary including category_name as keys and an string as value come from url
        # here we get value of dictionary, category_name is what we set in urls.py
        category_name = self.kwargs['category_name']
        print(category_name)
        category = ProductCategory.objects.filter(name__iexact=category_name).first()
        print(category)
        # category differs from category_name for example category can be in persian but category_name can not
        # here category_name is vegetables but category_name is سبزیجات
        if category is None:
            raise Http404('صفحه مورد نظر یافت نشد')
        return Product.objects.get_products_by_category(category_name)  # here we filter-out non-active products


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def product_detail(request, *args, **kwargs):
    selected_product_id = kwargs['productId']
    new_order_form = UserNewOrderForm(request.POST or None, initial={'product_id': selected_product_id})
    product_name = kwargs['name']
    product = Product.objects.get_by_id(selected_product_id)
    if product is None or not product.active:
        raise Http404('محصول مورد نظر یافت نشد')

    product.visit_count += 1
    product.save()

    related_products = Product.objects.get_queryset().filter(categories__product=product).distinct()
    grouped_related_products = my_grouper(3, related_products)

    galleries = ProductGallery.objects.filter(product_id=selected_product_id)
    print(galleries)
    grouped_galleries = list(my_grouper(3, galleries))
    print(grouped_galleries)

    context = {
        'product': product,
        'galleries': grouped_galleries,
        'related_products': grouped_related_products,
        'new_order_form': new_order_form
    }
    # tag = Tag.objects.first()   # this line shows how to get access to tags
    # print(tag.products.all())   # here you can see how to get products by their tag

    # print(product.tag_set.all())   # this line shows how to get access to tags by using related product
    return render(request, 'product/products_detail.html', context)


# the following class is for search view of products
class SearchProductsView(ListView):
    template_name = 'product/products_list.html'
    paginate_by = 2  # we need to include this line because the products_list.html uses pagination.

    def get_queryset(self):
        request = self.request
        print(request)
        print(request.GET)  # this is a dictionary including 'q' as key and a list which includes queries
        query = request.GET.get('q')
        if query is not None:
            # return Product.objects.filter(active=True, title__icontains=query)  # we can do this line in
            # models.ProductsManager, too
            return Product.objects.search(query)  # here we do same thing as did in previous line in another wy
        return Product.objects.get_active_products()

    '''
        __icontains => return results containing  this
        __iexact => return results containing exactly this       
        
        
    '''


def products_categories_partial(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'product/products_categories_partial.html', context)
