from django.shortcuts import render,redirect
from django.views import View
from . forms import DocumentForm
from .models import Document
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.

class CreateProfileView(CreateView):
    model=Document
    form_class=DocumentForm
    template_name='profile.html'
    success_url=reverse_lazy('thank_you')

# class CreateProfileView(View):

#     def get(self,request):
#         form=DocumentForm()
#         return render(request,'profile.html',{'form':form})
    
#     def post(self,request):
#         form=DocumentForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#         return render(request,'profile.html',{'form':form})





from django.views.generic import ListView
from . models import Document

# def imgPath()
class ImageList(ListView):
    model=Document
    template_name='imageList.html'
    context_object_name='image_lists'
    paginate_by=10

# class ImageList(View):
#     def get(self,request):
#         form=Document.objects.all()
#         lists=[]
#         for x in form:
#             st=str(x.upload)
#             lists.append(st[6:])
#         print(lists)
#         return render(request,'imageList.html',{'image_lists':form})
        
        



