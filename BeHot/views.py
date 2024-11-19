from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class Entrance(TemplateView):
     template_name = "dykespage.html"


class Oshinagaki(ListView):
     model = Product
     template_name = "./dykeheya/product_list.html" #ファイルの名前リンク。URLと同一にする必要はない。
     paginate_by = 5

class Shinkan(CreateView):
     model = Product
     template_name = "./dykeheya/product_form.html"
     fields = "__all__"

class Edit(UpdateView):
     model = Product
     fields ="__all__"
     template_name = "./dykeheya/product_edit_form.html"

class Kyukan(DeleteView):
     model = Product
     template_name = "./dykeheya/product_confirm_delete.html"
     success_url = reverse_lazy("list")

class Preview(DetailView):
     model = Product
     fields = "__all__"
     template_name = "./dykeheya/product_detail.html"

