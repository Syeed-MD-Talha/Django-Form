from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import reviewForm
from .models import reviewModel
from django.views import View
from django.views.generic import TemplateView



# Create your views here.
# def review(request):
#      if request.method=='POST':
#             form=reviewForm(request.POST)
#             if form.is_valid():
#                   # review=reviewModel(
#                   #       username=form.cleaned_data['username'],
#                   #       review=form.cleaned_data['review'],
#                   #       rating=form.cleaned_data['rating']
#                   # )
#                   # review.save()
#                   form.save() # It is done when model form has been used
#                   print(form.cleaned_data)
#                   return HttpResponseRedirect('thank-you')
     
#      else:form=reviewForm()
#      print("...........GET request")
#      return render(request,'review.html',{'form':form})

class review(View):
      def get(self,request):
            form=reviewForm()
            return render(request,'review.html',{'form':form})
            
      def post(self,request):
            form=reviewForm(request.POST)
            if form.is_valid():
                  form.save()
                  return HttpResponseRedirect('thank-you')
            
            return render(request,'review.html',{'form':form})
 

class thank_you(View):
      def get(self,request):
            return render(request,'thank_you.html')
      
# def thank_you(request):
#      return render(request,'thank_you.html')


# def reviewList(request):
#       return render(request,'reviewList.html')

class reviewList(TemplateView):
      template_name='reviewList.html'
      def get_context_data(self, **kwargs) -> dict[str, any]:
          context = super().get_context_data(**kwargs)
          context["reviews"] = reviewModel.objects.all()
          return context
      



class single_review(TemplateView):
    template_name = 'single_review.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs['id']
        context["review"] = reviewModel.objects.get(pk=review_id)
        is_favorite=self.request.session.get('favorite_review',0)==review_id
      #   print(is_favorite,self.request.session.get('favorite_review',0),review_id)
        my_fav=str(review_id)+'is_my_favorite_id'
        context["fav_review_id"] = self.request.session.get(my_fav,0)
        return context



    
class addFavorite(View):
    def post(self, request):
        review_id = request.POST.get('review_id')
        fav_review = reviewModel.objects.get(pk=review_id)
        is_favorite=fav_review+'is_my_favorite_id'
        request.session[is_favorite] = True
        return redirect('/review-list/'+review_id)

      