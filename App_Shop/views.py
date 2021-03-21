from django.shortcuts import render

from django.views.generic import ListView, DetailView

from App_Shop.models import Product

from django.contrib.auth.mixins import LoginRequiredMixin


class Home(ListView):
    model = Product
    template_name = 'App_Shop/home.html'
    queryset = Product.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Home, self).get_context_data(object_list=object_list, **kwargs)
        context['products'] = self.queryset
        context['search_text'] = self.request.GET.get('q', '')
        return context

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if query:
            self.queryset = Product.objects.filter(name__icontains=query)
        else:
            self.queryset = Product.objects.all()
        return super(Home, self).get(request=request, *args, **kwargs)


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'App_Shop/product_detail.html'
