from django.shortcuts import render, redirect

from django.db.models import Sum
from django.views.generic import ListView, View

from dashboard.models import Category



class HomePageView(ListView):

    template_name = 'dashboard/index.html'
    context_object_name = 'categories'

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return
        queryset = Category.objects.filter(author=self.request.user).prefetch_related(
            'payments').annotate(payments_sum=Sum('payments__price'))
        return queryset


class CategoryAddView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard/category_add.html')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        category = Category(name=name, author=request.user)
        category.save()
        return redirect('home')
        

def category_detail(request):
    category = Category.objects.filter()
    return render(request, 'dashboard/category_detail.html')