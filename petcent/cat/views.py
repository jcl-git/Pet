from gc import get_objects

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Cat,Review
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def cathome(request):
    searchTerm=request.GET.get('searchCat')
    if searchTerm:
        cat_list=Cat.objects.filter(title=searchTerm)
    else:
        cat_list=Cat.objects.all()
    paginator=Paginator(cat_list,2)
    page_number=request.GET.get('page',1)
    cats=paginator.page(page_number)
    return render(request,'cathome.html',{'searchTerm':searchTerm,'cats':cats})


def home(request):
    return render(request,'home.html',{'name':'OSYouth'})

def signup(request):
    email=request.GET.get('email')
    return render(request,'signup.html',{'email':email})

def catdetail(request,cat_id):
    cat=get_object_or_404(Cat,pk=cat_id)
    reviews=Review.objects.filter(cat=cat)
    return render(request,'catdetail.html',{'cat':cat,'reviews':reviews})

@login_required
def createcatreview(request,cat_id):
    cat = get_object_or_404(Cat,pk=cat_id)
    if request.method=='GET':
        return render(request,'createcatreview.html',{'form':ReviewForm,'cat':cat})
    else:
        try:
            form=ReviewForm(request.POST)
            newReview=form.save(commit=False)
            newReview.user=request.user
            newReview.cat=cat
            newReview.save()
            return redirect('catdetail',newReview.cat.id)
        except ValueError:
            return render(request,'createcatreview.html',{'form':ReviewForm,'error':'非法数据'})


@login_required
def updatecatreview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'updatecatreview.html', {'review': review, 'form': form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('catdetail', review.cat.id)
        except ValueError:
            return render(request, 'updatecatreview.html',
                            {'review': review, 'form': form, 'error': '提交非法数据'})

@login_required
def deletecatreview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('catdetail',review.cat.id)