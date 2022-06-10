from django.shortcuts import render
from django.views import View
from .models import Category, Drink
# Create your views here.


class HomeView(View):
    def get(self,request):
        return render(request, 'index.html')

    def post(self, request):
        category=request.POST.get('category',None)

        # category_obj = Category.objects.get(id=category)
        #
        # data=Drink.objects.filter(category=category_obj).values()
        prefetch_qs = Category.objects.prefetch_related('drink_set')
        drinks = []
        for item in prefetch_qs:
            data = [{
                "name":drink.name
            } for drink in item.drink_set.filter(category_id = category)
            ]
            if data:
                drinks.append({"drinks":data})

        print("drinks = ", end=""), print(drinks)

        return render(request, 'index.html', {"data":drinks})



